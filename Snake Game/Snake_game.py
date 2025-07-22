from turtle import Turtle, Screen
import time
import random

WIDTH = 600
HEIGHT = 600
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game - Nokia Style")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

head = segments[0]

food = Turtle("circle")
food.penup()
food.color("red")
food.speed("fastest")
food.shapesize(0.5, 0.5)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

score = 0
score_display = Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))

def up():
    if head.heading() != DOWN:
        head.setheading(UP)

def down():
    if head.heading() != UP:
        head.setheading(DOWN)

def left():
    if head.heading() != RIGHT:
        head.setheading(LEFT)

def right():
    if head.heading() != LEFT:
        head.setheading(RIGHT)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for i in range(len(segments) - 1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)
    head.forward(MOVE_DISTANCE)

    if head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))

    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        game_is_on = False
        score_display.goto(0, 0)
        score_display.write("GAME OVER", align="center", font=("Courier", 24, "bold"))

    for segment in segments[1:]:
        if head.distance(segment) < 10:
            game_is_on = False
            score_display.goto(0, 0)
            score_display.write("GAME OVER", align="center", font=("Courier", 24, "bold"))

screen.mainloop()