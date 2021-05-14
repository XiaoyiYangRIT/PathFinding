"""
The function to validate point in image, check if the point in the image, walkable.

Author: Xiaoyi Yang
"""
from PIL import Image
from Models import interface

def vallidatePoint(point):
    """
    Vallidate the point check if this point will be searched.
    :param img: the image to check on
    :param point: the point to be checked(tuple)
    :return: True if this point is on this image and passible
    """
    if isinstance(point, tuple) and (len(point) == 2):
        if point[0] > 0 and point[0] < interface.width:
            if point[1] > 0 and point[1] < interface.height:
                # If the speed is not 0, then it passible
                if interface.getSpeed(interface.pix[point[0], point[1]]) != 0:
                    return True
                
        return False
    else:
        raise Exception("vallidatePoint(): Not a valid point input, must be a tuple with 2 element")