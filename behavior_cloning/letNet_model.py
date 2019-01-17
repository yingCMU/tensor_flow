import csv
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, Cropping2D
from scipy import ndimage
import matplotlib.pyplot as plt


images = []
measures = []
data_folder = '/opt/carnd_p3/data/'#'../train_data/4/'
image_folder = data_folder + 'IMG/'
print('training folder:', data_folder)
count = 0
with open(data_folder+'driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if count is 0:
            count = count +1
            continue
        source_path = line[0]
        file_name = source_path.split('/')[-1]
#         image = cv2.imread(source_path)
        current_img_path = image_folder + file_name
        image = ndimage.imread(current_img_path)
#         print(image.shape)
        images.append(image)
        m = float(line[3])
        measures.append(m)
        image_flipped = np.fliplr(image)
        images.append(image_flipped)
        measurement_flipped = -m
        measures.append(measurement_flipped)

#         print('source_path',source_path)
#         print('file_name',image)
y_train = np.array(measures)
X_train = np.array(images)
start_train = True
print_history = False

batch_size = 128
print(X_train.shape)
print(X_train[0].shape)
print(y_train.shape)
input_shape=(160, 320, 3)
if start_train:
    model = Sequential()
    # preprocessing
    model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=(160,320,3)))
    model.add(Cropping2D(cropping=((70,25),(0,0))))
#     ===== architecture =====
#     model.add(Flatten(input_shape=(160, 320, 3)))
    model.add(Conv2D(6, kernel_size=(5, 5),activation='relu',input_shape=input_shape))
#     model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Dropout(0.25)) # dropp 25%
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(6, kernel_size=(5, 5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)) )
    #flattern: multi dimension to one dimension
    model.add(Flatten())
#     fully connected layer, etc
#     model.add(Dropout(0.25)) # dropp 50%

    model.add(Dense(120))
    model.add(Dense(84))
    model.add(Dense(1))
    #2nd Layer - Add a fully connected layer
    #takes in the output of the first layer and sets the output dimensions to (100)

#  ===== architecture end =====
    model.compile(loss = 'mse', optimizer = 'adam')
    history_object = model.fit(x=X_train, y=y_train, batch_size=batch_size,validation_split= 0.2, shuffle = True, epochs = 7, verbose = 1)
    model.save('model.h5')
    if print_history:
        ### print the keys contained in the history object
        print(history_object.history.keys())

        ### plot the training and validation loss for each epoch
        plt.plot(history_object.history['loss'])
        plt.plot(history_object.history['val_loss'])
        plt.title('model mean squared error loss')
        plt.ylabel('mean squared error loss')
        plt.xlabel('epoch')
        plt.legend(['training set', 'validation set'], loc='upper right')
        plt.show()
