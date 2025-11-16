
#import turtle
#screen = turtle.Screen()
#screen.bgcolor("Orange")
#screen.setup(400, 300)
#screen.title("Welcome to my first turtle program")
#board = turtle.Turtle()
#for i in range(4):
#    board.forward(100)
#    board.left(90)



#import turtle
#turtle.Screen().bgcolor("pink")
#board = turtle.Turtle()
#board.forward(100)   #base line

#board.left(120)
#board.forward(100)

#board.left(120)
#board.forward(100)

#board.penup()
#board.right(150)
#board.forward(50)

#board.pendown()
#board.right(90)
#board.forward(100)

#board.right(120)
#board.forward(100)

#board.right(120)
#board.forward(100)

#turtle.done()


import turtle
t= turtle.Turtle()
s= turtle.Screen()
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
s.bgcolor("black")
t.speed('fastest')
t.hideturtle()
while True:
  for x in range(200):
    t.pencolor(colors[x%len(colors)])
    t.width(x/100+1)
    t.forward(x)
    t. left(59)
  t.right(239)
  for x in range(200, 0, -1):
    t.pencolor('black')
    t.width(x/100+7)
    t.forward(x)
    t.right(59)