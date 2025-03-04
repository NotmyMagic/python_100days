# from turtle import Turtle, Screen

# go = True

# tim = Turtle()
# print(tim)
# tim.shape("turtle")
# tim.color("Gray")


# my_screen = Screen()
# print(my_screen.canvheight)

# while go == True:
#     tim.forward(100)
#     tim.left(100)

# my_screen.exitonclick()


# python -m pip install PrettyTable
from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Minecraft mob", "main dimention", "main drop"]
table.add_row(["Creeper", "Overworld", "Gunpowder"])
table.add_row(["Enderman", "The End", "Ender pearl"])
table.align = "l"

print(table)