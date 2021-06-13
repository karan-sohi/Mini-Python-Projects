from turtle import Turtle, Screen
import random

screen = Screen()
turtle = Turtle()

screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_cor = 100
for i in range(len(colors)):
    tim = Turtle(shape = "turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-230, y_cor)
    y_cor -= 35

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

screen.exitonclick()