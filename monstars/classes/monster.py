import body, arm, head, leg
from arm import Arm
from body import Body
from head import Head
from leg import Leg



class Monster:
    def __init__(self):
        self.arm = Arm()
        self.body = Body()
        self.head = Head()
        self.leg = Leg()

