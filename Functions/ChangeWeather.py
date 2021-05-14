"""
The function for weather change.
Spring: aka "mud season". Any pixels within fifteen pixels of water that can be reached from a water pixel without gaining more than one meter of elevation (total) are now underwater. 
Summer: The default weather
Fall: Increase the time for any paths through (that is, adjacent to) easy movement forest (but only those paths).
Winter: Any water within seven pixels of non-water is safe to walk on
"""
from Models import interface

def ChangeWeather():
    """
    Recognize the weather and change the map accordingly
    """
    if interface.weather == "spring":
        print("Lake expands in spring")
        
        # I'm recording the elevation of all water pixel and non-water within 15 pixels (if gains elevation no more than 1 meter)
        # It will be easier to determine if the pixel gains evelation more than 1 meter
        tempElevations = interface.elevations.copy()        
        
        # Found the water edge
        waterEdge = []
        # Find the edge of water
        for x in range(1, interface.width):
            for y in range(1, interface.height):
                if isWater(x, y):
                    # Determine if water edge, find the function below
                    if checkSurrending(x, y):
                        waterEdge.append((x, y));
                        # Increase the elevation by 1 here to reduce the time complexity
                        tempElevations[y][x] = tempElevations[y][x] + 1
        
        
        # Find and color the surging water
        for i in range(15):
            # temp for BFS, store the water edge of each level
            temp = []  
            for point in waterEdge:
                # search all 8 pixels around
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        tempX = point[0] + i
                        tempY = point[1] + j
                        # check if pixel still in image
                        if (tempX > 0) and (tempX < interface.width) and (tempY > 0) and (tempY < interface.height):
                            # find the non-water pixel
                            if interface.pix[tempX, tempY][:3] != (0,0,255) and interface.pix[tempX, tempY][:3] != (205,0,101):
                                # find the pixel will be underwater
                                if tempElevations[tempY][tempX] < tempElevations[point[1]][point[0]]:
                                    # then it's underwater now
                                    tempElevations[tempY][tempX] = tempElevations[point[1]][point[0]]
                                    interface.draw.point((tempX, tempY), fill=(135,72,12))
                                    temp.append((tempX, tempY))
            # prepare for next level of searching
            waterEdge = temp
    elif interface.weather == "summer":
        print("Nothing changed, summer is the default weather.") # Default weather, no action required
    elif interface.weather == "fall":
        print("The speed on easy movement forest is now slower")  # No map changeing required in fall
    elif interface.weather == "winter":
        print("Lake partially freeze in winter")                 # Winter, similar to spring
        # Found the water edge
        waterEdge = []
        # Find the edge of water
        for x in range(1, interface.width):
            for y in range(1, interface.height):
                if isWater(x, y):
                    if checkSurrending(x, y):
                        waterEdge.append((x, y));
        
        
        # Found and color the frozen water
        for level in range(7):
            temp = []
            for point in waterEdge:
                
                interface.draw.point(point, fill=(66,233,245))
                
                # Draw first then search, no need for search if on level 6 (7th)
                if level < 6:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            tempX = point[0] + i
                            tempY = point[1] + j
                            if (tempX > 0) and (tempX < interface.width) and (tempY > 0) and (tempY < interface.height):
                                if interface.pix[tempX, tempY][:3] == (0,0,255):
                                    temp.append((tempX, tempY))
                           
            waterEdge = temp
    else:
        raise Exception("Not a valid weather type")

def isWater(x, y):
    """
    Functions use to check if this pixel is water
    :param x: The x coordinate
    :param y: The y coordinate
    :return Boolean
    """
    if interface.pix[x, y][:3] == (0,0,255):
        return True
    return False
        
def checkSurrending(x, y):
    """
    pre-condition: this pixel is water already
    Functions used to find the water edge
    If any pixel around this pixel is Non-Water, then this is edge
    :param x: The x coordinate
    :param y: The y coordinate
    :return Boolean
    """
    for i in range(-1, 2):
        for j in range(-1, 2):
            tempX = x + i
            tempY = y + j
            if (tempX > 0) and (tempX < interface.width) and (tempY > 0) and (tempY < interface.height):
                if not (interface.pix[tempX, tempY][:3] == (0,0,255)):
                    return True
    return False