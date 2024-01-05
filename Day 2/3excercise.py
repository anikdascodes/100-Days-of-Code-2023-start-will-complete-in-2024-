'''
Write a program that adds the digits in a two digit number. e.g. if the input was 35, then the output should be 3+5 =8

Warning : Do not change the code on line 1.your program should work for different inputs.e.g. any two-digit number.

The last line of your program should print the result.


Example Input :
39

Example Output
12
'''

two_digit_number = input("Input your two digit number : ")
print(type(two_digit_number))

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#lets add the two digit 

print(first_digit + second_digit)
