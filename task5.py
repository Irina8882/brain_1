import turtle
import random

colors = ['black', 'blue', 'magneta', 'cyan']


def get_random_color():
    return random.choice(colors)

brain = turtle.Pen()
brain.color(get_random_color(), get_random_color())
brain.width(7)
brain.fd(100)

input()