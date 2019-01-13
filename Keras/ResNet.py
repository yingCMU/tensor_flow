from keras.applications.resnet50 import ResNet50
# Again, you'll need to do ImageNet-related pre-processing if you want to use
# the pre-trained weights for it. ResNet50 has a 224x224 input size.
model = ResNet50(weights='imagenet', include_top=False)
