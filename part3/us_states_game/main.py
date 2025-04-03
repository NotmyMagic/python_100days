import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./part3/us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("./part3/us_states_game/50_states.csv")
guessed_states = []
states = data.state.to_list()


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the state {len(guessed_states)}/50", prompt="What is a states name?").title()


    if answer_state == "Exit":
        # missing_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./part3/us_states_game/states_to_learn.csv")
        break

    elif answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.teleport(state_data.x.item(), state_data.y.item())
        t.write(answer_state)









screen.exitonclick()