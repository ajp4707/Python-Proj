import pygame
# from Card import *
# from Deck import *
from Hand import *


class discardArea(Hand):
    #Similar to hand properties, but cards in middle are all shown
    def __init__(self, width, height, x, y, color):
        super().__init__(width, height, x, y, color,False)
            