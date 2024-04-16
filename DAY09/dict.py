programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

#adding new items to dictionary
programming_dictionary["Loop"]="The action of doing something over and over again"

# Create empty dictionary
empty_dictionary= {}

#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary "KEYS"
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting a List in a Dictionary
capitals = {
    "France":"Paris",
    "Germany":"Berlin",
}

travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France" : {"cities_visited" : ["Paris","Lille","Dijon"], "total_visits": 12},
    "Germany": {"cities_visited" :["Berlin", "Hamburg", "Stuttgart"], "total_visits": 4},
}

# Nesting a Dictionary in a List
travel_log = [
    {
    "country": "France",
    "cities_visited" : ["Paris","Lille","Dijon"], 
    "total_visits": 12
    },

    {
    "country":"Germany", 
    "cities_visited" :["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 4
    },
]

def add_new_country(country, visits, list_of_cities):
  travel_log.append({"country":country,"visits":visits, "cities":list_of_cities})