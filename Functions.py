import heapq
import math
import matplotlib.pyplot as plt
from finalmap import *



def ActionSet(d):
    all_moves = [[d*1, 0, 0],                                # parallel to x
                 [d*math.cos(math.radians(30)),  d*math.sin(math.radians(30)), 30],         # positive 30
                 [d*math.cos(math.radians(60)),  d*math.sin(math.radians(60)), 60],         # positive 60
                 [d*math.cos(math.radians(-30)), d*math.sin(math.radians(-30)), -30],        # negative 30
                 [d*math.cos(math.radians(-60)), d*math.sin(math.radians(-60)), -60]]        # negative 60
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


def Astar(start_pos, goal_pos,step,clear, thres):
    # each node has three attributes 1) Parent 2) co-ordinates 3) Cost to Come
    start_node = (0, start_pos, None)
    goal_node = (0, goal_pos, None)
    plot_x = []
    plot_y = []
    space = ActionSet(step)
    open_list = []
    sort=[]
    heapq.heappush(sort, start_node)
    closed_list = []
    open_list.append(start_node)
    # obstacle_space[start_node[1][0]][start_node[1][1]] = 1
    x=0
    plt.xlim(0, 300)
    plt.ylim(0, 200)
    while len(open_list) > 0:
        current_node = heapq.heappop(sort)
        closed_list.append( current_node)

        plot_x.append(current_node[1][0])
        plot_y.append(current_node[1][1])

        res=(((current_node[1][0] - goal_pos[0]) ** 2) + ((current_node[1][1]-goal_pos[1]) ** 2) )
        if res<=(step*1.5)**2:
            print('Reached Goal')
            final_path = backtracking(closed_list)
            return final_path
        for newnode_pos in space:

            # Get node position
            node_position = (current_node[1][0] + newnode_pos[0],
                             current_node[1][1] + newnode_pos[1],newnode_pos[2])
            node_parent = current_node[1]
            cost2come = math.sqrt((goal_pos[0] - node_position[0]) ** 2 + (goal_pos[1] - node_position[1]) ** 2)
            cost2go =  math.sqrt((node_position[0]-node_parent[0]) ** 2 + (node_position[1] - node_parent[1]) ** 2)
            node_position_cost = current_node[0] + cost2go
            Aux = cost2go + cost2come

            # Bounds check
            # if node_position[0] > (len(obstacle_space) - 1) or node_position[0] < 0 or node_position[1] > (len(obstacle_space[1]) - 1) or node_position[1] < 0:
            #     continue
            #
            # # Ignore the locations in map which are obstacles
            # if obstacle_space[node_position[0]][node_position[1]] != 0:
            #     continue

            # Creating cost_map
            # obstacle_space[node_position[0]][node_position[1]] = 1
            node_position1=isobstacle(clear,node_position[0],node_position[1],thres)
            if node_position1==False:
                new_node = (Aux, node_position, node_parent)
                heapq.heappush(sort, new_node)

            plt.quiver(new_node[2][0], new_node[2][1], newnode_pos[0], newnode_pos[1], units='xy' ,scale=1,color= 'b',headwidth = 1,headlength=0,width=0.2)
            plt.pause(0.001)

        x+=1
