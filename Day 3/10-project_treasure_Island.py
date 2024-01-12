print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')


print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choose_your_direction = input("Where you want to go? Left or Right").lower()
if choose_your_direction == "left":
    print("Congrats You Complete Level 1 Start your next journey")

    choose_your_decision = input("What You Want to do?Swim or Wait?").lower()
    if choose_your_decision == "wait":
        print("Congrats You Complete Level 2 Start your next journey")
        choose_your_door = input("Which door you want to select? Red, Blue, Yellow").lower()
        if choose_your_door == "red":
            print("Ooh no, A tiger attack you, Game Over!") 
        elif choose_your_door == 'blue':
            print("Ooh no, A snake bite you. Game Over!")
        elif choose_your_door == "yellow":
            print("Bravo, You Complete the Game! Congratulation!")
        else:
            print("Wrong door selected, Game Over!")
            
    
    else:
        print("Ooh, You are attacked by a crocodile. Game Over")

else:
    print("Ooh You are Die, Gave Over!")