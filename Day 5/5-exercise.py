target = int(input())   # Enter the number between 0 and 1000

sum_of_even = 0
for even_number in range(0,target + 1 , 2):
    sum_of_even += even_number
print(sum_of_even)