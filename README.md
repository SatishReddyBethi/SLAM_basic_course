# SLAM basic course
This repo consists of my solutions to the assignments from Prof. [Claus Brenner's](https://scholar.google.com/citations?user=VK5xKS4AAAAJ&hl=en) SLAM course on YouTube. 
More importantly, all the code is modified to run in Python3.
It also has my notes for deeper understanding of the SLAM problem.

[YouTube Course](https://www.youtube.com/watch?v=B2qzYCeT9oQ&list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm)

## Steps for solving a localization problem:
*(This course simulates real-time localization using pre-recorded data)*
1. Build a *motion model* of your robot/device (Convert raw data from sensors into real-world coordinates estimates)
2. Estimate the robot pose at each state using the motion model and create a trajectory in world coordinate frame
3. If known landmarks/features exist in the surrounding, and if the robot has a sensor that can detect those surroundings, estimate the position of those landmarks using the sensor data and the robot's estimated pose at each state.
4. Get a similarity transform between the estimate landmark positions and the actual landmark positions. Then, correct the estimated poses using the similarity transform.\
(Scale can be set to 1 because, the robot is a rigid body that can't scale)\
    *(Note: The similarity transform can also be found using the entire point cloud data from the LiDar sensor through ICP)*