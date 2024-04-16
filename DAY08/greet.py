# Simple Function
# def greet():
#     print("Hello ")
#     print("to")
#     print("everyone")
#greet()

# Funtion that allows parameters
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print("to")
#     print(f"How do you do {name}?")
# greet_with_name('Angela')


#Functions with multiple parameters
def greet_with(name,location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')
greet_with("Nowhere","Jack Bauer")
#greet_with("Jack Bauer", "Nowhere")


# Functions with keyword arguments
def greet_with(name,location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')
greet_with(location="Nowhere",name="Jack Bauer")