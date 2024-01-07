year = int(input())

''' 
This is how we work out whether if a particular year is a leap year
    * on every year that is devisable by 4 with no reminder.
    * except every year that is evenly devisable by 100 with no reminder.
    *unless the year is also devisable by 400 with no reminder.
'''

if year % 4 ==0:
    if year % 100:
        if year % 400:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")

else:
    print("Not Leap Year")