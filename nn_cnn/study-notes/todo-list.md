1. L12 - [TensorFlow final lab](https://classroom.udacity.com/nanodegrees/nd013/parts/edf28735-efc1-4b99-8fbb-ba9c432239c8/modules/6b6c37bc-13a5-47c7-88ed-eb1fce9789a0/lessons/f035a45d-6203-4947-8175-6095862204d3/concepts/cbcb68d7-7575-442c-82d4-f796ad82b00a)
2. L13 - [dropout](https://classroom.udacity.com/nanodegrees/nd013/parts/edf28735-efc1-4b99-8fbb-ba9c432239c8/modules/6b6c37bc-13a5-47c7-88ed-eb1fce9789a0/lessons/c547d47e-bc84-434a-a72f-fd654be582f9/concepts/3cb3c513-935a-48c2-8ca7-195d4084c5da)
3. Watch CNN [video](https://classroom.udacity.com/nanodegrees/nd013/parts/edf28735-efc1-4b99-8fbb-ba9c432239c8/modules/6b6c37bc-13a5-47c7-88ed-eb1fce9789a0/lessons/0fb1d383-484e-4c49-a0e4-03922c1416d6/concepts/64063017560923) again
5. Adapt Lenet for traffic sign
2. how to improve training accuracy
* How was the architecture adjusted and why was it adjusted? Typical adjustments could include choosing a different model architecture, adding or taking away layers (pooling, dropout, convolution, etc), using an activation function or changing the activation function. One common justification for adjusting an architecture would be due to overfitting or underfitting. A high accuracy on the training set but low accuracy on the validation set indicates over fitting; a low accuracy on both sets indicates under fitting.
      grey scale?
    Neural network architecture (is the network over or underfitting?)
    WITH 15 EPOCHS
    train accuracy = 0.922, test accuracy = 0.908, so it is overfitting, how to prevent overfitting??
    grayscale: train = 0.817, test = 0.9
    Play around preprocessing techniques (normalization, rgb to grayscale, etc)
    Number of examples per label (some have more than others).
    Generate fake data.

    With the LeNet-5 solution from the lecture, you should expect a validation set accuracy of about 0.89
    -- cuz normalization has overflow
    dropout really increased accuracy from .92 to .959, why??
    increase eppoch, decrease learning rate: make it increase from 0.9 -> 0.92
    gray: EPOCH 30 ...Validation Accuracy = 0.959
    color: EPOCH 30 ...Validation Accuracy = 0.955
