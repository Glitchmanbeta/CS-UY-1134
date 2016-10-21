import turtle
import math
import random

class Sun:

    def __init__(self, center, size, color):
        self.center = center
        self.size = size
        self.color = color

    def draw(self):
        
        turtle.tracer(0,0)
        turtle.penup()
        turtle.goto(self.center)
        turtle.dot(self.size, self.color)

    def getSize(self):
        return self.size

class Planet(Sun):

    def __init__(self, orbitAround, orbitRadius, size, color, speed):
        self.orbitAround = orbitAround
        self.orbitRadius = orbitRadius
        self.speed = speed
        self.angle=0
        super().__init__(self.calculateCenter(),size,color)

    def calculateCenter(self):
        return [x+self.orbitRadius*f(self.angle)
              for x,f in zip(self.orbitAround.center, (math.sin,math.cos))]

    def move(self):
        self.angle+=self.speed
        self.center=self.calculateCenter()

    def getOrbitRadius(self):
        return self.orbitRadius

class SolarSystem:
    def __init__(self, sun, planet, moon):
        self.sun = sun
        self.planet = planet
        self.moon = moon

    def draw(self):
        self.sun.draw()
        for i in self.planet:
            i.draw()
            i.move()
        for j in self.moon:
            j.draw()
            j.move()

def randomColor():
    """Code is not used here but you may find it usefull"""
    return [random.random() for i in range(3)]

#Make the number of planets random and figure out how to calculate the orbit radius
sun = Sun((random.randint(0, 100), random.randint(0,100)), random.randint(50, 100), randomColor())
planets = []
moons = []

for i in range(random.randint(1, 5)):
    planets.append(Planet(sun, random.randint(sun.getSize() // 2 + 20, 200), random.randint(25, 50), randomColor(), 0.01))

for i in range(random.randint(1, 10)):
    moons.append(Planet(planets[i], planets[i].getOrbitRadius() - sun.getSize() // 2 - 20, random.randint(1, 25), randomColor(), 0.05))

s = SolarSystem((sun), planets,moons)



def drawPlanet(center,size,color,orbitRadius,angle):
    location=[x+orbitRadius*f(angle)
              for x,f in zip(center, (math.sin,math.cos))] #Some trig to compute the location
    turtle.penup()
    turtle.goto(*location)
    turtle.dot(size*2,color) #dot takes diameter rather than radius


def draw():
    """This draw function will be repeatedly called"""
    """turtle.clear() 
    turtle.tracer(0,0) #This speeds things up
    turtle.penup()
    turtle.goto(0,0)
    turtle.dot(100,"yellow")
    drawPlanet( (0,0), 30, "Blue", 200, angle) #Replace this with your code to draw"""
    turtle.clear()
    s.draw()
    global angle #Python requires this to change a global variable
    angle+=0.01 
    screen.ontimer(draw,0) #This tells the system to call this function again as soon as possible

angle=0 
turtle.tracer(0,0)
turtle.ht() 
screen=turtle.Screen() #Needed for the following
screen.onkey(turtle.bye,"q") #quits if you press q
screen.ontimer(draw,0) #Tells the system to call draw. Don't call it directly
screen.listen() 
turtle.mainloop()
