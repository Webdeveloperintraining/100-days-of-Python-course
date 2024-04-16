#functions with Outputs
def format_name(f_name,l_name):
    """ Take a first and last name and format it to return
    the title case version of the name """

    if f_name== "" or l_name == "":
        return "Provide Valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

format_string = format_name('AnGeLa','YU')
print(format_string)

#Recursive Funtion
def calculator():
    print("aaaaaargh")
    calculator()

# DON't RUN THIS INFINITE LOOP
#calculator()