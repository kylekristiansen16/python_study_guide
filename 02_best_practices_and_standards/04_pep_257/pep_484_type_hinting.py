
# No type information added:
def hello(name):
    return "Hello, " + name


# Type information added to a function:
def hello(name: str) -> str:
    return "Hello, " + name


""" 
First of all, type hinting can help you document your code. Instead of leaving argument- 
and response-related information in docstrings, you can use the language itself to serve this purpose. 
This may be an elegant and useful way to highlight some of the more important code information, especially 
when publishing code in a project, sharing it with other developers, or leaving hints for yourself when you 
have to come back to the source code in the future. In some of the bigger software development projects, 
type hinting is a recommended practice that helps teams better understand the ways that types run through the code.

Type hinting allows you to notice certain kinds of errors more effectively and write a more beautiful and, 
most of all, cleaner code. When using type hints, you more carefully think about types in your code, which 
helps to prevent or detect some of the errors that may result from the dynamic nature of Python. (However,
we're not advocates for making Python require static typing.)

You must remember that type hinting in Python is not used at runtime, which means all the type information you 
leave in the code in the form of annotations is erased when the program is executed. In other words, type hinting 
does not have any effect on the operation of your code. On the other hand, when used along with some type checking 
system or lint-like tools that you can plug in to your editor or IDE, it can support your code-writing by 
autocompleting your typing and spotting and highlighting errors before your code is executed.

Since type hints have no effect on the source code, this means that they have no impact on performance times 
(characters are ignored by Python at runtime, which has no influence on interpretation/compilation speedups).
"""