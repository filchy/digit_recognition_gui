import pandas as pd
import numpy as np
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split


def load():
	train = pd.read_csv("dependencies/train.csv")

	X_train = train.iloc[:, 1:].values
	y_train = train.iloc[:, 0].values
	sns_y_train = y_train

	X_train = X_train.astype("float32")/255
	y_train = to_categorical(y_train, num_classes=10)

	X_train = np.array(X_train).reshape(-1, 28, 28 ,1)

	X_train1, X_test1, y_train1, y_test1 = train_test_split(X_train, y_train, test_size = 0.15)

	return X_train1, X_test1, y_train1, y_test1
