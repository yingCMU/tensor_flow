[kf-gaussian]: ./images/kf-gaussian.png "more certainty"
[kf-math]: ./images/kf-math.png "math behind"
[eg1]: ./images/eg2.png "example 1"
[eg2]: ./images/eg2.png "example 2"
[eg3]: ./images/eg3.png "example 3"
[multi]: ./images/multi.png "multi"
[vp]: ./images/velocity-position.png "velocity-position"
[kf-map]: ./images/kf-map.png "kf-map"
[kf-cycle]: ./images/kf-cycle.png "kf-cycle"
[kf-cycle-variables]: ./images/kf-cycle-variables.png "kf-cycle-variables"



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
![alt text][kf-map]
Imagine you are in a car equipped with sensors on the outside. The car sensors can detect objects moving around: for example, the sensors might detect a pedestrian, as described in the video, or even a bicycle. For variety, let's step through the Kalman Filter algorithm using the bicycle example.

The Kalman Filter algorithm will go through the following steps:

first measurement - the filter will receive initial measurements of the bicycle's position relative to the car. These measurements will come from a radar or lidar sensor.
initialize state and covariance matrices - the filter will initialize the bicycle's position based on the first measurement.
then the car will receive another sensor measurement after a time period \Delta{t}Δt.
predict - the algorithm will predict where the bicycle will be after time \Delta{t}Δt. One basic way to predict the bicycle location after \Delta{t}Δt is to assume the bicycle's velocity is constant; thus the bicycle will have moved velocity * \Delta{t}Δt. In the extended Kalman filter lesson, we will assume the velocity is constant.
update - the filter compares the "predicted" location with what the sensor measurement says. The predicted location and the measured location are combined to give an updated location. The Kalman filter will put more weight on either the predicted location or the measured location depending on the uncertainty of each value.
then the car will receive another sensor measurement after a time period \Delta{t}Δt. The algorithm then does another predict and update step.
6. Measurement - Update
![alt text][kf-cycle]
![alt text][kf-cycle-variables]

7. variables
state transition matrix: F
process covariance matrix: Q
Measurement Noise Covariance Matrix: R
z is the measurement vector. For a lidar sensor, the z vector contains the position-x and position−y measurements.
H is the matrix that projects your belief about the object's current state into the measurement space of the sensor. For lidar, this is a fancy way of saying that we discard velocity information from the state variable since the lidar sensor only measures position: The state vector xx contains information about [p_x, p_y, v_x, v_y], whereas the zz vector will only contain [px, py]. Multiplying Hx allows us to compare x, our belief, with z, the sensor measurement.
What does the prime notation in the xx vector represent? The prime notation like p_x' means you have already done the prediction step but have not done the measurement step yet. In other words, the object was at p_x. After time Δt, you calculate where you believe the object will be based on the motion model and get p_x'
--
Motion noise and process noise refer to the same case: uncertainty in the object's position when predicting location. The model assumes velocity is constant between time intervals, but in reality we know that an object's velocity can change due to acceleration. The model includes this uncertainty via the process noise.
the process noise depends on both: the elapsed time and the uncertainty of acceleration. So, how can we model the process noise by considering both of these factors?

8. radar measurements
Radar measurements require a non-linear function:
 applying a nonlinear function to a Gaussian distribution removes its "Gaussian-ness." (I just made up that word. "Gaussianality?" "Gaussianism?")
 So a linear proximation is using taylor seriese expansion


9. Extended Kalman Filter Equations
Although the mathematical proof is somewhat complex, it turns out that the Kalman filter equations and extended Kalman filter equations are very similar. The main differences are:
to calculate x', the prediction update function, ff, is used instead of the FF matrix.
to calculate y', the hh function is used instead of the HH matrix.

For this project, however, we do not need to use the ff function or F_jF
j
​	 . If we had been using a non-linear model in the prediction step, we would need to replace the FF matrix with its Jacobian, F_jF
j
​	 . However, we are using a linear model for the prediction step. So, for the prediction step, we can still use the regular Kalman filter equations and the FF matrix rather than the extended Kalman filter equations.

The measurement update for lidar will also use the regular Kalman filter equations, since lidar uses linear equations. Only the measurement update for the radar sensor will use the extended Kalman filter equations.

10. Compared to Kalman Filters, how would the Extended Kalman Filter result differ when the prediction function and measurement function are both linear??
Answer: Compared to Kalman Filters, how would the Extended Kalman Filter result differ when the prediction function and measurement function are both linear?
If f and h are linear functions, then the Extended Kalman Filter generates exactly the same result as the standard Kalman Filter. Actually, if f and h are linear then the Extended Kalman Filter F_j turns into f and H_j turns into h. All that's left is the same ol' standard Kalman Filter!

In our case we have a linear motion model, but a nonlinear measurement model when we use radar observations. So, we have to compute the Jacobian only for the measurement function.
