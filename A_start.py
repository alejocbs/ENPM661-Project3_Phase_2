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


else:
    start_nodex = 150
    start_nodey = 10
    goal_nodex = 151
    goal_nodey = 99
    clearance = 0
    step = 1

start_pos = (start_nodex, start_nodey)
goal_pos = (goal_nodex, goal_nodey)
plt.plot(start_nodex, start_nodey, "Dr")
plt.plot(goal_nodex, goal_nodey, "Dr")

start_time = time.time()

if __name__ == '__main__':
    if finalmap(clearance, start_nodex, start_nodey)==-1:
        print("Start Position in obstacle space")

    elif finalmap(clearance, goal_nodex, goal_nodey)==-1:
        print("goal Position in obstacle space")

    else:
         path = Astart(start_pos, goal_pos, step)
    #     if path is not None:
    #         scatterx = [x[0] for x in path]
    #         scattery = [x[1] for x in path]
    #         plt.plot(scatterx, scattery, color='r', linewidth=4)
    #         plt.savefig('path_rigid.png')
    #         plt.show()
    #         elapsed_time = time.time() - start_time
    #         print("Time Required to Solve ", round(elapsed_time, 2), "seconds")
    #     else:
    #         print("No path found")