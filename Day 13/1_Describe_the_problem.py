############DEBUGGING#####################

# Describe Problem
def my_function():
    for i in range(1, 20):
        if i == 20:  # here i will not call 20 because it will go 1 to before 20 means 19 only
            print("You got it")


my_function()

# Reproduce the Bug
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1,
                   6)  # here as the index number counted so the last index will be 5 , so if we give last index as 6 will will give out of range, so if we want to fix this error we can start index 0 position to last inddex  index position
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print(
        "You are a Gen Z.")
# here if user select 1980 or 1994 they will not get any result so to solve it we can use <= or >= so that we can cover all the year

"""# Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")"""
# here is the solution of Fix the Errors:
# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # here word oer page have == so the word per page is not defined it use the previous value word per page = 0
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item) # here should give an indentation
  print(b_list)

mutate([1,2,3,5,8,13])
