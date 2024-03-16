""" 
few rules you should follow when leaving comments in code:
- Write comments that will not contradict the code or mislead the reader. They’re much worse than no comment at all.
- Update your comments when your program gets updated.
- Write comments as complete sentences (capitalize the first word if it’s not an identifier, and end your sentence with a full stop). For example:
"""

# Program that calculates body mass index (BMI).

height = float(input("Your height (in meters): "))
weight = float(input("Your weight (in kilograms): "))
bmi = round(weight / (height*height), 2)

print("Your BMI: {}".format(bmi))

""" 
- When writing block comments with multi-sentence comments, use two spaces after each full stop ending a sentence, except after the final sentence.
- Write comments in English (unless you are 100% sure that the code will never be read by people who don’t speak your language.)
- Comments should consist of no more than 72 characters per line (but you know that already).
"""

""" 
Block comments are usually longer, and you should use them to explain sections of code rather than particular lines

- should refer to the code that follows them;
- should be indented to the same level as the code they describe.
"""

def calculate_product():
    # Calculate the average of three numbers obtained from the user. Then 
    # multiply the result by 4.17, and assign it to the product variable.
    #
    # Return the value passed to the product variable and use it
    # for the subsequent x to y calculations to speed up the process.
    sum_numbers = 0
    
    for number in range(0, 3):
        number = float(input("Enter a number: "))
        sum_numbers += number
    
    average = (sum_numbers / 3) * 4.17
    product = average
    return product

x = product * 1.73
y = x ** 2
x_to_y = (x*y) / 1.05

""" 
Inline comments are comments that are written on the same line as your statements. 
They should address or provide further explanation to a single line of code or a single statement. 
You should not overuse them
- separated by two (or more) spaces from the statement they address;
- used sparingly.
"""
# Bad:

a = 'Adam'  # User's first name.

# Good:

user_first_name = 'Adam'

""" 
Documentation strings, or docstrings as they’re often called, 
let you provide descriptions and explanations for all public modules, files, functions, classes, and methods you use in your code

begins and ends with three double quotes: """

# A multi-line docstring:

def fun(x, y):
    """Convert x and y to strings,
    and return a list of strings.
    """
    ...


# A single-line docstring:

def fun(x):
    """Return the square root of x."""
    ...