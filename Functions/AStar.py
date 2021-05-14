"""
The function for A* Algorithm

Author: Xiaoyi Yang
"""
from Models.Path import Path
from Models.PathNode import PathNode
from Models import interface
from PIL import Image
from Functions import Validation, Cost
import heapq
import sys

def AStar(begin, end):
    """
    The core function, a heuristic search algorithm
    :param x: The x coordinate
    :param y: The y coordinate
    :return Boolean
    """
    # unnecessary print out, illustrate the current path being searched
    print(str(begin) + "   " + str(end))   
    # Intialize the path of points
    path = Path()
    
    # Intialize the current state
    currentH = Cost.HCost(begin, end)
    curState = PathNode(begin, currentH, 0)
    
    # Initialize the frontier state pool
    frontier = []
    
    # Initialize a 2D list separately for the Frontier Node and Explored Node
    # For checking if this node is Frontier or has been explored, in order to reduce the time complexity to O(1)
    isExplored = [[False for i in range(interface.height + 1)] for j in range(interface.width + 1)]
    isFrontier = [[False for i in range(interface.height + 1)] for j in range(interface.width + 1)]
    
    # The searching part, break when find the end point
    while not (curState.getPoint() == end):
        # Mark the current state as explored, for it will not be searched again
        isExplored[curState.getX()][curState.getY()] = True
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = curState.getX() + i
                y = curState.getY() + j
                
                # The point has been searched will not be searched again as stated above.
                if (not isFrontier[x][y]) and (not isExplored[x][y]):
                    
                    # Validated point will be searched, funciton defined as shown below
                    if Validation.vallidatePoint((x, y)):
                        isFrontier[x][y] = True
                        
                        # Calculate G and H
                        g = curState.getGcost() + Cost.GCost(curState.getPoint(), (x, y))
                        h = Cost.HCost((x, y), end)
                        
                        # Create a new Node
                        node = PathNode((x, y), h, g, curState)
                        
                        # Push into a min heap queue
                        heapq.heappush(frontier, node)
        
        # Pop out the Node with smallest F = G + H, Overwrite in Class PathNode
        
        try:
            curState = heapq.heappop(frontier)
        except:
            print("Can't find a valid path from %s to %s" % (str(begin), str(end)))
            sys.exit(1)
            #raise Exception("Search fails")
        
        isFrontier[curState.getX()][curState.getY()] = False
        
        # Add the current state to the Class Path, used to track the traveled path
        path.add(curState)
        
    
    # Get the Path, defined in Path 
    result, pathLength = path.trace(curState)
    
    return result, pathLength
    