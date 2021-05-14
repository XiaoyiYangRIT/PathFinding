"""
A module for representing the tree of explored path

Author: Xiaoyi Yang
"""
from Models.PathNode import PathNode
import math

class Path:
    """
    Class: Path
    Description: 
    """

    __slots__ = "top", "beginning", "cursor"

    def __init__(self):
        """
        Construct a WordTree instance.
        """
        self.top = None
        

    def add(self, node):
        """
        Add a node in the path
        :param node: the searched node
        :param prev: the previous node for tracing
        """
        if not self.top:
            self.beginning = node
            self.top = node
        else:
            self.top = node
        
    def get(self, node):
        if(self.find(node)):
            return self.cursor
        
    def find(self, node):
        """
        Find the node in the tree
        set the node to cursor if found
        :param node: the node being to be searched
        :return boolean
        """
        if not self.top:
            raise Exception("The path tree is empty.")
            return False;
            
        self.cursor = self.top
        while(True):
            if self.cursor == node:
                return True
            
            print(self.cursor)
            if (self.cursor == self.beginning) or (self.cursor.getPrev() == None):
                raise Exception("This node at " + string((node.getX(), node.getY())) + " is not on this Path.")
                return False;
            else:
                self.cursor = self.cursor.getPrev()

    def trace(self, node):
        """
        Trace the PathNode in the tree, find the path
        :param node: the node starts to trace back
        :return The list of path
        """
        result = []
        pathLength = 0
        if(self.find(node)):
            while(True):
                result.append(self.cursor.getPoint())
                if (self.cursor == self.beginning) or self.cursor.getPrev() is None:
                    result.reverse()
                    return result, pathLength
                
                if self.cursor.getPrev() is None:
                    raise Exception("The point at " + str(self.cursor) + " has no previous point")
                else: 
                    temp = self.cursor.getPrev()
                    pathLength += math.sqrt(((temp.getX() - self.cursor.getX())*10.29)**2 + ((temp.getY() - self.cursor.getY())*7.55)**2)
                    self.cursor = temp