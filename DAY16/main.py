# from turtle import Turtle, Screen

# timmy = Turtle()
# #print(timmy)
# timmy.shape('turtle')
# timmy.color('green')
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
# CAlling methods from a CLASS
table.add_column("Pokemon Name",
['Pikachu','Squirtle','Charmander'])

table.add_column("Type",
['Electric','Water','Fire'])

#CHANGING A CLASS ATTRIBUTE
table.align = 'l'

print(table)
