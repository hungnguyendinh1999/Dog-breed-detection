from keras.layers import  GlobalAveragePooling2D, Dense
from keras.models import Sequential


def init(): 
	#load weights into new model
	model = Sequential()
	model.add(GlobalAveragePooling2D(input_shape=(1,1,2048)))
	model.add(Dense(133, activation='softmax'))

	model.load_weights("model/weights.best.Resnet50.hdf5")
	print("Loaded Model from disk")
	

	return model