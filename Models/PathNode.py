"""
A module that represents the node in A* searching.

Author: Xiaoyi Yang
"""
class PathNode:
    
    __slots__ = "x", "y", "hcost", "gcost", "prev",
    
    def __init__(self, point, hcost = 0, gcost = 0, prev = None):
        """
        Construct a node instance.
        :param point: the point with coordinate[x, y]
        :param hcost: the hueristic cost
        :param gcost: the goal cost
        """
        self.x = point[0]
        self.y = point[1]
        self.hcost = hcost
        self.gcost = gcost
        self.prev = prev
        
    def setHcost(self, hcost):
        self.hcost = hcost
        
    def getHcost(self):
        return self.hcost
    
    def setGcost(self, gcost):
        self.gcost = gcost
        
    def getGcost(self):
        return self.gcost
       
    def getFcost(self):
        return self.gcost + self.hcost
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getPoint(self):
        return (self.x, self.y)
    
    def setPrev(self, prev):
        self.prev = prev
    
    def getPrev(self):
        return self.prev
    
    def __eq__(self, other):
        """
        Overwrite the eq, considered as equal if coordinates are the same
        :param other: The other point being compared
        :return Boolean: 
        """
        return (self.getX() == other.getX()) and (self.getY() == other.getY())
    
    def __lt__(self, other):
        """
        Overwrite the lt, compare the FCost.
        :param other: The other point being compared
        :return Boolean: 
        """
        return self.getFcost() < other.getFcost()
        
    def __str__(self):
        """
        Return a string representation of the node
        """
        return "X: " + str(self.getX()) + " Y: " + str(self.getY())