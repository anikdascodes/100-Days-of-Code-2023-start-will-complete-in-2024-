import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
tim.speed(1)

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

t.done()