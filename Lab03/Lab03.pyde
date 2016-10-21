#If the "g" key is pressed, the tree will grow larger or smaller depending on the position of the mouse. (mouseY)
import sys
import random
import math

leafcount = 0
def setup():
    size(1100, 800)
    background(255)
    pixelDensity(displayDensity())
    global leafcount
    leafcount = 0

def drawLineAngle(color, start, angle, length, width=1):
    angle += 180  # make up zero degrees
    end = (start[0] + math.sin(math.radians(angle)) * length,
           start[1] + math.cos(math.radians(angle)) * length)
    stroke(*color)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end

def drawLeaf(location, radius):
        global leafcount
        stroke(0, 50, 0)
        fill(100, 255, 100)
        strokeWeight(0.5)
        ellipse(location[0],location[1],radius, radius)
        fill(0, 0, 0)
        textAlign(CENTER, CENTER)
        text(leafcount, location[0], location[1])
        leafcount += 1

def drawTree(start,leaf):
        end = drawLineAngle((255,0,0),start,0,300)
        endL = drawLineAngle((0,255,255),end,25,300)
        endR = drawLineAngle((0,0,255),end,-25,300)
        if leaf:
            drawLeaf(endL)
            drawLeaf(endR)        

def drawRecTree(start, leaf):
    if(grow):
        drawHelpTree(start, leaf, 0, 12, 800 - mouseY, (800 - mouseY) / 5)
    else:
        drawHelpTree(start, leaf, 0)
    if leaf:
        drawLeaf(start, 13)
    
def drawHelpTree(start, leaf, angle, counter = 12, length = 100, width = 13):
    global leafcount
    global x
    end = drawLineAngle((0, 0, 0), start, angle , length, width)
    if counter == 0:
        if leaf:
            drawLeaf(end, 13)
        return None
    else:
        if(x < 0):
            drawHelpTree(end, leaf, angle + 25 - (x / 22), counter - 1, (length / 2) + 5, (width / 3) + 1)
            drawHelpTree(end, leaf, angle - 25 - (x / 22), counter - 1, (length / 2) + 5, (width / 3) + 1)
        if(x >= 0):
            drawHelpTree(end, leaf, angle + 25 - (x / 22), counter - 1, (length / 2) + 5, (width / 3) + 1)
            drawHelpTree(end, leaf, angle - 25 - (x / 22), counter - 1, (length / 2) + 5, (width / 3) + 1)
        if leaf:
            drawLeaf(end, 13)
            
def keyPressed():
    global leaf
    global grow
    if key == "g":
        grow = not grow
    if key=="l":
        leaf = not leaf

def setup():
    global leaf
    global grow
    leaf= False
    grow = False

def draw():
    global leafcount
    global x
    x = mouseX - 550
    clear()
    background(255)
    leafcount = 0
    drawRecTree((550,800), leaf)