import math
import turtle
import random

window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic("images/background.png")
window.screensize(1200, 800)
# window.tracer(n=2)

BASE_X, BASE_Y = 0, -300


def calc_heading(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    length = (dx ** 2 + dy ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    if dy < 0:
        alpha = -alpha
    return alpha


def enemy_missiles():
    e_missile = turtle.Turtle(visible=False)
    pos_missile = random.randint(-600, 600)
    e_missile.speed(0)
    e_missile.color('red')
    e_missile.penup()
    e_missile.setpos(x=pos_missile, y=300)
    e_missile.pendown()
    target_angle = calc_heading(x1=pos_missile, y1=300, x2=BASE_X, y2=BASE_Y)
    print(target_angle)
    e_missile.setheading(target_angle)
    e_missile.showturtle()
    e_info = {'missile': e_missile, 'target': [BASE_X, BASE_Y],
              'state': 'launched', 'radius': 0}
    all_e_missiles.append(e_info)


def fire_missile(x, y):
    missile = turtle.Turtle(visible=False)
    missile.speed(0)
    missile.color('white')
    missile.penup()
    missile.setpos(x=BASE_X, y=BASE_Y)
    missile.pendown()
    heading = calc_heading(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    missile.setheading(heading)
    missile.showturtle()
    info = {'missile': missile, 'target': [x, y],
            'state': 'launched', 'radius': 0}
    our_missiles.append(info)


our_missiles = []
all_e_missiles = []

window.onclick(fire_missile)
i = 0
while i <= 5:
    enemy_missiles()
    i += 1


def explosive_logic(array_missiles):
    for info in array_missiles:
        state = info['state']
        missile = info['missile']
        if state == 'launched':
            missile.forward(4)
            target = info['target']
            if missile.distance(x=target[0], y=target[1]) < 20:
                info['state'] = 'explode'
                missile.shape('circle')
        elif state == 'explode':
            info['radius'] += 1
            if info['radius'] > 5:
                missile.clear()
                missile.hideturtle()
                info['state'] = 'dead'
            else:
                missile.shapesize(info['radius'])

    dead_missiles = [info for info in our_missiles if info['state'] == 'dead']
    for dead in dead_missiles:
        array_missiles.remove(dead)


while True:
    window.update()
    explosive_logic(our_missiles)
    explosive_logic(all_e_missiles)
