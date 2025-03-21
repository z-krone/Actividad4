"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Aumentar la velocidad del proyectil
        speed.x = (x + 200) / 5  # Cambiado para aumentar la velocidad horizontal
        speed.y = (y + 200) / 5  # Cambiado para aumentar la velocidad vertical


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 2  # Aumentado para que los objetivos se muevan más rápido

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    
    # Reposicionar objetivos que salen de la pantalla
    for target in targets:
        if target.x < -210:  # Si un objetivo se sale de la pantalla por la izquierda
            target.x = 210  # Lo reubica en el lado derecho

    # Reposicionar el balón cuando sale de la pantalla
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = 0
        speed.y = 0

    ontimer(move, 30)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
