import os
import csv
from scipy import ndimage
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, Cropping2D

samples = []
data_folder = "/opt/carnd_p3/data/"
image_folder = data_folder + "IMG/"
INPUT_SHAPE = (160, 320, 3)

print("training folder:", data_folder)
with open(data_folder + "driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        samples.append(line)

from sklearn.model_selection import train_test_split

train_samples, validation_samples = train_test_split(samples, test_size=0.2)

import numpy as np
import sklearn

FLG_USE_LR = False


def generator(samples, batch_size=128):
    num_samples = len(samples)
    while 1:  # Loop forever so the generator never terminates
        sklearn.utils.shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset : offset + batch_size]

            images = []
            angles = []
            for batch_sample in batch_samples:
                center_file_name = batch_sample[0].split("/")[-1]
                if center_file_name == "center":
                    continue
                center_img_path = image_folder + center_file_name
                center_image = ndimage.imread(center_img_path)
                center_angle = float(batch_sample[3])
                images.append(center_image)
                angles.append(center_angle)
                if FLG_USE_LR:
                    left_img_path = image_folder + batch_sample[1].split("/")[-1]
                    right_img_path = image_folder + batch_sample[2].split("/")[-1]
                    left_img = ndimage.imread(left_img_path)
                    right_img = ndimage.imread(right_img_path)
                    images.append(left_img)
                    angles.append(center_angle + 0.2)
                    images.append(right_img)
                    angles.append(center_angle - 0.2)

            # trim image to only see section with road
            X_train = np.array(images)
            y_train = np.array(angles)
            yield sklearn.utils.shuffle(X_train, y_train)


# compile and train the model using the generator function
train_generator = generator(train_samples, batch_size=128)
validation_generator = generator(validation_samples, batch_size=128)


model = Sequential()
# Preprocess incoming data, centered around zero with small standard deviation
model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=INPUT_SHAPE))
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

model.compile(loss="mse", optimizer="adam")
# model.fit_generator(train_generator, samples_per_epoch=len(train_samples), validation_data=validation_generator,nb_val_samples=len(validation_samples), nb_epoch=3)
model.fit_generator(
    train_generator,
    steps_per_epoch=len(train_samples),
    validation_data=validation_generator,
    validation_steps=len(validation_samples),
    epochs=5,
    verbose=1,
)
"""
If the above code throw exceptions, try
model.fit_generator(train_generator, steps_per_epoch= len(train_samples),
validation_data=validation_generator, validation_steps=len(validation_samples), epochs=5, verbose = 1)
"""
