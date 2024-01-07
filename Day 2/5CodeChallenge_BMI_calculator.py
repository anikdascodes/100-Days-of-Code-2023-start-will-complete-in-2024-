'''
Instructions:

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

BMI Wikipedia Page(https://en.wikipedia.org/wiki/Body_mass_index)

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

BMI Formula:

BMI = weight(kg)/height**2(m*m)


NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.

Example Input 1
1.75
80
means: weight = 80 and height = 1.75

Example Output 1
26
Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837

Example Input 2
1.58
57
Example Output 1
22
'''

# 1st input : enter height in meters e.g: 1.65
height = input()
# 2nd input : enter weight in kilogram e.g: 72
weight = input()

weight_as_int = int(weight)
height_as_float = float(height)

#using the exponent operator
BMI = weight_as_int / height_as_float ** 2

#or using the multiplication and PEMDAS
BMI = weight_as_int / (height_as_float * height_as_float)

BMI_as_int = int(BMI)
print(BMI_as_int)