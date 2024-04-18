print(int(8/3))

#Round Function
'''
The `round()` function in Python is used to round a number to a specified number of decimal places. The behavior of this function is straightforward:

1. **Syntax:** `round(number, ndigits)`

   - `number`: This is the number you want to round.
   - `ndigits`: This is optional. It specifies the number of decimal places to which you want to round the number. If omitted, it defaults to 0, meaning it rounds to the nearest integer.

2. **Behavior:**
   - If `ndigits` is provided, the number is rounded to that many decimal places.
   - If `ndigits` is omitted, the number is rounded to the nearest integer.
   - For values exactly halfway between two integers (e.g., 2.5, 3.5), Python rounds to the nearest even number. This is known as "rounding half to even" or "bankers' rounding," which reduces a small bias that could accumulate when adding many such numbers together.

3. **Examples:**

   - `round(3.14159, 2)` would return `3.14`.
   - `round(3.14159)` would return `3`.
   - `round(2.5)` would return `2`, and `round(3.5)` would return `4` (demonstrating rounding half to even).

This function is often used in situations where you need to control the precision of floating-point numbers, such as in financial calculations, data analysis, or when displaying values to the user.
'''

print(round(8/3))
print(round(8/3,2))
print(round(2.55555555555555555555555555, 2))

# Floor division
'''
In Python, floor division is an operation that divides one number by another and then applies the floor function to the result, which means it rounds down to the nearest whole number. The floor division operator is `//`.

Here are some key points about floor division:

1. **Syntax and Usage:** 
   - The syntax for floor division is `a // b`, where `a` and `b` are numbers.
   - Unlike regular division (`/`) which returns a floating-point result (a number with a decimal point), floor division returns an integer result.

2. **Behavior with Positive and Negative Numbers:**
   - When both operands are positive, floor division simply divides and truncates the decimal part (if any).
   - When dealing with negative numbers, floor division can yield different results compared to regular division, as it always rounds towards negative infinity. For example, `-7 // 3` would be `-3` instead of `-2`, because `-2.333...` is rounded down to `-3`.

3. **Examples:**
   - `8 // 3` would return `2`, as the division results in `2.666...`, and the decimal part is discarded.
   - `9 // 2` would return `4`, as `4.5` is truncated to `4`.
   - `-7 // 3` would return `-3`, because the result of `-2.333...` is rounded down to `-3`.
   - `7 // -3` would return `-3`, as `-2.333...` is rounded down to `-3`.

4. **Data Types:**
   - If both operands are integers, the result will be an integer.
   - If one of the operands is a floating-point number, the result will still be floored but returned as a float. For example, `7.0 // 2` would yield `3.0`.

5. **Use Cases:**
   - Floor division is commonly used in scenarios where you need to calculate the number of times a value fits into another value, such as in pagination systems (calculating the number of pages), or in grid-based layouts (determining row and column indices).

In summary, floor division is a useful tool in Python for performing division when you are interested in the integer quotient and want to round down the result, especially in cases involving negative numbers.
'''

print(8//3)



'''
iIn Python, operators like `+=`, `-=`, `*=`, and `/=` are called "assignment operators." These are a type of shorthand used to perform an operation and an assignment in a single step. 

Here's a breakdown of each:

1. **`+=` (Addition assignment):**
   - `a += b` is equivalent to `a = a + b`.
   - This operator adds the value of `b` to `a` and then assigns the result back to `a`.

2. **`-=` (Subtraction assignment):**
   - `a -= b` is equivalent to `a = a - b`.
   - This operator subtracts the value of `b` from `a` and then assigns the result back to `a`.

3. **`*=` (Multiplication assignment):**
   - `a *= b` is equivalent to `a = a * b`.
   - This operator multiplies `a` by `b` and then assigns the result back to `a`.

4. **`/=` (Division assignment):**
   - `a /= b` is equivalent to `a = a / b`.
   - This operator divides `a` by `b` and then assigns the result back to `a`.

These assignment operators are widely used for their convenience and readability, especially in loops or iterative calculations. They allow you to modify the value of a variable without repeating the variable name, making the code cleaner and often easier to understand.
'''

score = 0

# User scores point
score += 1 

print(score)





#f -  string 

score = 0 
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, your winning is {isWinning}" )