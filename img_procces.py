import cv2
import numpy as np
from tensorflow.keras.models import load_model, Model
from skimage.filters import threshold_local
import imutils


filchy_model = load_model("./dependencies/models/filchy.h5")
vgg16_model = load_model("./dependencies/models/vgg16.h5")
mobilenet_model = load_model("./dependencies/models/mobilenet.h5")

def img_preprocces():
	img = cv2.imread("dependencies/images/predict1.png")
	img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	img = cv2.subtract(255, img)
	img = cv2.resize(img, (28, 28))
	img = img.astype("float32") / 255
	img = np.array(img).reshape(-1, 28, 28, 1)
	return img

def img_prediction(img, model):
	if model == "filchy":
		nums = filchy_model.predict(img)
		num = np.argmax(nums, axis=1)
		final_num = str(num)
		final_num = final_num[1]

		layer_outputs = [layer.output for layer in filchy_model.layers]
		activation_model = Model(inputs=filchy_model.input, outputs=layer_outputs)
		activations = activation_model.predict(img)

		return final_num, activations

	elif model == "vgg16":
		nums = vgg16_model.predict(img)
		num = np.argmax(nums, axis=1)
		final_num = str(num)
		final_num = final_num[1]

		layer_outputs = [layer.output for layer in vgg16_model.layers]
		activation_model = Model(inputs=vgg16_model.input, outputs=layer_outputs)
		activations = activation_model.predict(img)

		return final_num, activations

	elif model == "mobilenet":
		nums = mobilenet_model.predict(img)
		num = np.argmax(nums, axis=1)
		final_num = str(num)
		final_num = final_num[1]

		layer_outputs = [layer.output for layer in mobilenet_model.layers]
		activation_model = Model(inputs=mobilenet_model.input, outputs=layer_outputs)
		activations = activation_model.predict(img)
		
		return final_num, activations

def multi_img_predict():
	image = cv2.imread("dependencies/images/predict2.png")

	#perform basic operation to smooth image
	img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	img = cv2.GaussianBlur(img, (5, 5), 0)

	#find threshold
	ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	#find contours and draw contours
	ctrs, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(image,ctrs,-1,(255,255,0),2)
	rects = [cv2.boundingRect(ctr) for ctr in ctrs]

	for rect in rects:
		x, y, w, h = rect
		if  h > 50 and h < 150  or w > 10 :
			#draw rectangel on image
			cv2.rectangle(image, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
			leng = int(rect[3] * 1.6)
			pt1 = abs(int(rect[1] + rect[3] // 2 - leng // 2))
			pt2 = abs(int(rect[0] + rect[2] // 2 - leng // 2))
			roi = img[pt1:pt1+leng, pt2:pt2+leng]
			#resize image
			roi = cv2.resize(roi,(28, 28), interpolation=cv2.INTER_AREA)
			roi = roi.reshape(-1,28, 28, 1)
			roi = np.array(roi, dtype="float32")
			roi /= 255
			pred_array = filchy_model.predict(roi)
			pred_array = np.argmax(pred_array)
			cv2.putText(image, str(pred_array), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 3)
			cv2.imwrite("dependencies/images/predict2.png", image)

def order_points(pts):
	rect = np.zeros((4, 2), dtype = "float32")

	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	return rect

def four_point_transform(image, pts):
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))

	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))

	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	return warped

def find_roi(image):
	ratio = image.shape[0] / 500.0
	orig = image.copy()
	image = imutils.resize(image, height = 500)

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 75, 200)

	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

	for c in cnts:
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		if len(approx) == 4:
			screenCnt = approx
			break
	contour_img = cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)

	warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
	warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
	T = threshold_local(warped, 11, offset = 10, method = "gaussian")
	warped = (warped > T).astype("uint8") * 255
	warped = cv2.resize(warped, (827, 578))
	return warped

def roi_img_predict(img):
	orig_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	#smooth image
	img = cv2.GaussianBlur(img, (5, 5), 0)
	#find threshold
	ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	#find contours and draw contours
	ctrs, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	rects = [cv2.boundingRect(ctr) for ctr in ctrs]

	for rect in rects:
		x, y, w, h = rect
		if  h > 50 and h < 150  or w > 10 and w < 90:
			#draw rectangel on image
			cv2.rectangle(orig_img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
			leng = int(rect[3] * 1.6)
			pt1 = abs(int(rect[1] + rect[3] // 2 - leng // 2))
			pt2 = abs(int(rect[0] + rect[2] // 2 - leng // 2))
			roi = img[pt1:pt1+leng, pt2:pt2+leng]
			roi = cv2.resize(roi,(28, 28), interpolation=cv2.INTER_AREA)
			#resize image
			roi = roi.reshape(-1,28, 28, 1)
			roi = np.array(roi, dtype="float32")
			roi /= 255
			pred_array = filchy_model.predict(roi)
			pred_array = np.argmax(pred_array)
			cv2.putText(orig_img, str(pred_array), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 3)
			cv2.imwrite("dependencies/images/predict3.jpg", orig_img)
