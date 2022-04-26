
import turtle
turtle.bgcolor("black")

squary = turtle.Turtle()
squary.speed(25)
squary.pencolor("red")
for i in range(600):
    squary.forward(i)
    squary.left(56)
turtle.done()







# import time
# from turtle import*
# pen=Turtle()
# pen.color('red')
# bgcolor('black')
# def curve():
#     for i in range(200):
#         pen.right(1)
#         pen.forward(1)
#         pen.speed(120)
# def draw_heart():
#     pen.fillcolor('red')
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(113)
#     curve()
#     pen.left(120)
#     curve()
#     pen.forward(112)
#     pen.end_fill()
# def draw_txt():
#     pen.up()
#     pen.setpos(-50, 90)
#     pen.down()
#     pen.color('black')
#     pen.write("", font=("Montserrat", 16, "bold"))
#     pen.up()
#     pen.setpos(-70, 70)
#     pen.down()
#     time.sleep(1)
# draw_heart()
# draw_txt()
# pen.ht()
# done()  









# import turtle
# t=turtle.Turtle()
# t.speed(100)
# turtle.bgcolor("black")
# for i in range(200):
#     t.color("cyan")
#     t.circle(i)
#     t.left(10)
# turtle.done()  








# import turtle 
# screen = turtle.Screen()
# screen.setup(550,600, startx=0, starty=100)
# t=turtle.Turtle()
# turtle.bgcolor('black')
# turtle.color('green')
# turtle.speed(10)
# turtle.right(45)
# for i in range(150):
#     turtle.circle(25)
#     if 7<i<62:
#         turtle.left(5)
#     if 80<i<133:
#         turtle.right(5)
#     if i<80:
#         turtle.forward(10)
#     else:
#         turtle.forward(5)
# turtle.done()











# import turtle
# turtle.bgcolor("black")
# turtle.pensize(2)
# turtle.speed(0)
# for i in range(6):
#     for colours in ['red','magenta','blue','cyan','green','yellow','white']:
#         turtle.color(colours)
#         turtle.circle(100)
#         turtle.left(10)

# turtle.done()




# import turtle
# turtle.speed(0)
# turtle.bgcolor("black")
# turtle.color('red','green')
# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.left(170)
#     if abs(turtle.pos())<1:
#         break
# # turtle.end()
# turtle.done()


