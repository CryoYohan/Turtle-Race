from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.title('Turtle Race!')
screen.setup(500, 400)
screen.bgcolor('olive drab')

user_bet = ""
is_racing_on = False
turtles = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

def create_turtles() -> None:
    global turtles, user_bet
    user_bet = screen.textinput(title="Which turtle color do you think will win?", prompt="Enter turtle color: ")
    for color in colors:
        tim = Turtle(shape='turtle')
        tim.color(color)
        tim.penup()
        turtles.append(tim)

def align_turtles() -> None:
    global turtles
    y_cor = -150
    for turtle in turtles:
        turtle.goto(x=-230,y=y_cor)  # Align turtles at the starting line
        y_cor += 50

def start_race()->None:
    global user_bet, is_racing_on, turtles
    if user_bet: is_racing_on = True
    while is_racing_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_racing_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The winning color is {winning_color}")
                else:
                    print(f"You've lost! The winning color is {winning_color}")
            else:
                rand_distance = randint(0, 10)
                turtle.forward(rand_distance)


def main() -> None:
    create_turtles()
    align_turtles()
    start_race()

if __name__ == "__main__":
    main()
    screen.exitonclick()


