import pygame

class Points:
    def __init__(self,x,y,surface,colours,coordinates):
        self.x = x
        self.y = y
        self.surface = surface
        self.colours = colours
        self.coordinates = coordinates

    def draw(self):
        if len(self.coordinates) > 2:
            pygame.draw.lines(self.surface, self.colours, False, self.coordinates, 4)
