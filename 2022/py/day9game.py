import sys
import math
from dataclasses import dataclass
import pygame


input="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

input="""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

input="""D 2
U 2
L 2
R 1
L 1
U 1
L 2
D 1
L 2
D 1
L 2
D 2
L 1
R 2
U 1
R 1
U 2
R 1
U 2
D 1
L 2
U 1
D 1
L 1
D 1
U 1
R 2
D 2
L 1
R 1
L 2
D 1
R 2
D 1
U 2
D 2
R 2
L 2
U 2
R 2
L 1
D 1
R 1
U 1
R 2
L 1
D 1
R 1
L 2
D 2
U 1
L 1
R 1
U 1
L 2
D 2
L 2
U 1
L 2
R 1
L 1
R 1
D 1
R 2
D 1
R 1
D 1
U 1
L 1
R 1
L 1
R 1
D 2
L 1
D 2
R 1
D 1
U 2
R 2
U 2
L 1
U 1
R 1
L 2
D 2
R 1
U 1
L 1
U 2
L 1
D 2
R 1
U 1
R 1
U 2
R 1
U 2
L 1
R 1
U 2
R 2
U 1
L 2
R 1
L 2
U 2
L 2
U 2
R 2
D 1
U 2
L 2
D 3
U 1
L 1
R 1
D 3
U 1
L 3
R 1
U 1
R 3
D 2
U 1
R 2
L 2
U 1
D 1
U 1
D 1
L 2
U 2
R 3
D 2
L 2
D 2
U 3
D 3
U 2
L 1
U 2
R 3
D 2
R 2
D 1
U 3
L 3
D 1
U 3
R 3
D 1
L 1
D 3
U 3
D 1
U 2
R 1
D 2
U 3
D 1
R 2
D 3
L 3
R 1
D 3
L 2
D 3
U 3
R 1
U 3
L 2
U 2
L 2
D 3
L 3
U 2
R 2
L 3
R 2
U 3
R 3
L 1
U 3
D 3
L 2
D 2
U 2
D 3
L 3
D 2
L 1
U 3
D 2
R 3
L 3
R 1
U 1
D 1
R 2
L 3
U 2
D 1
R 3
L 1
R 1
L 2
R 1
U 3
R 2
U 1
L 1
R 3
D 3
U 2
R 2
D 1
R 3
D 2
L 3
R 1
U 3
R 2
U 4
L 2
D 1
U 1
R 4
U 2
R 2
U 3
R 1
L 3
U 3
R 3
U 4
R 4
D 1
U 2
R 1
L 1
R 2
U 4
L 1
U 2
L 1
R 3
L 2
D 4
R 4
D 3
R 4
U 1
D 4
R 2
D 1
R 4
U 3
R 4
L 1
U 4
D 2
L 1
D 3
L 1
R 2
L 2
D 4
U 3
D 1
L 3
D 3
U 3
L 4
R 3
U 1
R 2
D 1
U 4
D 4
R 4
U 2
R 4
L 4
D 2
L 4
D 2
U 3
D 2
U 4
R 1
U 1
L 1
U 1
L 1
D 3
U 4
L 3
U 1
L 4
R 4
L 3
R 2
U 2
L 3
D 2
U 1
D 1
U 4
R 2
L 2
D 1
L 4
D 3
U 3
L 2
U 4
R 4
L 2
R 3
L 1
D 4
U 1
L 2
D 4
L 2
D 3
U 4
R 4
U 2
R 2
U 4
D 3
U 3
L 4
D 2
R 1
U 4
R 1
U 1
D 3
U 1
L 5
U 5
R 2
D 3
U 5
D 5
U 1
D 2
L 2
U 5
L 1
R 5
L 1
D 5
L 4
D 4
R 4
L 1
R 1
U 1
R 4
U 2
R 5
L 4
R 3
U 4
R 2
U 4
L 4
U 3
L 3
U 1
L 4
R 1
U 3
R 3
L 5
U 5
L 4
D 1
L 2
U 1
D 2
L 1
U 5
D 4
U 1
R 2
D 2
U 5
R 5
U 1
L 3
U 5
L 4
R 3
U 4
L 2
R 4
D 2
L 2
R 4
U 2
D 4
R 3
D 4
U 1
L 3
R 4
L 3
U 1
R 2
U 3
L 3
D 2
U 4
R 1
L 3
D 4
L 1
R 1
D 5
R 1
U 2
D 1
U 4
L 2
U 2
R 4
U 3
R 3
D 2
R 5
D 2
U 5
D 5
U 2
D 1
R 5
U 3
L 3
U 1
R 5
L 4
D 6
L 1
U 2
D 4
U 6
D 6
R 1
U 3
L 5
R 5
U 2
R 2
L 5
D 4
L 3
R 1
U 4
D 3
L 2
D 5
L 3
R 3
D 2
L 1
U 5
L 5
D 6
U 3
R 5
L 5
U 2
L 3
U 5
D 6
R 4
L 5
U 6
L 2
R 1
L 1
U 5
D 3
U 2
R 1
U 2
R 2
D 5
R 1
D 5
R 5
U 2
L 3
R 1
U 5
D 5
R 2
L 5
D 6
L 1
U 1
D 6
U 4
D 5
L 5
D 3
L 4
D 1
L 4
D 6
R 5
D 6
U 6
D 2
L 3
D 3
R 5
U 6
D 2
U 4
L 1
U 6
L 2
U 4
D 6
R 1
D 1
U 2
L 3
D 3
R 2
L 6
U 3
D 5
U 3
L 4
U 5
L 5
U 6
L 3
R 1
U 3
R 1
U 4
L 4
D 5
L 6
R 1
L 3
D 4
L 3
R 1
L 4
R 3
D 3
L 1
U 4
D 2
U 5
L 3
D 6
U 2
R 3
D 5
L 1
D 1
L 3
U 2
R 3
L 3
U 7
R 2
D 1
L 3
R 4
D 2
R 5
L 1
D 5
L 2
R 2
U 7
L 7
D 2
L 7
D 5
U 2
L 2
U 2
D 4
U 1
D 4
L 1
D 2
R 5
D 3
L 2
U 4
R 7
D 4
R 3
U 2
R 4
L 1
U 4
L 4
U 7
R 1
L 6
D 5
R 5
L 1
R 4
L 1
U 3
L 7
R 7
D 4
L 3
R 3
D 1
U 7
R 3
D 2
U 4
D 2
R 3
D 1
R 3
D 3
U 1
R 6
L 2
D 2
U 4
D 5
L 7
R 1
L 7
U 6
D 2
R 3
D 5
U 1
L 7
D 6
U 3
D 6
L 1
R 2
L 6
D 7
R 5
U 1
L 7
U 2
D 2
L 5
R 7
D 4
U 3
R 7
L 4
U 8
D 8
R 2
U 2
R 7
U 1
D 7
R 1
L 7
R 7
L 8
D 3
R 5
L 4
D 3
L 6
R 6
D 6
L 3
D 5
R 1
U 5
D 7
R 8
U 3
D 5
U 8
L 8
R 6
D 8
U 5
R 1
D 1
R 5
U 2
R 8
D 7
L 3
D 3
U 7
D 3
U 7
R 7
L 4
D 7
U 2
L 3
U 7
L 1
D 3
L 1
R 4
D 8
L 5
U 5
D 3
L 5
D 6
L 1
R 5
U 4
R 4
D 1
R 6
L 1
D 7
R 4
L 2
R 3
U 4
L 8
D 1
R 6
L 6
R 8
D 8
U 4
R 1
D 2
R 5
D 1
U 8
L 5
D 5
U 5
R 8
L 6
R 4
U 1
R 5
U 8
D 1
U 1
D 5
L 7
R 6
L 3
R 1
U 2
L 6
R 5
D 4
R 6
D 4
R 2
L 7
R 8
L 6
D 2
L 8
U 4
R 4
U 3
D 8
U 8
L 8
D 5
R 2
D 5
U 7
L 9
R 8
U 9
R 9
U 6
L 6
D 1
U 3
L 1
D 7
R 6
L 6
D 7
U 1
R 9
D 7
U 8
R 6
U 1
D 5
U 5
D 1
L 1
D 9
U 1
R 6
U 9
R 6
U 6
D 7
R 1
L 1
D 8
L 3
D 7
U 8
L 7
D 2
U 6
D 4
L 8
U 3
D 1
U 6
D 3
R 8
L 9
R 3
L 6
U 9
D 9
L 3
U 1
D 2
R 4
L 5
R 2
U 3
D 5
R 5
L 4
U 3
L 7
U 5
D 9
U 6
R 5
D 3
U 8
L 6
D 5
R 9
U 8
L 5
D 1
R 8
L 4
R 2
L 3
R 9
D 9
R 7
D 5
R 6
U 2
D 4
L 8
D 2
L 1
D 2
U 3
L 2
R 3
D 9
U 3
R 4
D 1
L 8
R 3
U 4
L 4
R 3
L 5
D 4
R 2
D 4
R 4
U 4
R 7
L 6
R 9
D 1
R 8
L 5
U 4
D 10
L 6
D 3
R 2
U 1
D 5
R 2
U 6
L 9
U 7
L 10
U 4
L 8
D 3
U 7
D 7
U 9
L 2
R 6
U 4
R 9
L 5
U 3
L 4
R 1
D 8
U 10
D 10
R 3
U 3
D 2
L 5
U 3
D 4
U 1
R 9
L 3
D 8
L 5
U 8
R 3
U 10
L 10
R 4
D 5
U 9
R 8
L 5
U 9
L 6
U 10
D 8
U 2
L 8
D 7
U 2
D 5
U 8
L 2
D 3
U 8
R 8
D 10
R 3
L 3
U 4
R 3
U 4
L 6
U 4
R 3
D 9
L 9
U 5
D 1
R 3
D 2
L 9
U 9
R 9
U 6
R 7
L 8
U 2
L 4
D 10
L 4
D 9
L 9
R 10
L 3
R 7
U 2
L 3
R 1
D 4
L 2
R 10
D 5
L 2
D 2
L 4
U 6
D 9
R 6
U 9
D 4
L 6
U 8
D 1
R 1
L 10
U 4
R 6
U 11
R 8
U 1
D 5
R 7
D 8
L 5
R 6
U 5
R 1
U 7
L 4
D 6
U 8
R 10
D 1
L 8
R 3
U 7
R 2
U 9
D 9
R 9
L 3
R 4
U 10
L 7
R 1
L 5
D 11
R 4
U 10
R 10
L 3
D 2
L 4
U 9
L 1
D 10
L 7
R 11
D 5
U 3
D 10
U 5
L 2
R 9
D 10
U 1
R 10
U 1
L 11
R 10
L 8
D 10
L 5
R 2
L 3
U 4
L 10
R 3
D 5
R 8
L 2
U 1
D 7
U 7
L 1
U 11
D 2
L 2
D 11
L 6
R 9
U 10
R 7
L 11
R 7
D 1
R 3
U 6
R 7
D 8
U 3
L 1
D 11
U 7
R 1
L 7
R 2
L 7
D 3
U 10
D 9
U 10
R 5
D 4
U 7
L 11
U 1
L 12
R 10
U 7
R 3
L 2
U 11
R 6
U 8
D 2
R 2
L 8
U 7
D 10
U 3
D 1
U 8
R 2
D 9
L 8
R 10
L 1
U 8
R 11
U 8
R 12
D 10
L 5
U 6
L 11
D 12
L 5
U 4
L 8
U 11
D 2
U 4
L 6
R 1
L 4
U 2
L 5
R 2
D 7
L 12
R 4
L 1
D 7
L 11
U 3
D 9
R 12
U 10
D 9
U 10
L 6
R 6
D 10
R 10
D 5
U 9
R 2
D 4
L 9
U 2
R 5
L 8
R 1
D 9
L 7
D 11
R 3
L 8
U 3
D 7
U 3
R 8
U 7
L 1
U 10
D 8
R 11
U 10
D 11
U 8
R 12
U 9
D 12
U 4
D 11
R 8
D 1
L 4
R 9
L 7
U 8
R 6
D 5
R 8
D 2
R 6
L 4
D 7
L 3
U 11
R 2
L 10
D 13
R 2
D 10
U 9
D 5
U 5
D 5
L 11
U 3
R 5
U 7
L 6
D 4
L 3
R 2
D 9
U 7
D 9
U 1
D 8
L 11
D 7
U 7
R 3
L 6
D 6
R 5
L 6
R 3
U 10
L 13
U 9
R 11
L 13
R 9
D 3
U 3
L 12
U 4
L 3
D 12
R 13
D 7
U 6
L 11
U 4
L 2
D 7
L 8
R 10
U 13
R 9
U 8
R 11
U 8
R 7
U 11
L 8
D 3
L 4
U 6
D 12
R 13
U 10
L 4
R 12
U 13
L 11
R 10
L 8
U 6
L 1
D 11
U 12
L 8
U 2
L 6
U 2
L 1
U 3
D 5
U 2
D 10
U 11
L 9
D 9
R 7
L 3
U 3
D 2
U 2
R 10
D 1
R 5
L 1
D 3
R 8
U 4
R 1
D 13
L 12
U 1
D 13
R 4
D 3
R 8
D 2
U 3
D 8
L 3
U 9
R 4
D 8
U 9
D 3
L 8
D 11
L 8
U 1
D 13
U 14
D 10
U 9
R 4
D 14
L 10
D 10
U 6
D 7
R 8
U 5
L 8
R 9
D 12
L 9
D 8
R 13
L 7
U 11
R 8
D 5
U 14
D 5
U 9
L 7
D 12
R 2
L 14
U 1
R 9
U 10
R 4
U 4
R 14
D 10
L 3
R 4
L 13
U 3
R 6
L 2
U 6
R 2
D 10
U 4
L 10
U 8
L 6
D 2
R 1
D 5
U 14
L 4
D 5
L 5
U 10
D 5
R 13
D 14
U 14
R 4
D 13
U 10
R 13
D 12
R 10
L 12
U 8
D 10
U 12
D 5
L 11
D 13
R 8
D 10
R 13
L 13
D 1
U 10
L 4
U 14
D 12
U 4
D 5
R 10
L 8
R 13
D 13
U 5
D 4
L 1
D 9
L 14
U 14
R 3
U 6
R 14
L 4
R 7
D 3
R 8
D 5
L 2
U 5
D 8
U 3
R 7
D 13
U 14
R 11
U 6
L 15
R 4
U 12
R 1
L 8
U 15
R 5
L 2
D 1
R 12
D 1
R 12
D 1
L 1
R 9
U 11
D 2
U 12
D 3
U 6
D 12
U 11
R 6
D 11
L 5
R 3
D 1
U 7
L 10
D 4
L 7
R 2
U 8
D 11
L 12
R 6
L 7
D 13
U 11
R 5
D 1
L 11
D 2
U 15
L 11
R 3
L 9
D 12
U 8
D 9
L 14
D 10
L 12
R 13
D 3
L 9
D 13
R 8
D 15
U 14
R 9
U 12
R 2
D 3
U 5
L 3
R 7
U 15
R 10
L 6
R 6
D 12
R 14
L 7
U 8
L 11
R 13
U 8
L 8
R 5
D 3
U 8
D 4
L 1
D 11
U 15
L 14
R 8
L 1
R 13
L 2
R 13
U 9
D 12
L 14
R 13
L 5
R 7
D 13
U 15
R 2
L 12
D 12
R 13
U 2
D 4
R 14
L 1
U 12
D 3
U 6
R 6
L 6
U 9
L 16
U 16
D 8
R 8
U 1
D 14
R 13
D 3
U 14
R 7
U 7
R 7
D 12
U 1
D 2
U 2
R 7
D 11
U 4
R 13
U 2
L 16
U 12
L 15
D 10
U 11
L 1
D 1
L 3
D 15
L 12
R 2
D 12
U 16
R 16
U 11
D 15
R 11
U 13
L 3
R 15
D 16
R 9
D 1
L 3
U 9
D 12
U 11
L 13
R 10
D 4
U 12
L 2
R 8
L 1
U 9
L 1
D 7
R 14
U 12
L 9
R 5
D 7
R 10
D 14
L 2
U 2
L 4
D 15
U 7
D 9
L 4
R 1
L 8
D 14
U 9
D 1
R 15
U 9
R 10
D 11
L 14
R 12
L 12
U 13
R 12
L 1
R 10
D 14
R 3
U 5
D 10
L 13
U 11
R 16
L 14
U 6
D 5
R 16
D 7
L 16
U 12
R 14
U 7
R 6
U 17
R 3
U 15
R 17
U 3
R 4
U 6
D 13
U 7
R 12
U 10
R 7
L 13
U 16
D 13
U 2
L 13
R 2
D 1
U 10
R 6
D 11
R 10
D 6
R 2
L 1
R 1
L 5
D 16
U 1
L 13
U 3
R 9
L 10
D 12
R 9
U 17
R 10
U 1
D 13
L 13
R 6
L 5
D 5
R 15
D 15
L 7
U 11
D 1
U 11
L 17
R 5
L 11
R 15
U 16
D 2
L 5
D 9
R 13
D 14
U 6
L 10
U 15
D 15
R 5
D 4
L 13
R 11
D 15
U 13
R 8
U 6
R 8
U 3
R 12
U 11
L 6
U 9
D 6
L 1
U 4
L 6
R 4
D 2
L 6
U 11
L 1
U 10
R 2
U 6
R 1
U 7
R 16
L 12
U 9
D 9
U 6
R 13
U 8
L 6
U 2
R 17
L 6
U 5
D 14
R 15
D 13
L 5
U 18
R 9
L 10
R 9
D 6
L 8
U 3
D 8
R 17
L 4
R 9
L 13
U 3
R 12
D 4
R 11
U 13
L 15
R 13
D 18
R 8
L 7
R 10
D 11
U 8
R 4
L 7
U 15
L 3
D 15
R 3
U 6
L 17
D 17
L 12
D 16
R 14
L 1
R 7
D 15
U 2
L 5
U 16
D 7
L 11
U 1
R 2
D 4
L 13
U 17
R 5
D 17
R 14
L 1
D 11
U 11
R 8
U 12
D 12
U 17
R 15
L 4
D 7
U 8
R 4
L 14
U 11
L 3
R 1
L 14
U 3
L 3
D 15
L 14
D 7
R 2
L 6
U 6
R 12
U 17
D 1
R 15
D 1
U 14
D 6
U 4
R 4
L 3
U 14
L 1
R 4
U 13
D 18
L 11
U 4
D 9
R 10
U 17
R 8
D 12
R 9
L 5
D 6
L 9
R 9
L 17
D 9
R 2
L 4
R 8
D 8
R 8
D 13
R 12
L 13
U 8
D 8
L 16
D 15
U 11
L 8
R 7
D 2
R 6
U 19
D 4
U 7
L 17
R 9
U 18
D 4
R 19
L 14
U 8
D 19
L 12
R 14
U 13
D 3
L 8
D 4
R 9
U 18
D 1
U 2
L 16
U 2
D 12
U 5
L 4
D 6
U 14
R 1
L 7
D 7
L 19
D 5
U 16
D 15
R 14
U 19
D 19
L 6
R 3
L 14
R 16
L 1
U 4
R 19
U 2
L 3
D 19
L 17
U 13
D 5
L 10
U 18
R 13
D 6
L 17
D 9
R 10
D 8
R 19
L 6
D 7
R 18
U 8
L 6
U 18
L 18
D 16
R 8
L 10
R 6
D 1
L 6
U 8
L 19
D 18
U 3
D 17
U 9
R 13
D 18
R 2
L 10
D 17
L 17
U 8
L 13
D 5
L 1
U 10
L 3
R 3
D 12
U 11
L 15
D 15"""

pygame.init()
screen = pygame.display.set_mode([800,800])
running = True

@dataclass
class vec2:
    __slots__ = 'x', 'y'
    x: int
    y: int
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

lines=input.split('\n')
head = vec2(0,0)
headprevious = vec2(0,0)
tail = vec2(0,0)
tail_visits=set(tuple())
lineindex=0
countindex=0
center = vec2(screen.get_width()/2,screen.get_height()/2)
while running and lineindex < len(lines):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    screen.fill((122,122,122))

    line=lines[lineindex]
    dir,count = line.split(' ')
    count=int(count)
    if dir=='R':
        xinc=0
        yinc=1
    elif dir=='L':
        xinc=0
        yinc=-1
    elif dir=='U':
        xinc=1
        yinc=0
    elif dir=='D':
        xinc=-1
        yinc=0

    if countindex < count:
        headprevious.x,headprevious.y=head.x,head.y
        head.x+=xinc
        head.y+=yinc
        
        if not (head.x>=tail.x-1 and head.x<=tail.x+1 and head.y>=tail.y-1 and head.y<=tail.y+1):
            tail.x=headprevious.x
            tail.y=headprevious.y
        tail_visits.add((tail.x, tail.y))

        # Draw a solid blue circle in the center
        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        # pygame.draw.circle(screen, (0, 0, 255), (head.x+center.x, head.y+center.y), 2)
        # pygame.draw.circle(screen, (0, 255, 0), (tail.x+center.x+5, tail.y+center.y+5), 2)

        # Flip the display
        # pygame.display.flip()
        countindex+=1
    
    if countindex == count:
        # reset
        countindex=0
        lineindex+=1


print('a',len(tail_visits))

tail_visits=set(tuple())
knots=[]
for i in range(10):
    knots.append(vec2(0,0))
lineindex=0
countindex=0
while running and lineindex < len(lines):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    screen.fill((122,122,122))

    line=lines[lineindex]
    dir,count = line.split(' ')
    count=int(count)
    if dir=='R':
        xinc=0
        yinc=1
    elif dir=='L':
        xinc=0
        yinc=-1
    elif dir=='U':
        xinc=1
        yinc=0
    elif dir=='D':
        xinc=-1
        yinc=0

    if countindex < count:
        # head
        knots[0].x+=xinc
        knots[0].y+=yinc
        
        # move all other knots
        for ki in range(1,len(knots)):
            if not (knots[ki-1].x>=knots[ki].x-1 and knots[ki-1].x<=knots[ki].x+1 
                    and knots[ki-1].y>=knots[ki].y-1 and knots[ki-1].y<=knots[ki].y+1):
        
                update_x=False
                update_y=False
                if knots[ki-1].x==knots[ki].x:
                    update_y=True
                elif knots[ki-1].y==knots[ki].y:
                    update_x=True
                else:
                    if knots[ki-1].x > knots[ki].x+1:
                        knots[ki].x+=1
                        update_y=True
                    elif knots[ki-1].x < knots[ki].x-1:
                        knots[ki].x-=1
                        if knots[ki-1].y > knots[ki].y:
                            knots[ki].y+=1
                        elif knots[ki-1].y < knots[ki].y:
                            knots[ki].y-=1
                    elif knots[ki-1].y > knots[ki].y+1:
                        knots[ki].y+=1
                        update_x=True
                    elif knots[ki-1].y < knots[ki].y-1:
                        knots[ki].y-=1
                        if knots[ki-1].x > knots[ki].x:
                            knots[ki].x+=1
                        elif knots[ki-1].x < knots[ki].x:
                            knots[ki].x-=1
                if update_x:
                    if knots[ki-1].x > knots[ki].x:
                        knots[ki].x+=1
                    else:
                        knots[ki].x-=1
                if update_y:
                    if knots[ki-1].y > knots[ki].y:
                        knots[ki].y+=1
                    else:
                        knots[ki].y-=1

            if ki == len(knots)-1:
                tail_visits.add((knots[ki].x, knots[ki].y))
        
        
        for ki in range(len(knots)):
            # Draw a solid blue circle in the center
            pygame.draw.rect(screen, (0,255-(ki*10), 255-(ki*20)), 
                    pygame.Rect(knots[ki].x+center.x+(ki*2), knots[ki].y+center.x+(ki*2), 10,10)
                    )
    countindex+=1
    if countindex == count:
        countindex=0
        lineindex+=1

    # Flip the display
    pygame.display.flip()            
        
pygame.quit()
print('b',len(tail_visits))