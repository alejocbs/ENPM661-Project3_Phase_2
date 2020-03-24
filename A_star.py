import time
from Functions import *
from finalmap import *

userdefined = False
if userdefined:
    start_nodex = int(input("Please enter Start point X coordinate: "))
    start_nodey = int(input("Please enter Start point Y coordinate: "))

    goal_nodex = int(input("Please enter Goal point X coordinate: "))
    goal_nodey = int(input("Please enter Goal point Y coordinate: "))
    clearance = int(input("Please enter the Radius of the robot"))
    step = int(input("Please enter the value of the step"))
    thresho =int(input("Please enter the threshold"))
    radius =int(input("Please enter the radius"))
    # start_angle = int(input("Please enter the value of the step"))
    # goal_angle =int(input("Please enter the value of the step"))


else:
    start_nodex = 50
    start_nodey = 30
    goal_nodex = 295
    goal_nodey = 195
    clearance = 1
    d = 1
    thresho = 1
    radius = 1
    start_angle = 60
    goal_angle = 30
d=5
start_pos = (start_nodex, start_nodey, start_angle)
goal_pos = (goal_nodex, goal_nodey, goal_angle)
plt.plot(start_nodex, start_nodey, "Dr")
plt.plot(goal_nodex, goal_nodey, "Dr")

start_time = time.time()

if __name__ == '__main__':
    final_obs, wall_x, wall_y = finalmap(clearance)
    if isobstacle(clearance, start_nodex, start_nodey, thresho):
        print("Start Position in obstacle space")

    elif isobstacle(clearance, goal_nodex, goal_nodey, thresho):
        print("goal Position in obstacle space")

    else:
        path = Astar(start_pos, goal_pos, d, clearance,thresho)
        print(path)
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
