from keras.applications.inception_v3 import InceptionV3

model = InceptionV3(weights='imagenet', include_top=False)
# Don't forget to perform the necessary pre-processing steps to any inputs you
# include! While the original Inception model used a 224x224 input like VGG,
# InceptionV3 actually uses a 299x299 input.
