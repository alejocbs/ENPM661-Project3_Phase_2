import heapq
import math
import matplotlib.pyplot as plt
from finalmap import *
import queue


def ActionSet(node, d):
    node_x = node[0]
    node_y = node[1]
    node_angle = np.deg2rad(node[2])

    thirty = np.deg2rad(30)
    sixty = np.deg2rad(60)
    m_thirty = np.deg2rad(-30)
    m_sixty = np.deg2rad(-60)

    all_moves = [[node_x + d * math.cos(sixty), node_y + d * math.sin(sixty), 30],
                 [node_x + d * math.cos(thirty), node_y + d * math.sin(thirty), 60],
                 [node_x + d * 1, 0, 0],  # parallel to x
                 [node_x + d * math.cos(m_thirty), node_y + d * math.sin(m_thirty), -30],  # negative 30
                 [node_x + d * math.cos(m_sixty), node_y + d * math.sin(m_sixty), -60]]  # negative 60
    # print(all_moves[0])
    # print(all_moves[0][1])
    valid_moves = []
    for i in range(0, 5):
        a = withinbounds(all_moves[i], 0.5)
        # print(a)
        if a:
            if not isobstacle(0, all_moves[i][0], all_moves[i][1], 0.5):
                valid_moves.append(all_moves[i])
            # print(valid_moves)
        else:
            continue

    return valid_moves


def withinbounds(node, thresh):
    x = node[0]
    y = node[1]
    # print(x)
    # print(y)
    if (0 <= x <= (300 / thresh)) and (0 <= y <= (200 / thresh)):
        return True
    else:
        return False


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


def round_region(co_ord, thresh):
    remainder = co_ord % 1
    quotient = co_ord // 1
    round_thresh = 0
    if remainder % thresh < thresh / 100:
        round_thresh = quotient + remainder

    else:
        for val in np.arange(0, 1, thresh):
            if (remainder - val) <= thresh:
                if abs(remainder - (val)) < abs(remainder - (val + thresh)):
                    round_thresh = quotient + val
                else:
                    round_thresh = quotient + (val + thresh)
                break

    return round_thresh


def discretize_node(node, thresh):
    node_x = node[0]
    node_y = node[1]
    node_angle = node[2]

    x = int(round_region(node_x, thresh) * (1 / thresh))
    y = int(round_region(node_y, thresh) * (1 / thresh))
    if node_angle < 0:
        node_angle = 360 + round(node_angle)
    node_angle = int(node_angle * (1 / 30))

    discretized_node = (x, y, node_angle)
    return discretized_node


# def Astart(start_pos, goal_pos,step):
#     # each node has three attributes 1) Parent 2) co-ordinates 3) Cost to Come
#     start_node = (0, start_pos, None)
#     goal_node = (0, goal_pos, None)
#     plot_x = []
#     plot_y = []
#     space = ActionSet(step)
#     open_list = []
#     closed_list = []
#     heapq.heappush(open_list, start_node)
#     obstacle_space[start_node[1][0]][start_node[1][1]] = 1
#
#     while len(open_list) > 0:
#         current_node = heapq.heappop(open_list)
#         heapq.heappush(closed_list, current_node)
#         plot_x.append(current_node[1][0])
#         plot_y.append(current_node[1][1])
#         print(current_node)
#         if len(plot_y) % 1000 == 0:
#             plt.plot(goal_pos[0], goal_pos[1], "hb")
#             plt.plot(plot_x, plot_y, '.y')
#             plt.plot(goal_pos[0], goal_pos[1], "hb")
#             plt.pause(0.001)
#
#         if current_node[1] == goal_node[1]:
#             print('Reached Goal')
#             final_path = backtracking(closed_list)
#             return final_path
#
#         for newnode_pos in space:
#
#             # Get node position
#             node_position = (current_node[1][0] + newnode_pos[0],
#                              current_node[1][1] + newnode_pos[1])
#             node_position_cost = current_node[0] + newnode_pos[2]
#             print("Current", node_position[0])
#             print("position", node_position_cost)
#             print("Goal pos", goal_pos)
#             print("difference", goal_pos[0]-node_position[0], goal_pos[1]-node_position[1])
#             d =math.sqrt((goal_pos[0]-node_position[0])**2+(goal_pos[1]-node_position[1])**2)
#
#             node_parent = current_node[1]
#             # Bounds check
#             #if node_position[0] > (len(obstacle_space) - 1) or node_position[0] < 0 or node_position[1] > (len(obstacle_space[1]) - 1) or node_position[1] < 0:
#             #    continue
#
#             # Ignore the locations in map which are obstacles
#             # if obstacle_space[node_position[0]][node_position[1]] != 0:
#             #     continue
#
#             # Creating cost_map
#             obstacle_space[round(node_position[0])][round(node_position[1])] = 1
#             new_node = (round(node_position_cost+d), node_position, node_parent)
#             print(new_node)
#             a = input(" ")
#             heapq.heappush(open_list, new_node)
def A_star(start_pos, goal_pos, d, thresh, radius):
    def take_second(elem):
        return elem[1]

    nodes = []
    nodes.append(start_pos)

    size_x = int(300 / thresh)
    size_y = int(200 / thresh)
    size_th = int(12)
    visited_nodes = np.zeros((size_x, size_y, size_th))
    print(visited_nodes.shape)
    discretized_start = discretize_node(start_pos, thresh)
    visited_nodes[discretized_start[0], discretized_start[1], discretized_start[2]] = 1
    costs2come = np.full((visited_nodes.shape[0], visited_nodes.shape[1], visited_nodes.shape[2]), np.inf)
    costs2goal = np.full((visited_nodes.shape[0], visited_nodes.shape[1], visited_nodes.shape[2]), np.inf)
    cost2come = 0
    costs2come[discretized_start[0], discretized_start[1], discretized_start[2]] = cost2come
    cost2goal = math.sqrt((goal_pos[0] - start_pos[0]) ** 2 + (goal_pos[1] - start_pos[1]) ** 2)

    parents = np.full((visited_nodes.shape[0], visited_nodes.shape[1], visited_nodes.shape[2]), np.nan)
    parents[discretized_start[0], discretized_start[1], discretized_start[2]] = -1

    queue = [(0, cost2come + cost2goal)]

    foundGoal = False
    while queue:
        queue.sort(key=take_second)
        parent, distance = queue.pop(0)
        current_node = nodes[parent]
        disc_current_node = discretize_node(current_node, thresh)
        cost2come = costs2come[disc_current_node[0], disc_current_node[1], disc_current_node[2]]
        space = ActionSet(current_node, d)
        for newnode_pos in space:
            cost2goal = math.sqrt((goal_pos[0] - newnode_pos[0]) ** 2 + (goal_pos[1] - newnode_pos[1]) ** 2)
            disc_newnode_pos = discretize_node(newnode_pos, thresh)
            if visited_nodes[disc_newnode_pos[0], disc_newnode_pos[1], disc_newnode_pos[2]] == 0:
                visited_nodes[disc_newnode_pos[0], disc_newnode_pos[1], disc_newnode_pos[2]] = 1
                costs2come[disc_newnode_pos[0], disc_newnode_pos[1], disc_newnode_pos[2]] = cost2come + d
                parents[disc_newnode_pos[0], disc_newnode_pos[1], disc_newnode_pos[2]] = parent
                nodes.append(newnode_pos)
                queue.append((len(nodes) - 1, cost2goal))
            elif cost2come + d < costs2come[disc_newnode_pos[0], disc_newnode_pos[1], disc_newnode_pos[2]]:
                costs2come[disc_newnode_pos[0], disc_newnode_pos[1], disc_newnode_pos[2]] = cost2come + d
                parents[disc_newnode_pos[0], disc_newnode_pos[1], disc_newnode_pos[2]] = parent
            if cost2goal < radius:
                foundGoal = True
                queue.clear()
                break

    goal = nodes[-1]  # negatve indexing, last element
    disc_goal = discretize_node(goal, thresh)
    parent = int(parents[disc_goal[0], disc_goal[1], disc_goal[2]])
    path_nodes = [parent]
    while parent != -1:
        node = nodes[path_nodes[-1]]
        disc_node = discretize_node(node, thresh)
        parent = int(parents[disc_node[0], disc_node[1], disc_node[2]])
        path_nodes.append(parent)
    path = [goal]
    for ind in path_nodes:
        if ind == -1:
            break
        else:
            path.insert(0, nodes[ind])
    return path
