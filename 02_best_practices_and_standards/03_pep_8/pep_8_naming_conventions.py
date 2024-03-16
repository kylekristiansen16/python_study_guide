# https://peps.python.org/pep-0008/#prescriptive-naming-conventions

""" 
Giving suitable names and avoiding inappropriate ones will definitely increase your code readability and 
save you (and other programmers reading your code) a lot of time and effort.

mysamplename – lowercase
my_sample_name – lowercase with underscores (snake_case)
MYSAMPLENAME – uppercase
MY_SAMPLE_NAME – uppercase with underscores (SNAKE_CASE)
MySampleName – CamelCase (also known as capitalized words, StudlyCaps, or CapWords)

A short note: when you use acronyms, you should capitalize all the letters that make up the acronym, e.g., HTTPServerError

mySampleName – mixed case, which actually differs from CamelCase only by having an initial lowercase character

My_Sample_Name – capitalized words with underscores (considered ugly by PEP 8)

_my_sample_name – a name that starts with a single leading underscore indicates a weak "internal use", e.g., the instruction 
    from SAMPLE import * will not import objects whose names start with an underscore.

my_sample_name_ -– a single trailing underscore is used by convention in order to avoid any conflicts with Python keywords, 
    e.g., class_

__my_sample_name – a name that starts with a double leading underscore is used for class attributes where it invokes name 
    mangling, e.g., inside the class MySampleClass, __room will become _MySampleClass__room

__my_sample_name__ – a name that starts and ends with a double underscore is used for "magic" objects and attributes that reside 
    in user-controlled namespaces, e.g., __init__, __import__, or __file__. You shouldn't create such names, but only use them as documented.
"""

""" naming different objects
When giving a name to a variable, you should use a lowercase letter or word(s), and separate words by underscores, e.g., x, var, my_variable.
The same convention applies to global variables.

Functions follow the same rules as variables, i.e., when giving a name to a function, you should use a lowercase letter or word(s) separated
by underscores, e.g., fun, my_function.

When giving a name to a class, you should adopt the CamelCase style, e.g., MySampleClass, or if there's only one word, start it with a capital
letter, e.g., Sample.

When giving a name to a method, you should use a lowercase word or words separated by underscores, e.g., method, my_class_method. You should 
always use self for the first argument to instance methods, and cls for the first argument to class methods.

When giving a name to a constant, you should use uppercase letters and separate words by underscores, e.g., TOTAL, MY_CONSTANT.

When giving a name to a module, you should use a lowercase word or words, preferably short, and separate them with underscores, 
e.g., samples.py, my_samples..

When giving a name to a package, you should use a lowercase word or words, preferably short ones. You shouldn't separate words, 
e.g., package, mypackage.

Type variable names should follow the CamelCase convention and be short, e.g., AnyStr, or Num.

When giving a name to an exception, you should follow the same convention as with classes (bear in mind that exceptions should actually be classes), 
i.e., use the CamelCase style.
"""