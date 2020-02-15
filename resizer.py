import cv2


def resize(name):
	img = cv2.imread(name)
	img = cv2.resize(img, (321, 214))
	cv2.imwrite(name, img)
	print("Complete")


resize("kaggel_accuracy.png")
resize("kaggle_loss.png")