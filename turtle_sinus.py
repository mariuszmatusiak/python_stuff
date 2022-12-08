####################################
# Copyright Mariusz Matusiak 2022
# Script for generating sinus and
# drawing using the turtle package.
# Used as an assignment in the
# Python Basics course.
# Usage:
# py -3 turtle_sinus.py
####################################
import turtle
import math

# Draw 1s of 10Hz sinus
T = 1 #1s
Fs = 1000 #1kHz sampling rate
F = 10 #5Hz sin
x = list(range(0, T*Fs)) #time samples
L = len(x)
y = [0] * len(x)
parameters = """
Signal parameters: T={}s, fs={}Hz, f={}Hz, N={}
where:
    T - signal period,
    fs - sampling frequency,
    f - signal frequency,
    N - number of samples.
""".format(T, Fs, F, L)
print(parameters)
for n in range(L): #generate output samples
    x[n] = x[n] / Fs
    y[n] = math.sin(2 * math.pi * F * x[n])
# Render screen
wn = turtle.Screen()
wn_height = wn.window_height()
wn_width = wn.window_width()
print("Screen size: {}x{}".format(wn_height, wn_width))
# Render X axis
xturtle = turtle.Turtle()
xturtle.speed(5)
xturtle.penup()
xturtle.goto(-wn_width/2,0)
xturtle.pendown()
xturtle.forward(wn_width)
# Render Y axis
yturtle = turtle.Turtle()
xoffset = 5
yturtle.speed(5)
yturtle.penup()
yturtle.left(90)
yturtle.goto(-wn_width/2+xoffset,-wn_height/2)
yturtle.pendown()
yturtle.forward(wn_height)
# Render y
graphturtle = turtle.Turtle()
graphturtle.speed(20)
graphturtle.pencolor("red")
graphturtle.penup()
graphturtle.goto(-wn_width/2+xoffset,0)
graphturtle.pendown()
xscale = wn_width/T
yscale = wn_height/2
for n in range(L):
    graphturtle.goto(-wn_width/2+xoffset + x[n] * xscale, y[n] * yscale)
