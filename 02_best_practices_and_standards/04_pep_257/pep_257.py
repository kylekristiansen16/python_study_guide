
""" 
standardize the high-level structure of docstrings
    What should Python docstrings contain?
    How should Python docstrings be used?

Comments	
    Docstrings
Comments are non-executable statements in Python, which means that they are ignored by the Python interpreter; 
they are not stored in the memory, and cannot be accessed during program execution (i.e. they can be accessed 
by looking at the source code).	
    Docstrings can be accessed by reading the source code, and by using the __doc__ attribute or the help() function.
The main purpose of comments is increasing the readability and understandability of the code, and explaining the 
code to the user in a meaningful way. The user here means both other programmers and you (e.g. when you go back 
to your code after some time) – somebody who will want to or need to modify, extend, or maintain the code.	
    The main purpose of docstrings is documenting your code – describing its use, functionality, and capabilities 
    to users who do not necessarily need to know how it works.
Comments cannot be turned into documentation; their purpose is to simplify the code, provide precise information, a
nd help to understand the intention of a particular snippet/line.	
    Docstrings can be easily turned into actual documentation, which describes a module's or function's behavior, 
    the meaning of parameters, or the purpose of a specific package.
"""