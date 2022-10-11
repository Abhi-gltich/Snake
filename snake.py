from turtle import Turtle
POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.seg = []
        self.create()
        self.head = self.seg[0]

    def create(self):
        for postition in POS:
            """Creating Snake"""
            self.add_segment(postition)

    def add_segment(self, postition):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(postition)
        self.seg.append(body)

    def extend(self):
        self.add_segment(self.seg[-1].position())

    def move(self):
        """Formating Snake #Aligning them while moving"""
        for num in range(len(self.seg)-1, 0, -1):
            new_x = self.seg[num - 1].xcor()
            new_y = self.seg[num - 1].ycor()
            self.seg[num].goto(new_x, new_y)

        self.seg[0].fd(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for x in self.seg:
            x.goto(3000, 3000)
        self.seg.clear()
        self.create()
        self.head = self.seg[0]
