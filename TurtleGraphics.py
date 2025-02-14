#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides): 
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def fillCorner(alice, corner): 
    drawSquare(alice, 100)
    if corner == 1: 
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 3:
        alice.forward(100)
        alice.right(90)
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 4:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    
def squaresInSquares(jawn, num):
    jawn.up()
    jawn.goto(-150,150)
    jawn.down()
    drawSquare(jawn, 300)
    for n in range(num):
        jawn.right(45)
        jawn.up()
        jawn.forward(30)
        jawn.down()
        jawn.left(45)
        drawSquare(jawn, 250)
        
    
def main():
    myTurtle = turtle.Turtle()
    #drawSquare(myTurtle, size) 
    #drawPolygon(myTurtle, 9) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 4) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
