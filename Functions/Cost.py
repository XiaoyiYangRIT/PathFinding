"""
The functions to calculate GCost and HCost. The default speed is 5

Author: Xiaoyi Yang
"""
import math
from PIL import Image
from Models import interface

def HCost(p1, p2, speed = 5):
    """
    Functions used to calculate H Cost, which is the straight line between 2 points
    :param p1: The 1st point
    :param p2: The 2nd point
    :return float: the time cost of traveling
    """
    x1 = p1[0]
    y1 = p1[1]
    z1 = interface.elevations[y1][x1]
    
    x2 = p2[0]
    y2 = p2[1]
    z2 = interface.elevations[y2][x2]
    
    distance = math.sqrt(((x2 - x1)*10.29)**2 + ((y2 - y1)*7.55)**2 + (z2 - z1)**2)
    
    return distance / speed
    
def GCost(p1, p2, speed = 5):
    """
    Functions used to calculate G Cost, which is the weighted value between 2 points.
    Determined by slope, terrain
    :param p1: The 1st point
    :param p2: The 2nd point
    :return float: the time cost of traveling
    """
    x1 = p1[0]
    y1 = p1[1]
    z1 = interface.elevations[y1][x1]
    
    x2 = p2[0]
    y2 = p2[1]
    z2 = interface.elevations[y2][x2]
    
    distance = math.sqrt(((x2 - x1)*10.29)**2 + ((y2 - y1)*7.55)**2 + (z2 - z1)**2)
    
    # Calculate the slope
    tan = abs(z2 - z1) / math.sqrt(((x2 - x1)*10.29)**2 + ((y2 - y1)*7.55)**2)
    
    weightSpeed = interface.getSpeed(interface.pix[x2, y2], speed) * interface.elevationSpeed(tan)
    
    return distance / weightSpeed
