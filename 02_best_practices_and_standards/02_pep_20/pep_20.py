""" Pep 20: The Zen of Python

The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


"""

import this # easter egg with poem from Tim Peters about python zen
print()

""" Beautiful is better than ugly.

example bad:
    from math import sqrt
    sidea = float(input("The length of the 'a' side:"))
    sideb = float(input("The length of the 'b' side:"))
    sidec = sqrt(a**2+b**2)
    print("The length of the hypotenuse is", sidec )

example good:
    from math import sqrt

    side_a = float(input("The length of the 'a' side: "))
    side_b = float(input("The length of the 'b' side: "))
    hypotenuse = sqrt(a**2 + b**2)

    print("The length of the hypotenuse is", hypotenuse)
"""

""" Explicit is better than implicit.
bad:
    from fruit import *

    apples(2, 3.45)

good:
    from fruit import apples, bananas

    apples(quantity=2, price=3.45)
"""

""" Simple is better than complex
Remember: use appropriate tools adjusted to the specificity of your project.

Example: Sort the numbers list in ascending order.
bad:
    import heapq

    numbers = [-1, 12, -5, 0, 7, 21, 15, 1]
    heapq.heapify(numbers)

    sorted_numbers = []

    while numbers:
        sorted_numbers.append(heapq.heappop(numbers))

    print(sorted_numbers)
    
good:
    numbers = [-1, 12, -5, 0, 7, 21, 15, 1]
    numbers.sort()

    print(numbers)
"""

""" Complex is better than complicated
Distinguishing between 
- complex, as consisting of many elements and 
- complicated, meaning difficult to understand, 
is yet another thing to consider when writing code.

example: Perform five additions of two numbers.
bad:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    addition_result = first_number + second_number
    print(first_number, "+", second_number, "=", addition_result)
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    addition_result = first_number + second_number
    print(first_number, "+", second_number, "=", addition_result)
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    addition_result = first_number + second_number
    print(first_number, "+", second_number, "=", addition_result)
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    addition_result = first_number + second_number
    print(first_number, "+", second_number, "=", addition_result)
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    addition_result = first_number + second_number
    print(first_number, "+", second_number, "=", addition_result)
    
good:
    def addition(x, y):
        print(x, "+", y, "=", x+y)

    for i in range(5):
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        addition(first_number, second_number)
"""

""" Flat is better than nested.
Nesting two or three levels deep may still be good, but anything beyond that becomes confusing and unreadable.

Even though you can actually have any level of nested loops or if statements in Python, anything above three 
should be a clear signal that it’s maybe a good time to start refactoring your code.

Flat code is more user-friendly, and becomes much easier to maintain. Remember this.

bad:
    x = float(input("Enter a number: "))

    if x > 0:
        if x > 1:
            if x > 2:
                if x > 3:
                    if x >= 4:
                        if x <= 6:
                            print("x is a number between 4 and 6.")
    else:
        print("x is not a number between 4 and 6.")
good:
    x = float(input("Enter a number: "))

    if x >= 4 and x <=6:
        print("x is a number between 4 and 6.")
    else:
        print("x is not a number between 4 and 6.")
"""

""" Sparse is better than dense.
comes after "flat better than nested" bc the way to increase sparsity is through nesting, it's a balancing act.

bad:
    x = 1
    if x == 1 : print("Hello, World!")
good:
    x = 1
    if x == 1:
        print("Hello, World!")
"""

""" Readability counts.
the essence of the Python philosophy is that “code is read more often than it is written” (Guido Van Rossum).

bad:
    def f(i):
        l = i + (0.08 * i)
        return l
good:
    # Calculates the gross price of products in Wonderland.
    
    def calculate_gross_price(net_price):
        gross_price = net_price + (0.08 * net_price)
        return gross_price
"""

""" Special cases aren't special enough to break the rules.
No special cases such as time pressure or complexity of a given problem should be an excuse for writing code that does not follow the guidelines.

Example: Write a function that multiplies two numbers and a function that adds two numbers.

bad:
    def multiply_two_numbers(first_number, second_number):
        return first_number * second_number

    print(multiply_two_numbers(7, 9))


    def addingTwoNumbers(firstNumber, secondNumber):
        return firstNumber + secondNumber

    print(addingTwoNumbers(7, 9))

good:
    def multiply_two_numbers(first_number, second_number):
        return first_number * second_number

    print(multiply_two_numbers(7, 9))


    def add_two_numbers(first_number, second_number):
        return first_number + second_number

    print(add_two_numbers(7, 9))
"""

""" Although practicality beats purity.
If the possible benefits (e.g., better performance) are larger than the possible negative effects 
    (e.g., affected maintainability), 
the real-world coding problems may find an excuse for making an exception to the rules. 
    Practicality then becomes more important than purity.
"""

""" Errors should never pass silently ...Unless explicitly silenced.
The Zen of Python gently reminds us that if a block of code is unable to perform its function and 
    work in the way that is expected by the programmer, 
it should terminate the program and/or loudly announce that something has gone wrong (i.e., raise 
    an exception) rather than continue running without interruption.

bad: 
    try:
        print(1/0)
    except Exception as e:
        pass
good:
    try:
        print(1/0)
    except ZeroDivisionError:
        print("Don't divide by zero!")
good:
    try:
        number = int(input("Enter an integer number: "))
    except:
        number = 0
"""

""" In the face of ambiguity, refuse the temptation to guess.
This guideline conveys a twofold message: on the one hand, it tells you to have limited trust in the code you’re writing, 
while on the other hand, it implies that you should have limited trust in the code you’re reading...
- test your code before releasing it to production 
- testing your code allows you to save time, not waste it
- a bug at an advanced stage of development, corrections may be a pretty expensive and time-consuming enterprise.
- avoid writing ambiguous code, which means you should leave no room for guessing. Give your variables self-commenting 
    names, and leave comments where necessary
- If you’re working on a program that accepts data from the user, don’t rely on your guesses, because what you assume 
    to be the most common may turn out to be the least common when faced with real-life data

"""
print("A" > "a") # False
print(1.0 == 1) # True
print("1" == 1) # False
print(True == "1") # False
print(True == 1) # True
print(True == 1.0) # True
print("1" + "1") # '11'
print(1 + 1) # 2
# print(1 + "1") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

""" There should be one-- and preferably only one --obvious way to do it ...Although that way may not be obvious at first unless you're Dutch
where possible, it’s good to remember that each function, each class, each method – each entity – 
    should have a single cohesive responsibility. 
why? Because such an approach helps you gain more clarity and produce cleaner code, makes it easier 
    and cheaper to maintain it, and less vulnerable to bugs.

one obvious way to do something may not necessarily be obvious at first.
- Finding a relevant and preferred solution may require time, effort, and changing certain habits.

What’s the best way to access values in a dictionary: using the get() method, or the syntax my_dict['key'], 
    or some other way? 
What’s the best way to read a file: block by block, line by line? 
What’s the best way to print the user’s first and last names on the screen…?
"""

""" Now is better than never ...Although never is often better than *right* now
Python lets you quickly translate your ideas into working code
-  write down your thoughts and encode them in Python – even if your code is far from perfect. 
    You can later refine, develop, or redesign it very easily.

Another thing to remember is that there is no such thing as a perfect thing.
- If you give in to temptation to complete a program and release it only when it’s perfect, 
    it’s highly probable you will never do it.

the aphorism tells us not to forget about the proper balance. Just as perfect is the enemy of 
    good, it often turns out that faster is the enemy of slower. There are cases when things 
    should not be rushed.

def deprecated_function():
    raise DeprecationWarning
"""

""" If the implementation is hard to explain, it's a bad idea ... If the implementation is easy to explain, it may be a good idea.
- Everything and anything that can be explained in words can be translated into code, 
    and eventually turned into a well-operating computer program.

If you can explain what you expect from a program, what you want it to do – such a program can be designed. 
If you find it difficult to explain its features and functionality, it may be a signal that maybe 
    your idea should be thought over again and digested.

However, even though something’s easy to explain, it doesn’t mean it’s good. It’s just easier to judge whether it is or not.
"""

""" Namespaces are one honking great idea -- let's do more of those!
what is namespace? https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces 
    a namespace is a system that has a unique name for every object in Python. An object might be a variable or a method.
    Simply speaking, it means that whenever you define a variable, Python “remembers” two things: the variable’s identifier, and the value you pass to it.
    
    How does it happen? Python implicitly adds them to an internal dictionary which resides within a particular scope, i.e., the region of a Python program where namespaces are accessible
    
Functions, classes, objects, modules, packages… they’re all namespaces
- a more specific namespace cannot be altered by a less specific namespace, as they reside within two different scopes (e.g., a local variable inside a function doesn’t influence a global variable*). 
- However, a more specific namespace has access to a less specific namespace (e.g., a global variable can be accessed from within a function).

bad:
    from instruments.guitars import fender, ibanez

    fender(page)
    ibanez(vai)
good bc it imports the namespace:
    from instruments import guitars

    guitars.fender(page)
    guitars.ibanez(vai)
"""