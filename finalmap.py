import numpy as np
import matplotlib.pyplot as plt

def finalmap(clearance, x, y):

        if (0<= x <=300) and (0<= y <=200):
            # Object 1 = Centre ellipse
            centre_ellipse = []
            major_axis = int(40) + clearance
            minor_axis = int(20) + clearance
            # Elipse boundary
            if (((x - 150) ** 2) / major_axis ** 2) + (((y - 100) ** 2) / minor_axis ** 2) - 1<=0:
                return -1
            elif ((x - 225) ** 2 + (y - 150) ** 2 - (25 + clearance) ** 2)<=0:
                return -1
            elif   (5 * y + 3 * x - (875 + 5*clearance))<=0 and (0<= 5 * y - 3 * x + 625 + 5*clearance) and (0<= 5 * y + 3 * x - (725 - 5*clearance)) and  (5 * y - 3 * x + 475 - 5*clearance<=0):
                return -1
            # Object 4 = Bottom left rectangle
            elif  (9 * y - 5 * x - (462 + 9*clearance)<=0) and (65 * y + 38 * x - (6227 + 65*clearance)<=0) and (0<=9 * y - 5 * x + 205 + 9*clearance) and (0<= 65 * y + 38 * x - (5560 - 65*clearance)):
                return -1
            elif  ((y - 13 * x + (140 - 5* clearance)<=0) and (0 <= y - x - (100 - clearance)) and (5 * y + 7 * x - (1110 + 5*clearance)<= 0) and (y - (185 + clearance)<=0) and (x - 75<=0) and
                (0<= 10 * y + 13 * x - (2175 + clearance)) and (5 * y + 7 * x - (1450 + 5*clearance)<=0) and (0<=5 * y - 6 * x - (150 + clearance)) and (0<= x - 75)):
                return -1
            else:
                return x,y