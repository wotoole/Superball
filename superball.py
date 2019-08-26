'''
Liam O'Toole
superball.py
models a bouncing superball on an incline without air resistance
7 October, 2014
'''

#import libraries
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, tan, pi

#define initial conditions
g = 9.81
h = input("Enter the initial height of the ball: ")
theta = 30*pi/180   #converted to radians
v = sqrt(2*g*h)     #get the initial speed of the ball at the incline
vx = 0.0
vy = -v
x = 0.0
y = 0.0
t = 0.0
dt = 0.01

while t < 30:

    ay = -g
    vy = vy + ay*dt
    vx = vx
    y = y + vy*dt
    x = x - vx*dt

    y_incline = x*tan(theta)

    if y <= y_incline:
        v = sqrt(vx**2 + vy**2)
        vx = v*cos(theta)
        vy = v*sin(theta)
    t = t + dt
    plt.plot(x,x*tan(theta), 'c_')
    plt.plot(x,y, 'k.')
    plt.xlabel("Position (x)")
    plt.ylabel("Position (y)")
    plt.title("Superball Bounce on Incline")


plt.show()

'''
with air resitance
'''
#import libraries
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, tan, pi

#define initial conditions
g = 9.81
h = input("Enter the initial height of the ball: ")
theta = 30*pi/180   #converted to radians
v = sqrt(2*g*h)     #get the initial speed of the ball at the incline
vx = 0.0
vy = -v
vt = 9.0
x = 0.0
y = 0.0
t = 0.0
dt = 0.01

while t < 10:

    ay = -g*(1 + vy/vt)
    ax = -g*(vx/vt)
    vy = vy + ay*dt
    vx = vx + ax*dt
    y = y + vy*dt
    x = x - vx*dt

    y_incline = x*tan(theta)

    if y <= y_incline:
        v = sqrt(vx**2 + vy**2)
        vx = v*cos(theta)
        vy = v*sin(theta)
    t = t + dt
    plt.plot(x,x*tan(theta), 'c_')
    plt.plot(x,y, 'k.')
    plt.xlabel("Position (x)")
    plt.ylabel("Position (y)")
    plt.title("Ping Pong Ball Bounce on Incline")


plt.show()

'''
with air resistance
'''
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, tan, pi

#define initial conditions
g = 9.81
h = input("Enter the initial height of the ball: ")
theta = 30*pi/180   #converted to radians
v = sqrt(2*g*h)     #get the initial speed of the ball at the incline
vx = 0.0
vy = -v
vt = 9.0
x = 0.0
y = 0.0
t = 0.0
dt = 0.01

while t < 10:

    ay = -g*(1 + vy/vt)
    ax = -g*(vx/vt)
    vy = vy + ay*dt
    vx = vx + ax*dt
    y = y + vy*dt
    x = x - vx*dt

    y_incline = x*tan(theta)

    if y <= y_incline:
        print"new bounce"
        v = sqrt(vx**2 + vy**2)
        vx = v*cos(theta)
        vy = v*sin(theta)
    t = t + dt
    plt.plot(x,x*tan(theta), 'c_')
    plt.plot(x,y, 'k.')
    plt.xlabel("Position (x)")
    plt.ylabel("Position (y)")
    plt.title("Ping Pong Ball Bounce on Incline")


plt.show()

