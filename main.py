from turtle import Turtle, Screen
import random

# set the screen dimensions
screen = Screen()
screen.setup(width=500, height=400)


def game():

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_pos = [-60, -30, 0, 30, 60, 90]
    all_turtles = []

    # initialise  six rainbow-colored turtles
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-240, y=y_pos[turtle_index])
        all_turtles.append(new_turtle)

    # ask for input
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

    '''check if one of the turtles has reached the goal, if not let them race one step at random speed, if yes check 
    if the player has won or not and ask if they want to play again '''
    if user_bet:
        is_race_on = True

        while is_race_on:
            for turtle in all_turtles:
                if turtle.xcor() > 220:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet:
                        play_again = screen.textinput(title="Hurray! :)",
                                                      prompt=f"Your {winning_color} turtle wins! Hurray! \nPlay "
                                                             f"again? yes/no: ")
                    else:
                        play_again = screen.textinput("Don't cry!",
                                                      prompt=f"{winning_color} wins, you lose. \nPlay again? "
                                                             f"yes/no: ")
                    if play_again == "yes":
                        screen.clearscreen()
                        game()
                    else:
                        screen.bye()
                        return
                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)


game()

