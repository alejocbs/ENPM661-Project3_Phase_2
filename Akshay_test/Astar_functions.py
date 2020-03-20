import heapq
import math
import matplotlib.pyplot as plt
import numpy as np


def ActionSet(d):
    thirty=np.deg2rad(30)
    sixty = np.deg2rad(60)
    m_thirty = np.deg2rad(-30)
    m_sixty = np.deg2rad(-60)
    all_moves = [[d * 1, 0, d],  # parallel to x
                 [d * math.cos(thirty), d * math.sin(thirty), 2*d * math.sin(thirty)],  # positive 30
                 [d * math.cos(sixty), d * math.sin(sixty), 2*d * math.cos(sixty)],  # positive 60
                 [d * math.cos(m_thirty), d * math.sin(m_thirty), 2*d * math.sin(m_thirty)],  # negative 30
                 [d * math.cos(m_sixty), d * math.sin(m_sixty), 2*d * math.cos(m_sixty)]]  # negative 60
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


def Astar(start_pos, goal_pos, obstacle_space):
    # each node has three attributes 1) Parent 2) co-ordinates 3) Cost to Come
    start_node = (0, start_pos, None)
    goal_node = (0, goal_pos, None)
    plot_x = []
    plot_y = []
    d=10
    eightspace = ActionSet(d)
    open_list = []
    closed_list = []
    heapq.heappush(open_list, start_node)
    obstacle_space[start_node[1][0]][start_node[1][1]] = 1

    while len(open_list) > 0:
        current_node = heapq.heappop(open_list)
        heapq.heappush(closed_list, current_node)
        plot_x.append(current_node[1][0])
        plot_y.append(current_node[1][1])

        if len(plot_y) % 1000 == 0:
            plt.plot(goal_pos[0], goal_pos[1], "hb")
            plt.plot(plot_x, plot_y, '.y')
            plt.plot(goal_pos[0], goal_pos[1], "hb")
            plt.pause(0.001)

        if current_node[1] == goal_node[1]:
            print('Reached Goal')
            final_path = backtracking(closed_list)
            return final_path

        for newnode_pos in eightspace:

            # Get node position
            node_position = (current_node[1][0] + newnode_pos[0],
                             current_node[1][1] + newnode_pos[1])
            node_position_cost = current_node[0] + newnode_pos[2]
            cost2goal = round(math.sqrt((
                (current_node[1][0] - goal_node[1][0]) ** 2 + (current_node[1][1] - goal_node[1][1]) ** 2)))
            final_cost = node_position_cost + cost2goal
            node_parent = current_node[1]
            # Bounds check
            if node_position[0] > (len(obstacle_space) - 1) or node_position[0] < 0 or node_position[1] > (len(obstacle_space[1]) - 1) or node_position[1] < 0:
                continue

            # Ignore the locations in map which are obstacles
            if obstacle_space[round(node_position[0])][round(node_position[1])] != 0:
                continue

            # Creating cost_map
            obstacle_space[round(node_position[0])][round(node_position[1])] = 1
            new_node = (final_cost, node_position, node_parent)
            heapq.heappush(open_list, new_node)
