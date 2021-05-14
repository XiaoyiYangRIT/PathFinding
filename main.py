"""
Lab1

Author: Xiaoyi Yang
"""

import sys
import time
from Functions.AStar import AStar
from Functions.ChangeWeather import ChangeWeather
from PIL import Image, ImageDraw, ImageFont
from Models import interface

class Orienteering:
    """
    Class: Orienteering
    """
    
    def main():
        """
        The main program
        Load all required files
        Run A* algorithm
        Output the result
        """
        # Load the img, initialize the draw
        interface.img = Image.open("input/" + sys.argv[1])
        interface.pix = interface.img.load()
        interface.draw = ImageDraw.Draw(interface.img)
        interface.width, interface.height = interface.img.size
        
        # Load the elevations
        with open("input/" + sys.argv[2], "r") as f:
            for height in f.readlines():
                interface.elevations.append(list(map(float, height.lstrip(' ').rstrip('\n').split())))
                
        # Load the stops on path
        stops = []
        with open("input/" + sys.argv[3], "r") as f:
            for point in f.readlines():
                # Convert the coordinates to int
                stop = list(map(int, point.lstrip(' ').rstrip('\n').split(" ")))
                
                # Save stops into list
                stops.append(tuple(map(int, stop)))
                       
        # Load the weather
        interface.weather = sys.argv[4]
        # Load the weather and change the map accordingly
        ChangeWeather()
        
        # Initialize the path list and path length
        path = []
        length = 0
        # Iterate through the path
        for i in range(len(stops) - 1):
            result, pathLength = AStar(stops[i], stops[i + 1]) # Run A* and get the partial path
            path = path + result                               # Add up the partial path to get the whole path
            length = length + pathLength                       # Add up the partial length to get the whole length
        
        for stop in stops:
            p1 = (stop[0] - 3, stop[1] + 3)                # Point out these stops on map, draw rectanges
            p2 = (stop[0] + 3, stop[1] - 3)
            interface.draw.rectangle([p1, p2], fill="blue")
        
        for point in path:
            p1 = (point[0] - 1, point[1] + 1)                # Point out these stops on map, draw rectanges
            p2 = (point[0], point[1])
            interface.draw.rectangle([p1, p2], fill="red")         # Illustrate the path on image
        
        # Print out the path length (in meters) on image
        text = "The path length is " + "{:.6}".format(length) + "m"
        font = ImageFont.truetype('"input/Roboto-Regular.ttf', 20)
        interface.draw.text((50, 20), text, (255, 255, 255), font=font)
        
        #interface.img.show()
        interface.img.save("output/" + sys.argv[5],"PNG")
        
        
    if __name__ == "__main__":
        start_time = time.time()
        main()
        print("--- %s seconds ---" % (time.time() - start_time))