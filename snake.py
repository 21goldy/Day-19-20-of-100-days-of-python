from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FONT = ("Courier New", 25, "normal")
CENTER = 'center'


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in positions:
            self.add(position)

    def add(self, position):
        goldy = Turtle('square')
        goldy.color('white')
        goldy.penup()
        goldy.goto(position)
        self.snake_body.append(goldy)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()

        self.create_snake()
        self.head = self.snake_body[0]

    def grow_snake(self):
        self.add(self.snake_body[-1].position())

    def snake_length(self):
        for move in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[move - 1].xcor()
            y = self.snake_body[move - 1].ycor()
            self.snake_body[move].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

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
