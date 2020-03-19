import heapq
import math
import matplotlib.pyplot as plt
from finalmap import *



def ActionSet(d):
    all_moves = [[d*1, 0, 0],                                # parallel to x
                 [d*math.cos(30),  d*math.sin(30), 30],         # positive 30
                 [d*math.cos(60),  d*math.sin(60), 60],         # positive 60
                 [d*math.cos(-30), d*math.sin(-30), -30],        # negative 30
                 [d*math.cos(-60), d*math.sin(-60), -60]]        # negative 60
    return all_moves


def backtracking(closed_list):
    backtrack = []
    length = len(closed_list)
    current_pos = closed_list[length - 1][1]
    backtrack.append(current_pos)
    parent = closed_list[length - 1][2]
    while parent is not None:
        for i in range(length):
            X = closed_list[i]
            if X[1] == parent:
                parent = X[2]
                current_pos = X[1]
                backtrack.append(current_pos)

    return backtrack[::-1]


def Astart(start_pos, goal_pos,step):
    # each node has three attributes 1) Parent 2) co-ordinates 3) Cost to Come
    start_node = (0, start_pos, None)
    goal_node = (0, goal_pos, None)
    plot_x = []
    plot_y = []
    space = ActionSet(step)
    open_list = []
    closed_list = []
    heapq.heappush(open_list, start_node)
    obstacle_space[start_node[1][0]][start_node[1][1]] = 1

    while len(open_list) > 0:
        current_node = heapq.heappop(open_list)
        heapq.heappush(closed_list, current_node)
        plot_x.append(current_node[1][0])
        plot_y.append(current_node[1][1])
        print(current_node)
        if len(plot_y) % 1000 == 0:
            plt.plot(goal_pos[0], goal_pos[1], "hb")
            plt.plot(plot_x, plot_y, '.y')
            plt.plot(goal_pos[0], goal_pos[1], "hb")
            plt.pause(0.001)

        if current_node[1] == goal_node[1]:
            print('Reached Goal')
            final_path = backtracking(closed_list)
            return final_path

        for newnode_pos in space:

            # Get node position
            node_position = (current_node[1][0] + newnode_pos[0],
                             current_node[1][1] + newnode_pos[1])
            node_position_cost = current_node[0] + newnode_pos[2]
            print("Current", node_position[0])
            print("position", node_position_cost)
            print("Goal pos", goal_pos)
            print("difference", goal_pos[0]-node_position[0], goal_pos[1]-node_position[1])
            d =math.sqrt((goal_pos[0]-node_position[0])**2+(goal_pos[1]-node_position[1])**2)

            node_parent = current_node[1]
            # Bounds check
            #if node_position[0] > (len(obstacle_space) - 1) or node_position[0] < 0 or node_position[1] > (len(obstacle_space[1]) - 1) or node_position[1] < 0:
            #    continue

            # Ignore the locations in map which are obstacles
            # if obstacle_space[node_position[0]][node_position[1]] != 0:
            #     continue

            # Creating cost_map
            obstacle_space[round(node_position[0])][round(node_position[1])] = 1
            new_node = (round(node_position_cost+d), node_position, node_parent)
            print(new_node)
            a = input(" ")
            heapq.heappush(open_list, new_node)