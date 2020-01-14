import random 
from classes.arm import Arm
from classes.body import Body
from classes.head import Head
from classes.leg import Leg

class Monster:
    def __init__(self):
        self.arm = Arm()
        self.body = Body()
        self.head = Head()
        self.leg = Leg()

