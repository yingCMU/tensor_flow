# search
Find the least steps to reach goal from start state, given a map with obstacles and cost of move action
## what is cost?
This is depending on the definition of the cost model of each action
every move
every turn
turn left and move forward
punish left turns:

## solutions
A start: for optimal search
Dynamic programming: for policy which tells you what action to take at each location in the map

##todo:
1. 8.11, search program
2. 8.12, expand program
3. 8.13, path program
4. 8.15 A start program
5. 8.20 value program
5. 8.21 optimum policy program
7. 8.22 left turn policy program

# prediction
## papers:
[Trajectory Clustering for Motion Prediction](http://video.udacity-data.com.s3.amazonaws.com/topher/2017/July/5978c2c6_trajectory-clustering/trajectory-clustering.pdf)
## Inputs and Outputs to Prediction
A prediction module uses a map and data from sensor fusion to generate predictions for what all other dynamic objects in view are likely to do. To make this clearer, let's look at an example (in json format) of what the input to and output from prediction might look like.
### Notes
The predicted trajectories shown here only extend out a few seconds. In reality the predictions we make extend to a horizon of 10-20 seconds.
The trajectories shown have 0.5 second resolution. In reality we would generate slightly finer-grained predictions.
This example only shows vehicles but in reality we would also generate predictions for all dynamic objects in view.
## approach
1. model based: emcompass our knowledge of physics, road structure, traffic,traffic laws
to generate a possibility of multiple scenarios

2. data driven:a blackbox tell u what is happening next. ML, use lots of data. Use data to extract solid patterns that would otherwise be missed by model based approach
which is best? Neither approach (model based or data driven) is strictly better than the other but there are certain situations in which one is more useful than the other.
examples:
1. Determining maximum safe turning speed on a wet road.
In this situation we could use a model based approach to incorporate our knowledge of physics (friction, forces, etc...) to figure out exactly (or almost exactly) when a vehicle would begin to skid on a wet road.
You certainly could use a data-driven approach, but that wouldn't really be harnessing the strengths of data and would neglect to use our very strong understanding of the relevant physics involved.
2. Predicting the behavior of an unidentified object sitting on the road.
That's right. Even with data driven approaches this would still be a very hard problem but since we don't even know what this object is, a model based approach to prediction would be nearly impossible.
3. Predicting the behavior of a vehicle on a two lane highway in light traffic.
You could really use either approach (or a hybrid approach) in this situation.
On the one hand there are very few behaviors we need to model in a highway driving situation and the physics are all very well understood so model based approaches could work.
On the other hand it would be relatively easy to collect a lot of training data in similar situations so a purely data driven approach could work too.

# Trajectory clustering
## training (offline)
1. get lots of trajectories data
2. clean data
3. define measure of similarity
4. perform unsupervised clustering
5. define prototype trajectories for each cluster
## online prediction
every update cycle...
1. observe vehicle's partial trajectory
2. compare to prototype trajectories(using same similarity)
3. predict a trajectory (probability distribution)

# model based approach
for each dynamic object nearby
1. identify common driving behaviors(change lane, turn left, cross street, etc)
2. define process model for each ^
3. update beliefs by comparing the observation with the output of the process model
4. trajectory generation

## Frenet Coordinates
representing position on a road in a more intuitive way than traditional (x,y)(x,y) Cartesian Coordinates
## Process Models
define what is lane following
[A comparative study of multiple-model algorithms for maneuvering target
tracking](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5953fc34_a-comparative-study-of-multiple-model-algorithms-for-maneuvering-target-tracking/a-comparative-study-of-multiple-model-algorithms-for-maneuvering-target-tracking.pdf)
## hybrid approach
combine process model with ML classifier
### Naive Bayes
Naive: assume feature variables contribute independently but in reality there are usually correlation
### Gussian Naive Bayes
assume individual probabilities have gaussian distribution: P(h|male) ~ N(mu_male_height,var_male_height)
So the problem is:
1. select relevant features (that can distinguishing between these two behaviors.)
2. identify the means/variance for different classes
  a. can be guessed or
  b. learned from lots of data

#Helpful Resources
  [sklearn documentation on GaussianNB](https://scikit-learn.org/stable/modules/naive_bayes.html#gaussian-naive-bayes)
  [Wikipedia article on Naive Bayes / GNB](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Gaussian_naive_Bayes)


# Behavior planning
where to go next?
## Understanding Output
It's possible to suggest a wide variety of behaviors by specifying only a few quantities. For example by specifying only a target lane, a target vehicle (to follow), a target speed, and a time to reach these targets, we can make suggestions as nuanced as "stay in your lane but get behind that vehicle in the right lane so that you can pass it when the gap gets big enough."
responsible for suggest states/maneuvers that are:
- legal
- feasible
- safe
- efficient
not responsible for:
- execution details
- collision avoidance
## Finite state machines
There isn't one definitively correct answer.
The states choosen can impact the behavior of the vehicle.
- choose what states
- determine inputs of state transition
## approaches
One way to implement a transition function is by generating rough trajectories for each accessible "next state" and then finding the best. To "find the best" we generally use cost functions. We can then figure out how costly each rough trajectory is and then select the state with the lowest cost trajectory.
### cost functions
- speed cost(efficiency)
  The goal with this quiz is to create a cost function that would make the vehicle drive in the fastest possible lane, given several behavior options
- Lane change penalty: So we want a cost function that penalizes large |\Delta d|∣Δd∣ and we want that penalty to be bigger when \Delta sΔs is small. Furthermore, we want to make sure that the maximum cost of this cost function never exceeds one and that the minimum never goes below zero.
In this example, we found that the ratio \LARGE \frac{|\Delta d|}{\Delta s}
Δs
∣Δd∣
​	  was important. If we call that ratio xx we can then use that ratio in any function with bounded range. These functions tend to be useful when designing cost functions. These types of functions are called Sigmoid Functions.
#### cost function designing
difficulties:
- solving new problems without unsolving old ones: use regression testing
- balancing cost of drastically different magnitude: e.g safety overshadow efficiency
  (physical) feasibility > safety > legality > comfort > efficiency
  also weights can change depending on situations: e.g red light more weights than in highway

## schedule computing time
don't let low freq calculation block high freq update

# Hybrid A*
It uses a continuous search space.
It uses an optimistic heuristic function to guide grid cell expansion.
Solutions it finds are drivable
but:
It has a lack of completeness
solution is not always optimal
[Junior: The Stanford Entry in the Urban Challenge ](https://d17h27t6h515a5.cloudfront.net/topher/2017/July/595fe838_junior-the-stanford-entry-in-the-urban-challenge/junior-the-stanford-entry-in-the-urban-challenge.pdf)
* Polynomial Trajectory generation play ground
Lect 11-33
* Polynomial Trajectory generation
[Optimal Trajectory Generation For Dynamic Street Scenarios In A Frenet Frame](http://video.udacity-data.com.s3.amazonaws.com/topher/2017/July/595fd482_werling-optimal-trajectory-generation-for-dynamic-street-scenarios-in-a-frenet-frame/werling-optimal-trajectory-generation-for-dynamic-street-scenarios-in-a-frenet-frame.pdf)
- Cost Functions.
- Differences between high speed and low speed trajectory generation.
- Implementation of specific maneuvers relevant to highway driving like following, merging, and velocity keeping.
- How to combining lateral and longitudinal trajectories.
- A derivation of the transformation from Frenet coordinates to global coordinates (in the appendix).

* additional papers
Indoors
[Intention-Net: Integrating Planning and Deep Learning for Goal-Directed Autonomous Navigation by S. W. Gao, et. al.](https://arxiv.org/abs/1710.05627)

Abstract: How can a delivery robot navigate reliably to a destination in a new office building, with minimal prior information? To tackle this challenge, this paper introduces a two-level hierarchical approach, which integrates model-free deep learning and model-based path planning. At the low level, a neural-network motion controller, called the intention-net, is trained end-to-end to provide robust local navigation. The intention-net maps images from a single monocular camera and "intentions" directly to robot controls. At the high level, a path planner uses a crude map, e.g., a 2-D floor plan, to compute a path from the robot's current location to the goal. The planned path provides intentions to the intention-net. Preliminary experiments suggest that the learned motion controller is robust against perceptual uncertainty and by integrating with a path planner, it generalizes effectively to new environments and goals.

City Navigation
[Learning to Navigate in Cities Without a Map by P. Mirowski, et. al.](https://arxiv.org/abs/1804.00168)

Abstract: Navigating through unstructured environments is a basic capability of intelligent creatures, and thus is of fundamental interest in the study and development of artificial intelligence. Long-range navigation is a complex cognitive task that relies on developing an internal representation of space, grounded by recognizable landmarks and robust visual processing, that can simultaneously support continuous self-localization ("I am here") and a representation of the goal ("I am going there"). Building upon recent research that applies deep reinforcement learning to maze navigation problems, we present an end-to-end deep reinforcement learning approach that can be applied on a city scale. [...] We present an interactive navigation environment that uses Google StreetView for its photographic content and worldwide coverage, and demonstrate that our learning method allows agents to learn to navigate multiple cities and to traverse to target destinations that may be kilometers away. [...]

Intersections
[A Look at Motion Planning for Autonomous Vehicles at an Intersection by S. Krishnan, et. al.](https://arxiv.org/abs/1806.07834)

Abstract: Autonomous Vehicles are currently being tested in a variety of scenarios. As we move towards Autonomous Vehicles, how should intersections look? To answer that question, we break down an intersection management into the different conundrums and scenarios involved in the trajectory planning and current approaches to solve them. Then, a brief analysis of current works in autonomous intersection is conducted. With a critical eye, we try to delve into the discrepancies of existing solutions while presenting some critical and important factors that have been addressed. Furthermore, open issues that have to be addressed are also emphasized. We also try to answer the question of how to benchmark intersection management algorithms by providing some factors that impact autonomous navigation at intersection.

Planning in Traffic with Deep Reinforcement Learning
[DeepTraffic: Crowdsourced Hyperparameter Tuning of Deep Reinforcement Learning Systems for Multi-Agent Dense Traffic Navigation by L. Fridman, J. Terwilliger and B. Jenik](https://arxiv.org/abs/1801.02805)

Abstract: We present a traffic simulation named DeepTraffic where the planning systems for a subset of the vehicles are handled by a neural network as part of a model-free, off-policy reinforcement learning process. The primary goal of DeepTraffic is to make the hands-on study of deep reinforcement learning accessible to thousands of students, educators, and researchers in order to inspire and fuel the exploration and evaluation of deep Q-learning network variants and hyperparameter configurations through large-scale, open competition. This paper investigates the crowd-sourced hyperparameter tuning of the policy network that resulted from the first iteration of the DeepTraffic competition where thousands of participants actively searched through the hyperparameter space.
