# ENPM661-Project3_Phase_2
## Implementation of A Start algorithm for a Rigid Robot
Fig. Final Obstacle Map
    ![alt text](https://github.com/alejocbs/ENPM661-Project3_Phase_2/blob/master/map.png "Map Title Text 1")
## Libraries used
    1) Matplotlib
    2) Numpy
    3) Time
    4) Math
    5) heapq
 Warning - Use of 'heapq' may generate low memory or running out of memory error
## Files required in the source directory
    1) Astar_rigid.py
    2) finalmap.py
    3) Functions.py
## How to run the code-
 ### System Requirements-
        Python v3.0.x or later
 ### Set the User Defined Co-ordinates Flag in 'main.py'
        True= User inputs the initial and goal configuration.
        False- Pre-defined initial and goal configuration.
 ### Input arguements-
 #### For Rigid Robot(astar_rigid.py)
        1) Input Start point x co-ordinate - Enter X co-ordinate of start position.
        2) Input Start point y co-ordinate - Enter Y co-ordinate of start position.
        3) Input Goal point x co-ordinate - Enter X co-ordinate of goal position.
        4) Input Goal point y co-ordinate - Enter Y co-ordinate of goal position.
        5) Input Clearance                - Enter Radius of the robot
        6) Input Threshold                - Enter a Threshold for the vectors   
        7) Input Radius of the robot      - Enter Radius of the robot
        
Note: 
    If the radius of the robot is bigger than 15 this will cause the map to look distored. But will still calculate optimal path             following the conditions.
    If the step is bigger than the obstacle the vector would jump over it.
    If vector plot is required uncomment line 85 and 86 from Funtions.py 
 ## Runtime
    Runtime for:
        Start Position=(5,5)
        Goal Position =(295,195)
        Average ~ 100-133.3 seconds when showing no vectors
        Plotting vectors add 0.01 sec per vector
    Figure:- Final Path for (5,5) to (295,195)
    
   ![alt text](https://github.com/alejocbs/ENPM661-Project3_Phase_2/blob/master/path_rigid.png "Solved point")
   
   ##Video link:
 https://youtu.be/GoGM4uHsB8g
   
