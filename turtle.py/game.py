

import turtle
def funk1():
    tosh.forward(50)
def funk2():
    tosh.left(50)
def funk3():
    tosh.right(50)
def funk4():
    wn.bye()
def main():
    global tosh
    global wn
    wn=turtle.Screen()
    wn.setup(700,700)
    wn.title("Oddiy game ")
    wn.bgcolor("blue")
    tosh=turtle.Turtle()
    wn.onkey(funk1,"Up")
    wn.onkey(funk2,"Left")
    wn.onkey(funk3,"Right")
    wn.onkey(funk4,"q")
    wn.listen()
    wn.mainloop()
main()   
