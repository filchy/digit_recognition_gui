from tensorflow.keras import Input
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Dropout, Flatten, Dense, ZeroPadding2D, Activation, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ReduceLROnPlateau

from load_data import load


def _layer(model, output, count, strides):
	model = _layers_block(model, output, True, strides)

	for _ in range(1, count):
		model = _layers_block(model, output, False, strides)

	return model

def _layers_block(model, output, downsampling, strides):
	main_channel = output // 4

	model.add(BatchNormalization())
	model.add(Conv2D(main_channel, kernel_size=1, padding="same", strides=strides, kernel_initializer="he_normal", activation="relu"))
	# Conv 3x3
	model.add(BatchNormalization())
	model.add(Conv2D(main_channel, kernel_size=3, padding="same", strides=strides, kernel_initializer="he_normal", activation="relu"))
	# Conv 1x1
	model.add(BatchNormalization())
	model.add(Conv2D(main_channel, kernel_size=1, padding="same", strides=strides, kernel_initializer="he_normal", activation="relu"))

	if downsampling:
		model.add(Conv2D(main_channel, kernel_size=1, padding="same", strides=strides, kernel_initializer="he_normal"))

	return model


X_train1, X_test1, y_train1, y_test1 = load()

model = Sequential()
model.add(Input(shape=(28,28,1)))
model.add(ZeroPadding2D(padding=(2,2)))

model.add(Conv2D(16, kernel_size=3, padding="same"))

model = _layer(model, 64, 18, (1,1))
model = _layer(model, 128, 18, (1,1))
model = _layer(model, 256, 18, (1,1))

model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(GlobalAveragePooling2D())
model.add(Dense(10, activation="softmax"))

datagen = ImageDataGenerator(
            rotation_range=12,
            zoom_range=0.25,
            width_shift_range=0.25,
            height_shift_range=0.25,
            data_format="channels_last",
            shear_range=15)

datagen.fit(X_train1)

opt = SGD(lr=0.1, momentum=0.9, decay=1e-04)

reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, 
                                       patience=10, verbose=1)


model.fit_generator(datagen.flow(X_train1, y_train1, batch_size=32), steps_per_epoch=X_train1.shape[0]//32, 
                           epochs=70, validation_data=(X_test1, y_test1), callbacks=[reduce_lr])

model.save("resnet164.h5")
