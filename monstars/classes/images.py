from classes import utilities as util
import random
from PIL import Image, ImageDraw

def get_body(x, y, s, a, monster_draw):
	x1 = (x + s.arm_length) * a.ph
	y1 = (y + s.head_height) * a.pv
	x2 = x1 + s.body_length * a.ph 
	y2 = y1 + s.body_height * a.pv
	monster_draw.rectangle([x1,y1,x2,y2], fill = util.random_color()) 
	return monster_draw

def get_head(x, y, s, a, monster, monster_draw, color):
	y1 = (y + 0) * a.pv
	y2 = y1 + s.head_height * a.pv
	if monster.head.direction == 'left':
		x1 = (x + s.arm_length) * a.ph
		x2 = x1 + s.head_length * a.ph
	elif monster.head.direction == 'right':
		x1 = (x + s.arm_length + (s.body_length-s.head_length))   * a.ph
		x2 = x1 + s.head_length * a.ph
	elif monster.head.direction == 'front':
		x1 = (x + s.arm_length + (s.body_length/2 - s.head_length /2)) * a.ph
		x2 = x1 + s.head_length * a.ph
	monster_draw.rectangle([x1,y1,x2,y2], fill = color)
	return monster_draw

def get_left_arm(x,y,s,a,monster, monster_draw, color):
	y1 = (y + s.head_height + random.randint(0, (s.body_height - s.arm_height)* a.pv) ) * a.pv
	y2 = y1 + s.arm_height * a.pv
	if monster.left_arm.direction == 'straight':
		x1 = (x +0) * a.ph
		x2 = x1 + s.arm_length *a.ph
		monster_draw.rectangle([x1,y1,x2,y2], fill = color)
	else:
		x1 = (x + s.palm_length) * a.ph
		x2 = x1 + s.cut_arm_length * a.ph
		monster_draw.rectangle([x1,y1,x2,y2], fill= color)
		px1 = x * a.ph
		px2 = x1
		if monster.left_arm.direction == 'downwards':
			py1 = y2
			py2 = py1 + s.palm_height * a.pv
		else:
			py1 = y1 -s.palm_height * a.pv
			py2 = y1
		monster_draw.rectangle([px1,py1,px2,py2], fill = color)
	return monster_draw

def get_right_arm(x,y,s,a,monster, monster_draw, color):
	y1 = (y + s.head_height + random.randint(0, (s.body_height - s.arm_height)* a.pv) ) * a.pv
	y2 = y1 + s.arm_height * a.pv
	x1 = (x + s.arm_length + s.body_length) * a.ph
	if monster.right_arm.direction == 'straight':
		x2 = x1 + s.arm_length *a.ph
	else: 
		x2 = x1 + s.cut_arm_length *a.ph
		px1 = x1 + s.cut_arm_length * a.ph
		px2 = px1 + s.palm_length *a.ph	
		if monster.left_arm.direction == 'downwards':
			py1 = y2 
			py2 = py1 + s.palm_height *a.pv
			monster_draw.rectangle([px1, py1, px2, py2], fill = color)
		else:
			py1 = y1 -s.palm_height * a.pv
			py2 = y1
		monster_draw.rectangle([px1, py1, px2, py2], fill = color)
	monster_draw.rectangle([x1,y1,x2,y2], fill = color)
	return monster_draw

def get_legs(x,y,s,a,monster, monster_draw, color): 
	x1 = (x + s.arm_length + s.body_length /6 )* a.ph
	x2 = x1 + s.leg_length * a.ph
	y1 = (y + s.head_height+ s.body_height) * a.pv 

	if monster.leg.direction == 'front':
		y2 = y1 + s.leg_height *a.pv
		monster_draw.rectangle([x1, y1, x2, y2], fill = color)
		x1 = (x + s.arm_length + s.body_length /6* 4 )* a.ph
		x2 = x1 + s.leg_length * a.ph
		monster_draw.rectangle([x1, y1, x2, y2], fill = color)
	else:
		y2 = (y + s.head_height+ s.body_height + s.cut_leg_height)* a.pv
		monster_draw.rectangle([x1, y1, x2, y2],fill = color )
		x1 = (x + s.arm_length + s.body_length /6* 4 )* a.ph
		x2 = x1 + s.cut_leg_length * a.ph
		monster_draw.rectangle([x1, y1, x2, y2],fill = color )
		if monster.leg.direction == 'right':
			monster_draw.rectangle([x2, y2, x2 + s.foot_length*a.ph, y2+ s.foot_height* a.pv], fill= color )
			x1 = (x + s.arm_length + s.body_length /6 )* a.ph			
			x2 = x1 + s.leg_length * a.ph
			monster_draw.rectangle([x2, y2, x2 + s.foot_length*a.ph, y2+ s.foot_height* a.pv], fill= color )

		elif monster.leg.direction == 'left': 
			monster_draw.rectangle([x1 - s.foot_length*a.ph, y2, x1, y2+ s.foot_height* a.pv], fill= color )
			x1 = (x + s.arm_length + s.body_length /6 )* a.ph
			x2 = x1 + s.leg_length * a.ph
			monster_draw.rectangle([x1 - s.foot_length*a.ph, y2, x1, y2+ s.foot_height* a.pv], fill= color )
	return monster_draw

def get_name(x,y,s,a, monster_draw):
	names =  []
	return monster_draw
