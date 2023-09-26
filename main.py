from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
user_bet = None
screen.setup(width=500, height=400)

while is_race_on is False:
    user_bet = screen.textinput(title='Make you bet.', prompt='Which turtle will win the race?\n'
                                                              '(red/orange/yellow/green/blue/purple)\n Enter a color: ')
    if user_bet in colors:
        is_race_on = True
        break

y_pos = -100
for turtle in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += 40
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You`ve won! The {winning_color} turtle is the winner!')
            else:
                print(f'You`ve lost! The {winning_color} turtle is the winner!')
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
