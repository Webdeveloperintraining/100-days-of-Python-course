################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope
def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()

#global scope

# player_health =10

# def drink_potion2():
#   potion_strength = 2
#   print(player_health)

# drink_potion2()

#THERE is no Block Scope in PYTHON

game_level = 3
enemeies = ["Skeleton", "Zombie", "Alien"]

# For example variables inside if statments are count as global variables if not inside a function
# def create_enemy():
#   if game_level > 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# Modyfying the Global Scope

#Bad Practice
# enemies = 1
# def increase_enemies():
#   global enemies
#   enemies+=1
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Widespread aproved way
# enemies = 1
# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies +  1

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Global Constants
#Python conventions to global variables is to make variables be uppercase
PI = 3.14159