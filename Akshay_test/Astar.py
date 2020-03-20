import time
from Astar_functions import *
from finalmap import *

userdefined = False
if userdefined:
    start_nodex = int(input("Please enter Start point X coordinate: "))
    start_nodey = int(input("Please enter Start point Y coordinate: "))

    goal_nodex = int(input("Please enter Goal point X coordinate: "))
    goal_nodey = int(input("Please enter Goal point Y coordinate: "))
    clearance = int(input("Please enter the Radius of the robot"))
else:
    start_nodex = 5
    start_nodey = 15
    goal_nodex = 290
    goal_nodey = 75
    clearance = 5
    thresh=0.5

start_pos = (round(start_nodex/thresh), round(start_nodey/thresh))
goal_pos = (round(goal_nodex/thresh), round(goal_nodey/thresh))
plt.plot(start_nodex, start_nodey, "Dr")
plt.plot(goal_nodex, goal_nodey, "Dr")

start_time = time.time()

if __name__ == '__main__':
    final_obs, wall_x, wall_y = finalmap(clearance,0.5)
    if start_pos in (zip(wall_x, wall_y) or final_obs):
        print("Start Position in obstacle space")

    elif goal_pos in (zip(wall_x, wall_y) or final_obs):
        print("goal Position in obstacle space")

    else:
        path = Astar(start_pos, goal_pos, final_obs)
        if path is not None:
            scatterx = [x[0] for x in path]
            scattery = [x[1] for x in path]
            plt.plot(scatterx, scattery, color='r', linewidth=4)
            plt.savefig('path_rigid.png')
            plt.show()
            elapsed_time = time.time() - start_time
            print("Time Required to Solve ", round(elapsed_time, 2), "seconds")
        else:
            print("No path found")
