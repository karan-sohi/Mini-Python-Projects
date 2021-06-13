from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 5
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():

    def __init__(self):
        self.turtles = []
        self.start()
        self.head = self.turtles[0]

    def start(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
 

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.turtles.append(new_segment)
        

    def move(self):
        for i in range(len(self.turtles) - 1, 0 , -1):
            new_x = self.turtles[i-1].xcor()
            new_y = self.turtles[i-1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.turtles[-1].position())


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)