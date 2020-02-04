import random

def reverseString(string):
    return string[::-1]


def hsl(h, s, l):
    r = ""
    r += "hsl("
    r += str(h) + ", "
    r += str(s) + "%, "
    r += str(l) + "%"
    r += ")"
    return r


def get_direction():
    if random.randint(0, 1) == 0:
        return "side"
    else:
        return "front"

def get_straightness():
    if random.randint(0, 1) == 0:
        return "straight"
    else:
        return "curved"
