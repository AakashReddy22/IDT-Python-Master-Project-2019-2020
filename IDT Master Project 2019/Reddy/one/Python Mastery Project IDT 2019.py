'''
Name: Aakash Reddy
Assignment: Mastery Project
Class: Cowart
Date Created: 4/20/2019
Date last edited: 5/1/2019
Period: 1st
'''
import math
from turtle import *
from km_mi import miles
from ft_m import meters
from km_ly import lightyears
from january import jan20feb18
from february import feb18mar20
from march import mar20apr20
from april import apr20may21
from may import may21jun21
from june import jun21jul23
from july import jul23aug23
from august import aug23sep23
from september import sep23oct23
from october import oct23nov22
from november import nov22dec22
from december import dec22jan20
def measurements():
    print("Hey kid. The code you are about to read will have all the information needed to understand our galaxy to the highest level")
    # Please click out of turtle when the orbits of the planet have completed
    print("Before we get into the good stuff, we need to understand out units")
    print("And because space is international territory, we must understand metric units, so these modules may come in handy")
    print("Which function would you like to use today?")
    print("a. Kilometers to Miles")
    print("b. Feet to Meters")
    print("c. Kilometers to Light years")
    ans = input()
    if (ans == "a"):
        miles()
    if (ans == "b"):
        meters()
    if (ans == "c"):
        lightyears()
    print("Our past missions to Venus have been quite succesful, but more information is required in order to safely claim that venus can support life")
def birthdays():
    print("We first need to know your birth month in order to tell you your zodiac sign. As well as astronauts that were born on your birthday")
    print("type the letter that your birthday falls into from the provided dates")
    print("d. January 20th - Feburary 18th")
    print("e. February 18th - March 20th")
    print("f. March 20th - April 20th")
    print("g. April 20th - May 21st")
    print("h. May 21st - June 21st")
    print("i. June 21st - July 23rd")
    print("j. July 23rd - August 23rd")
    print("k. August 23rd - September 23rd")
    print("l. September 23rd - October 23rd")
    print("m. October 23rd - November 22nd")
    print("n. November 22nd - December 22nd")
    print("o. December 22nd - January 20th")
    ans = input()
    if (ans == "d"):
        jan20feb18()
    if (ans == "e"):
        feb18mar20()
    if (ans == "f"):
        mar20apr20()
    if (ans == "g"):
        apr20may21()
    if (ans == "h"):
        may21jun21()
    if (ans == "i"):
        jun21jul23()
    if (ans == "j"):
        jul23aug23()
    if (ans == "k"):
        aug23sep23()
    if (ans == "l"):
        sep23oct23()
    if (ans == "m"):
        oct23nov22()
    if (ans == "n"):
        nov22dec22()
    if (ans == "o"):
        dec22jan20()
    
    
print("Ok kid we are in some big trouble. Our most experienced crew of pilots are currently unavailable as it is their downtime. We have just got evidence that Earth is crumbling at a rate of 5 miles per hour")
print("We need to see if we can survive in alternate habitats seperate from earth")
print("And lucky for you, sarge has chosen you to be our researcher for the project.")
print(" Mission: Create a simulation of the orbits of Venus and Earth")
print(" Time: 5 days")
print(" Urgency: EXTREME")
G = 6.67428e-11    # Yes It has to be that small because we are putting the orbits of planets onto a 13 inch screen.
AU = (149.6e6 * 1000)    # 149.6 million kilometers
SCALE = 250 / AU    # Scaled down 250 times to fit on my screen
print("Okay kid, we are a bit short on time. We cannot inform you of all the galaxies and planets. We have decided to improvise and show you the orbits of venus ad earth")
print("With this information, you will understand the crucial information needed to visit these planets and how much faster venus is than earth")
class Body(Turtle):
    name = 'Body'
    mass = None
    vx = vy = 0.0
    px = py = 0.0
    
    def attraction(self, other):
        """(Body): (fx, fy)

        Returns the force exerted upon this body by the other body.
        """
        if self is other:
            raise ValueError("Attraction of object %r to itself requested" % self.name)

        # Getting the distance of the other body.
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
        d = math.sqrt(dx**2 + dy**2)
        if d == 0:
            raise ValueError("Collision between objects %r and %r" % (self.name, other.name))
        # The force of attraction   
        f = G * self.mass * other.mass / (d**2)

        # This part of the program finds the direction of the force.
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy

def update_info(step, bodies):
    print('Step #{}'.format(step))
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(body.name, body.px/AU, body.py/AU, body.vx, body.vy)
        print(s)
    print()
def loop(bodies):
    """([Body])

    Never returns; loops through the simulation, updating the
    positions of all the provided bodies.
    """
    timestep = 24*10000  # This will increase the distance between the points to speed up the process of placing the dots
    
    for body in bodies:
        body.penup()
        body.hideturtle()

    step = 1
    while True:
        update_info(step, bodies)
        step += 1

        force = {}
        for body in bodies:
            total_fx = total_fy = 0.0
            for other in bodies:
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy

            # Recording the total force exerted on the body
            force[body] = (total_fx, total_fy)

        # Updating the positions
        for body in bodies:
            fx, fy = force[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep

            # Updated positions
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px*SCALE, body.py*SCALE)
            body.dot(3)

def main():
    measurements()
    birthdays()
    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30
    sun.pencolor('yellow')

    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1*AU
    earth.vy = 29.783 * 1000            # 29.783 kilometers/sec or 18.506 miles per second
    earth.pencolor('blue')

    venus = Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000
    venus.pencolor('red')

    loop([sun, earth, venus])

if __name__ == '__main__':
    main()
