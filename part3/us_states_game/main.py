import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./part3/us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("./part3/us_states_game/50_states.csv")

number_of_states = len(data)
guessed_states = 0

states = data.state.to_list()


while number_of_states > 0:
    answer_state = screen.textinput(title=f"Guess the state {guessed_states}/50", prompt="What is a states name?").title()
    print(number_of_states)
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.teleport(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        number_of_states -= 1
        guessed_states += 1






screen.exitonclick()