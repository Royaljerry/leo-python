from classes import utilities as util
import random
from PIL import Image, ImageDraw, ImageFont


def get_body(x, y, s, a, monster_draw):
    x1 = x + s.arm_length
    y1 = y + s.head_height
    x2 = x1 + s.body_length
    y2 = y1 + s.body_height
    monster_draw.rectangle(
        [
            util.convert_x(x1),
            util.convert_y(y1),
            util.convert_x(x2),
            util.convert_y(y2),
        ],
        fill=util.random_color(),
    )
    return monster_draw


def get_head(x, y, s, a, monster, monster_draw, color):
    # draw head shape
    y1 = y + 0
    y2 = y1 + s.head_height
    if monster.head.direction == "left":
        x1 = x + s.arm_length
        x2 = x1 + s.head_length
    elif monster.head.direction == "right":
        x1 = x + s.arm_length + s.body_length - s.head_length
        x2 = x1 + s.head_length
    elif monster.head.direction == "front":
        x1 = x + s.arm_length + s.body_length / 2 - s.head_length / 2
        x2 = x1 + s.head_length
    monster_draw.rectangle(
        [
            util.convert_x(x1),
            util.convert_y(y1),
            util.convert_x(x2),
            util.convert_y(y2),
        ],
        fill=color,
    )

    # draw pattern
    color = util.random_color()
    width = s.head_length
    height = s.head_height
    apply_pattern(x1, y1, s, monster_draw, width, height, color)
    return monster_draw


def get_left_arm(x, y, s, a, monster, monster_draw, color):
    y1 = y + s.head_height + random.randint(0, (s.body_height - s.arm_height))
    y2 = y1 + s.arm_height
    if monster.left_arm.direction == "straight":
        x1 = x + 0
        x2 = x1 + s.arm_length
        monster_draw.rectangle(
            [
                util.convert_x(x1),
                util.convert_y(y1),
                util.convert_x(x2),
                util.convert_y(y2),
            ],
            fill=color,
        )
    else:
        x1 = x + s.palm_length
        x2 = x1 + s.cut_arm_length
        monster_draw.rectangle(
            [
                util.convert_x(x1),
                util.convert_y(y1),
                util.convert_x(x2),
                util.convert_y(y2),
            ],
            fill=color,
        )
        px1 = x
        px2 = x1
        if monster.left_arm.direction == "downwards":
            py1 = y2
            py2 = py1 + s.palm_height
        else:
            py1 = y1 - s.palm_height
            py2 = y1
        monster_draw.rectangle(
            [
                util.convert_x(px1),
                util.convert_y(py1),
                util.convert_x(px2),
                util.convert_y(py2),
            ],
            fill=color,
        )

    # draw pattern
    color = util.random_color()
    width = s.arm_length
    height = s.arm_height
    apply_pattern(x1, y1, s, monster_draw, width, height, color)

    return monster_draw


def get_right_arm(x, y, s, a, monster, monster_draw, color):
    y1 = y + s.head_height + random.randint(0, (s.body_height - s.arm_height))
    y2 = y1 + s.arm_height
    x1 = x + s.arm_length + s.body_length
    if monster.right_arm.direction == "straight":
        x2 = x1 + s.arm_length
    else:
        x2 = x1 + s.cut_arm_length
        px1 = x1 + s.cut_arm_length
        px2 = px1 + s.palm_length
        if monster.left_arm.direction == "downwards":
            py1 = y2
            py2 = py1 + s.palm_height
            monster_draw.rectangle(
                [
                    util.convert_x(px1),
                    util.convert_y(py1),
                    util.convert_x(px2),
                    util.convert_y(py2),
                ],
                fill=color,
            )
        else:
            py1 = y1 - s.palm_height
            py2 = y1
        monster_draw.rectangle(
            [
                util.convert_x(px1),
                util.convert_y(py1),
                util.convert_x(px2),
                util.convert_y(py2),
            ],
            fill=color,
        )
    monster_draw.rectangle(
        [
            util.convert_x(x1),
            util.convert_y(y1),
            util.convert_x(x2),
            util.convert_y(y2),
        ],
        fill=color,
    )
    return monster_draw


def get_legs(x, y, s, a, monster, monster_draw, color):
    x1 = x + s.arm_length + s.body_length / 6
    x2 = x1 + s.leg_length
    y1 = y + s.head_height + s.body_height

    if monster.leg.direction == "front":
        y2 = y1 + s.leg_height
        monster_draw.rectangle(
            [
                util.convert_x(x1),
                util.convert_y(y1),
                util.convert_x(x2),
                util.convert_y(y2),
            ],
            fill=color,
        )
        x1 = x + s.arm_length + s.body_length / 6 * 4
        x2 = x1 + s.leg_length
        monster_draw.rectangle(
            [
                util.convert_x(x1),
                util.convert_y(y1),
                util.convert_x(x2),
                util.convert_y(y2),
            ],
            fill=color,
        )
    else:
        y2 = y + s.head_height + s.body_height + s.cut_leg_height
        monster_draw.rectangle(
            [
                util.convert_x(x1),
                util.convert_y(y1),
                util.convert_x(x2),
                util.convert_y(y2),
            ],
            fill=color,
        )
        x1 = x + s.arm_length + s.body_length / 6 * 4
        x2 = x1 + s.cut_leg_length
        monster_draw.rectangle(
            [
                util.convert_x(x1),
                util.convert_y(y1),
                util.convert_x(x2),
                util.convert_y(y2),
            ],
            fill=color,
        )
        if monster.leg.direction == "right":
            monster_draw.rectangle(
                [
                    util.convert_x(x2),
                    util.convert_y(y2),
                    util.convert_x(x2 + s.foot_length),
                    util.convert_y(y2 + s.foot_height),
                ],
                fill=color,
            )
            x1 = x + s.arm_length + s.body_length / 6
            x2 = x1 + s.leg_length
            monster_draw.rectangle(
                [
                    util.convert_x(x2),
                    util.convert_y(y2),
                    util.convert_x(x2 + s.foot_length),
                    util.convert_y(y2 + s.foot_height),
                ],
                fill=color,
            )

        elif monster.leg.direction == "left":
            monster_draw.rectangle(
                [
                    util.convert_x(x1 - s.foot_length),
                    util.convert_y(y2),
                    util.convert_x(x1),
                    util.convert_y(y2 + s.foot_height),
                ],
                fill=color,
            )
            x1 = x + s.arm_length + s.body_length / 6
            x2 = x1 + s.leg_length
            monster_draw.rectangle(
                [
                    util.convert_x(x1 - s.foot_length),
                    util.convert_y(y2),
                    util.convert_x(x1),
                    util.convert_y(y2 + s.foot_height),
                ],
                fill=color,
            )
    return monster_draw


def get_name(x, y, s, a, monster_draw, names, index):
    prefix = ""
    for i in names:
        if len(i) > len(prefix):
            prefix = i
    c = 1
    font = ImageFont.truetype("Arial.ttf", c)
    while font.getsize(prefix)[0] < a.monster_width:
        c += 1
        font = ImageFont.truetype("Arial.ttf", c)
    if font.getsize(prefix)[0] > a.monster_width:
        c -= 1
    x1 = x
    y1 = y + s.head_height + s.body_height + s.leg_height
    monster_draw.text(
        (util.convert_x(x1), util.convert_y(y1)), names[index], fill="black", font=font
    )
    return monster_draw


def apply_pattern(x, y, s, monster_draw, width, height, color):
    fill = color
    outline = util.random_color()
    number = random.randint(1, 4)
    i = 0
    while i < (number + 1):
        x1 = random.randint(x, (x + width - s.pattern_length))
        y1 = random.randint(y, (y + height - s.pattern_height))
        x2 = x1 + s.pattern_length
        y2 = y1 + s.pattern_height

        monster_draw.rectangle(
            [
                util.convert_x(x1),
                util.convert_y(y1),
                util.convert_x(x2),
                util.convert_y(y2),
            ],
            fill=fill,
            outline=outline,
            width=5,
        )
        i += 1
    return monster_draw

