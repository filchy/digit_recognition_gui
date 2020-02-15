import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model, Model

filchy_model = load_model("./dependencies/models/filchy.h5")
vgg16_model = load_model("./dependencies/models/vgg16.h5")
mobilenet_model = load_model("./dependencies/models/mobilenet.h5")

def img_preprocces():
	img = cv2.imread("dependencies/images/predict.png")
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

		# for conv visualization
		layer_outputs = [layer.output for layer in filchy_model.layers]
		activation_model = Model(inputs=filchy_model.input, outputs=layer_outputs)
		activations = activation_model.predict(img)

		return final_num, activations

	elif model == "vgg16":
		nums = vgg16_model.predict(img)
		num = np.argmax(nums, axis=1)
		final_num = str(num)
		final_num = final_num[1]

		# for conv visualization
		layer_outputs = [layer.output for layer in vgg16_model.layers]
		activation_model = Model(inputs=vgg16_model.input, outputs=layer_outputs)
		activations = activation_model.predict(img)

		return final_num, activations

	elif model == "mobilenet":
		nums = mobilenet_model.predict(img)
		num = np.argmax(nums, axis=1)
		final_num = str(num)
		final_num = final_num[1]

		# for conv visualization
		layer_outputs = [layer.output for layer in mobilenet_model.layers]
		activation_model = Model(inputs=mobilenet_model.input, outputs=layer_outputs)
		activations = activation_model.predict(img)
		
		return final_num, activations

def multi_img_predict():
	image = cv2.imread("dependencies/images/multipredict.png")

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
			roi = cv2.resize(roi,(28, 28), interpolation=cv2.INTER_AREA)
			#resize image
			roi = roi.reshape(-1,28, 28, 1)
			roi = np.array(roi, dtype="float32")
			roi /= 255
			pred_array = filchy_model.predict(roi)
			pred_array = np.argmax(pred_array)
			cv2.putText(image, str(pred_array), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 3)
			cv2.imwrite("dependencies/images/multipredict.png", image)
