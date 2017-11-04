def star(t, distance, side):
    t.begin_fill()
    for times in range(side):
        t.forward(distance)
        t.left(144)
    t.end_fill()
     
def polygon(t, distance, side):
    
    angle = 360/side
    t.begin_fill()
    for times in range(side):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def move(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def bLT(t,x,y):
    t.begin_fill()
    
    t.color(255,252,119)
    angle = 120
    t.penup()
   
    t.goto(x,y)
 
    t.pendown()

    t.left(angle)
    t.forward(50)
    t.right(angle)
    t.forward(25)
    t.left(angle)
    t.forward(50)
    t.right(angle)
    t.forward(25)
    t.left(angle)
    t.forward(90)

    t.left(angle+40)
    t.forward(60)
    t.right(100)
    t.forward(25)
    t.left(angle)
    t.forward(50)
    t.right(angle)
    t.forward(25)
    t.left(angle+12)
    t.forward(90)
    
    t.end_fill()
