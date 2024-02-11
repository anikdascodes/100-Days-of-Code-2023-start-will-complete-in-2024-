name_string = "Alice, Bob, Charlie, Dana"

# The rest of your code
names = name_string.split(", ")

# print(names)

import random 

#Get the total number of items in list
num_items = len(names)
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")   
