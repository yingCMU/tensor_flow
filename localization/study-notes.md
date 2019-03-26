# inexact motion
U = 2
p = [0,1,0,0,0] => [0, 0, 0.1, 0.8, 0.1]
p = [0, 0.5, 0, 0.5, 0] => [0.4, 0.05, 0.05, 0.4, 0.1]
p = [0.2, 0.2, 0.2, 0.2, 0.2 ] => [0.2, 0.2, 0.2, 0.2, 0.2 ]

# limit distribution
As the robot continues to get more and more uncertain about where it is, eventually it will reach the state of maximal uncertainty: the uniform distribution.

# sense and move
with initial belief, car does sense and move  cycle
every move lose information because motion is inaccurate
every sense gains information
entropy is measurement of information: expected log likelihood
 entropy will decrease after the measurement update (sense) step and that entropy will increase after the movement step (move).
 In general, entropy represents the amount of uncertainty in a system. Since the measurement update step decreases uncertainty, entropy will decrease. The movement step increases uncertainty, so entropy will increase after this step.
# Markov Localization
Markov Localization or Bayes Filter for Localization is a generalized filter for localization and all other localization approaches are realizations of this approach, as we'll discuss later on. By learning how to derive and implement (coding exercises) this filter we develop intuition and methods that will help us solve any vehicle localization task, including implementation of a particle filter. We don't know exactly where our vehicle is at any given time, but can approximate it's location. As such, we generally think of our vehicle location as a probability distribution, each time we move, our distribution becomes more diffuse (wider). We pass our variables (map data, observation data, and control data) into the filter to concentrate (narrow) this distribution, at each time step. Each state prior to applying the filter represents our prior and the narrowed distribution represents our Bayes' posterior.

# Localization
Localization is about estimating the probability distribution of X_t given all observations, all previous control and map
Formal Definition of Variables
z_{1:t}
​	  represents the observation vector from time 0 to t (range measurements, bearing, images, etc.).

u_{1:t}
​	  represents the control vector from time 0 to t (yaw/pitch/roll rates and velocities).

mrepresents the map (grid maps, feature maps, landmarks)

x_t
​	  represents the pose (position (x,y) + orientation \thetaθ)
# Bayes' Rule
In other words the probability of state a, given evidence b, is the probability of evidence b, given state a, multiplied by the probability of state a, normalized by the total probability of b over all states.

With respect to localization, these terms are:

P(location|observation)P(location∣observation): This is P(a|b), the normalized probability of a position given an observation (posterior).
P(observation|location)P(observation∣location): This is P(b|a), the probability of an observation given a position (likelihood)
P(location)P(location): This is P(a), the prior probability of a position
P(observation) P(observation): This is P(b), the total probability of an observation


be aware that P(location) is determined by the motion model. The probability returned by the motion model is the product of the transition model probability (the probability of moving from x_{t-1} -> x_t and the probability of the state x_{t-1}
​
# initialize belief state
We have landmarks at x = 5.0, 10.0, and 20.0 meters, with position standard deviation of 1.0 meter. If we know that our car's initial position is at one of these three landmarks, how should we define our initial belief state?

Since we know that we are parked next to a landmark, we can set our probability of being next to a landmark as 1.0. Accounting for a position precision of +/- 1.0 meters, this places our car at an initial position in the range [4, 6] (5 +/- 1), [9, 11] (10 +/- 1), or [19, 21] (20 +/- 1). All other positions, not within 1.0 meter of a landmark, are initialized to 0. We normalize these values to a total probability of 1.0 by dividing by the total number of positions that are potentially occupied. In this case, that is 9 positions, 3 for each landmark (the landmark position and one position on either side). This gives us a value of 1.11E-01 for positions +/- 1 from our landmarks (1.0/9)

# Markov Derivation
There are lots of ppast data to bbe stored and claculated. We have to find a way that:
1. makes data stay constant, instead of increasing over time
2. per update, process little data

bel(Xt-1) => bel(Xt)
Rules applied is:
Bayes' rule
law of total probability
The 'Markov Assumption'
## Markov Assumption
A Markov process is one in which the conditional probability distribution of future states (ie the next state) is dependent only upon the current state and not on other preceding states. This can be expressed mathematically as:

P(x_t|x_{t-1},....,x_{t-i},...., x_0) = P(x_t|x_{t-1})
It is important to note that the current state may contain all information from preceding states.

we replace the integral by a sum over all x_i because we have a discrete localization scenario in this case, to get the same formula in Sebastian's lesson for localization. The process of predicting x_t with a previous beliefs (x_{t-1}) and the transition model is technically a convolution. If you take a look to the formula again, it is essential that the belief at x_t = 0 is initialized with a meaningful assumption. It depends on the localization scenario how you set the belief or in other words, how you initialize your filter. For example, you can use GPS to get a coarse estimate of your location.

## motion model probabilities

How is the summation doing that? It's looking at each prior location where the vehicle could have been, x_{t-1}.Then the summation iterates over every possible prior location, x_{t-1}^{(1)}...x_{t-1}^{(n)}.For each possible prior location in that list, x_{t-1}^{(i)}x
t−1
(i)
​	 , the summation yields the total probability that the vehicle really did start at that prior location and that it wound up at x_t.\
# observation model.
The Markov assumption can help us simplify the observation model. Recall that the Markov Assumption is that the next state is dependent only upon the preceding states and that preceding state information has already been used in our state estimation. As such, we can ignore terms in our observation model prior to x_t x
t
​	  since these values have already been accounted for in our current state and assume that t is independent of previous observations and controls.

Since z_t z
t
​	  can be a vector of multiple observations we rewrite our observation model to account for the observation models for each single range measurement. We assume that the noise behavior of the individual range values z_t^1 z
t
1
​	  to z_t^k z
t
k
​	  is independent and that our observations are independent, allowing us to represent the observation model as a product over the individual probability distributions of each single range measurement. Now we must determine how to define the observation model for a single range measurement.

In general there exists a variety of observation models due to different sensor, sensor specific noise behavior and performance, and map types. For our 1D example we assume that our sensor measures to the n closest objects in the driving direction, which represent the landmarks on our map. We also assume that observation noise can be modeled as a Gaussian with a standard deviation of 1 meter and that our sensor can measure in a range of 0 – 100 meters.

To implement the observation model we use the given state x_t x
t
​	 , and the given map to estimate pseudo ranges, which represent the true range values under the assumption that your car would stand at a specific position x_t x
t
​	 , on the map. For example, if our car is standing at position 20 it would make use x_t x
t
​	 , and m to make pseudo range ( z_t^* z
t
∗
​	 ) observations in the order of the first landmark to the last landmark or 5, 11, 39, and 57 meters. Compared to our real observations ( z_t z
t
​	  = [19, 37]) the position x_t x
t
​	 , = 20 seems unlikely and our observation would rather fit to a position around 40.

Based on this example the observation model for a single range measurement is defined by the probability of the following normal distribution (3.31 Markov Assumption for Observation Model)
# general Bayes Localization Filter (Markov Localization) lec 3.32
Starting with the generalized form of Bayes Rule we expressed our posterior, the belief of x at t as \etaη (normalizer) multiplied with the observation model and the motion model.
We simplified the observation model using the Markov assumption to determine the probability of z at time t, given only x at time t, and the map.
We expressed the motion model as a recursive state estimator using the Markov assumption and the law of total probability, resulting in a model that includes our belief at t – 1 and our transition model.
Finally we derived the general Bayes Filter for Localization (Markov Localization) by expressing our belief of x at t as a simplified version of our original posterior expression (top equation), \etaη multiplied by the simplified observation model and the motion model. Here the motion model is written bel^ a prediction model.
The Bayes Localization Filter dependencies can be represented as a graph, by combining our sub-graphs. To estimate the new state x at t we only need to consider the previous belief state, the current observations and controls, and the map.

 Bayes filter is a general framework for recursive state estimation!
 Recursive means:
  1. using previous state to estimate new state
  2. That means this framework allows us to use the previous state (state at t-1) to estimate a new state (state at t) using only current observations and controls (observations and control at t), rather than the entire data history (data from 0:t).
  3. The motion model describes the prediction step of the filter while the observation model is the update step.
  4. The state estimation using the Bayes filter is dependent upon the interaction between prediction (motion model) and update (observation model steps) and all the localization methods discussed so far are realizations of the Bayes filter.


# particle filter implementation
 our ultimate goal is to find a weight parameter for each particle that represents how well that particle fits to being in the same location as the actual car.
lec 6.3
## prediction step:
use motion model to predict where the care will be at next time step
by updating based on yaw rate and velocity, while accounting for Gaussian sensor noise(sensor uncertainty).
## update step:
use landmark measurement to update our belief of our position
need to solve data association first: math landmark measurement to object in the real world(map landmarks): here simply use nearest neighbor (map landmark vs (multiple)lidar measurements, pick the nearest lidar measurment to the map landmark). But this simple solution has many disadvantages(lec 6.10, 6.11)
1. We will first need to transform the car's measurements from its local car coordinate system to the map's coordinate system(with respect to our particle , which is estimated position of the car).
2. Next, each measurement will need to be associated with a landmark identifier, for this part we will take the closest landmark to each transformed observation.
3. Finally, we will use this information to calculate the weight value of the particle. Calculating the Particle's Final Weight  as the product of each measurement's Multivariate-Gaussian probability density. it is multi variate because there are multi dimentions (2D) in the postion measurement.
To get the final weight just multiply all the calculated measurement probabilities together.
