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
## lane folowing
