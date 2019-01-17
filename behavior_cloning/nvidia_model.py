import csv
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, Cropping2D
from scipy import ndimage, misc
import matplotlib.pyplot as plt

FLG_USE_LR = False
batch_size = 128
input_shape = (160, 320, 3)
count = 0

images = []
measures = []
data_folder = "/opt/carnd_p3/data/"
image_folder = data_folder + "IMG/"
print("training folder:", data_folder)
with open(data_folder + "driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        # skip header line
        if count is 0:
            count = count + 1
            continue
        source_path = line[0]
        file_name = source_path.split("/")[-1]
        current_img_path = image_folder + file_name
        image = ndimage.imread(current_img_path)
        misc.imsave('./original.png', image)
        m = float(line[3])
        if FLG_USE_LR:
            left_img_path = image_folder + line[1].split("/")[-1]
            right_img_path = image_folder + line[2].split("/")[-1]
            left_img = ndimage.imread(left_img_path)
            right_img = ndimage.imread(right_img_path)
            images.append(left_img)
            measures.append(m + 0.2)
            images.append(right_img)
            measures.append(m - 0.2)
        images.append(image)
        measures.append(m)
        image_flipped = np.fliplr(image)
        misc.imsave('./flipped.png', image_flipped)
        break
        images.append(image_flipped)
        measurement_flipped = -m
        measures.append(measurement_flipped)
y_train = np.array(measures)
X_train = np.array(images)
start_train = True
print_history = False

print(X_train.shape)
print(X_train[0].shape)
print(y_train.shape)
if start_train:
    model = Sequential()
    # preprocessing
    model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=(160, 320, 3)))
    model.add(Cropping2D(cropping=((70, 25), (0, 0))))
    #     ===== architecture =====
    model.add(Conv2D(24, kernel_size=(5, 5), activation="elu", strides=(2, 2)))
    model.add(Conv2D(36, kernel_size=(5, 5), activation="elu", strides=(2, 2)))
    model.add(Conv2D(48, kernel_size=(5, 5), activation="elu", strides=(2, 2)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation="elu"))
    model.add(Conv2D(64, kernel_size=(3, 3), activation="elu"))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(100, activation="elu"))
    model.add(Dense(50, activation="elu"))
    model.add(Dense(10, activation="elu"))
    model.add(Dense(1))
    # 2nd Layer - Add a fully connected layer
    # takes in the output of the first layer and sets the output dimensions to (100)
    #  ===== architecture end =====
    model.compile(loss="mse", optimizer="adam")
    history_object = model.fit(
        x=X_train,
        y=y_train,
        batch_size=batch_size,
        validation_split=0.2,
        shuffle=True,
        epochs=7,
        verbose=1,
    )
    model.save("model_without_lr.h5")
    if print_history:
        ### print the keys contained in the history object
        print(history_object.history.keys())

        ### plot the training and validation loss for each epoch
        plt.plot(history_object.history["loss"])
        plt.plot(history_object.history["val_loss"])
        plt.title("model mean squared error loss")
        plt.ylabel("mean squared error loss")
        plt.xlabel("epoch")
        plt.legend(["training set", "validation set"], loc="upper right")
        plt.show()
