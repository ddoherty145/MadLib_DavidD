
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!
name = input("Enter a Name: ")
print( f"{name}, is a good name but it doesn't strike fear into the Empire's enemys." )
jesire_name = input("Give a name that people will FEAR: ")
print( f"{jesire_name}. I felt a shiver from just by uttering the name. Much better than {name}.")
name_city = input("Where are you from? Name a Fantasy City: ")
print( f"{name_city}. Yes, i've heard of it.")
month = input("Name a legendary person. Keep it to one word, mind you, we haven't the time to be needlessly pedantic: ")
adjective = input("One word to discribe yourself: ")
date = input("Pick a number between 1 - 30: ")
empire = input("Name an everyday item: ")

print( f"On the {date} day of {month} every living soul in the city of {name_city} was lost. \n Though the origin of this tragedy is unknown the Empire of {empire} issued a bounty on the reclamation of the lost city only ten days after the loss. \n Only those of the Jesire answered the call, for though they were few in number, they were the only ones with the power to handle with the corruption that had befallen {name_city}. \n It is hard to say how many of the Jesire answered the call, but one thing is certain, after three nights the Jesire that came out… came out heroes. \n Heed the tale of the {adjective} Jesire known as {jesire_name} at the time called {name}.")































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")