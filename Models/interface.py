"""
An interface that stores all the data shared by many files.

Just for convienience

Author: Xiaoyi Yang
"""
import math

img = None
pix = None
draw = None
width = 0
height = 0
elevations = []
weather = ""

def setSpeed(color):
    if (color == (248,148,18)):    # 1.Open land               F89412 (248,148,18)
        return 0.95
    elif (color == (255,192,0)):   # 2.Rough meadow            FFC000 (255,192,0)
        return 0.75
    elif (color == (255,255,255)): # 3.Easy movement forest	   FFFFFF (255,255,255)
        if weather == "fall":          # Speed slows in fall
            return 0.45    
        return 0.85
    elif (color == (2,208,60)):    # 4.Slow run forest	       02D03C (2,208,60)
        return 0.65
    elif (color == (2,136,40)):    # 5.Walk forest	           028828 (2,136,40)
        return 0.55
    elif (color == (5,73,24)):     # 6.Impassible vegetation   054918 (5,73,24)
        return 0
    elif (color == (0,0,255)):     # 7.Lake/Swamp/Marsh	       0000FF (0,0,255)
        return 0
    elif (color == (71,51,3)):     # 8.Paved road	           473303 (71,51,3)
        return 1
    elif (color == (0,0,0)):       # 9.Footpath	               000000 (0,0,0)
        return 0.95
    elif (color == (205,0,101)):   # 10.Out of bounds	       CD0065 (205,0,101)
        return 0
    elif (color == (66,233,245)):  # 11.Ice surface(Winter)    42E9F5 (66,233,245)
        return 0.5
    elif (color == (135,72,12)):   # 12 Mud(Spring)            87480c (135,72,12)
        return 0.2
    else:
        raise Exception("setSpeed(): Color " + str(color) + " is not recorded")

def elevationSpeed(tan):
    return (1 - (1 / math.sqrt(3) * tan))
        
def getSpeed(rgb, spd = 1):
    return setSpeed(rgb[:3]) * spd

