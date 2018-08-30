from turtle import *

t = Turtle()
t.screen.bgcolor("black")
colors=["red","yellow","purple"]
t.screen.tracer(0,0)

for x in range(100):
    t.circle(x)
    t.color(colors[x%3])
    t.left(100)

def curvemove():
    for i in range(200):
        right(1)
        forward(1)
t.fillcolor("white")
color("white")
t.write("Love u",align="left",font=("Arial",60,"normal"))
color('red','red')
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()

t.screen.exitonclick()
t.screen.mainloop()
