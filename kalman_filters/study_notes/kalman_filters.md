[kf-gaussian]: ./images/kf-gaussian.png "more certainty"
[kf-math]: ./images/kf-math.png "math behind"
[eg1]: ./images/eg2.png "example 1"
[eg2]: ./images/eg2.png "example 2"
[eg3]: ./images/eg3.png "example 3"
[multi]: ./images/multi.png "multi"
[vp]: ./images/velocity-position.png "velocity-position"



1. Gaussian distribution
  - high variance means flat curve and means more uncertainty
  - we want more certainty

2. The new belief will be somewhere between the previous belief and the new measurement.
but the new peak will NOT be between the heights of the other two. In fact, it will be higher!
This is because more measurements always gives us more certainty.
![alt text][kf-gaussian]

Notice that the new mean is between the previous two means and the new variance is LESS than either of the previous variances.

![alt text][kf-math]

see examples:
![alt text][eg1]
![alt text][eg2]

If the Gaussian's have the same width (which means same certainty), than their product will be a Gaussian with a mean that is right in the middle.
![alt text][eg2]

3. motion update (math is addition)
new mean is addition of both means
new variance is addition of both variances

4. multi-dimentional Gaussian
two dimentional:
x and y can be correlated
X and y can have different variance
![alt text][multi]
![alt text][vp]

5. Kalman Filter Algorithm Map
Imagine you are in a car equipped with sensors on the outside. The car sensors can detect objects moving around: for example, the sensors might detect a pedestrian, as described in the video, or even a bicycle. For variety, let's step through the Kalman Filter algorithm using the bicycle example.

The Kalman Filter algorithm will go through the following steps:

first measurement - the filter will receive initial measurements of the bicycle's position relative to the car. These measurements will come from a radar or lidar sensor.
initialize state and covariance matrices - the filter will initialize the bicycle's position based on the first measurement.
then the car will receive another sensor measurement after a time period \Delta{t}Δt.
predict - the algorithm will predict where the bicycle will be after time \Delta{t}Δt. One basic way to predict the bicycle location after \Delta{t}Δt is to assume the bicycle's velocity is constant; thus the bicycle will have moved velocity * \Delta{t}Δt. In the extended Kalman filter lesson, we will assume the velocity is constant.
update - the filter compares the "predicted" location with what the sensor measurement says. The predicted location and the measured location are combined to give an updated location. The Kalman filter will put more weight on either the predicted location or the measured location depending on the uncertainty of each value.
then the car will receive another sensor measurement after a time period \Delta{t}Δt. The algorithm then does another predict and update step.
