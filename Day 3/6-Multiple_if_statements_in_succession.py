print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7.")
    else:
        bill = 12
        print("Adult ticket are $12")

    wants_photo = input("Do you want to photo taken? Y or N.")
    if wants_photo == "Y":
        #Add $3 to their bill 
        bill = bill + 3 #(or we can write bill += 3)
       
    print(f"Your final bill {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


    