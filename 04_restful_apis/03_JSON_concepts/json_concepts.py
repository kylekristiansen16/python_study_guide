
""" 
JSON = JavaScript Object Notation

JSON is a kind of universal bridge able to move data between seemingly incompatible parties
- JSON is a UTF-8 encoded text

how to represent an object?
1 - UTF-8 coded text – this means that no machine/platform-dependent formats are used; 
    it also means that the data JSON carries is readable (poorly, but always readable) and comprehensible by humans
        UTF-8 is the standard
        
2 - a simple and not very expanded format (we can call it syntax, or even grammar) to represent mutual dependencies and 
    relations between different parts of objects, and is able to transfer not only the values of objects’ properties, but also their names.
    
digraph : effective meaning
\\ = \
\/ = /
\b = backspace
\f = form feed
\n = line feed
\ = carriage return
\t = tab
\uXXXX or \UXXXX = unicode character with code XXXX (XXXX is a hexadecimal number)

** JSON strings cannot be split over multiple lines **

JSON representations:
numbers: 123, -123, 123.456, -123.456, 1.23e5, -1.23e5
strings: "abc", "a\"bc", "a\\bc", "a\/bc", "a\b", "a\f", "a\nbc", "a\rbc", "a\tbc", "a\u1234bc"
boolean: true, false
None   : null
arrays : [ ], [ 123 ], [ 123, 456, ["789", 293] ]
objects: { }, { "abc": 123 }, { "abc": 123, "def": 456, "ghi": ["789", 293] }

In JSON, all the above values may be combined (or packed) in two ways:
    - inside arrays (which are a very close relative to Python lists);
    - inside objects (which resemble Python dictionaries more than objects) (name must be enclosed in quotes.)

a JSON object is a set of property specifications separated by commas

no restrictions on property names

equivalent json objects:
{ 
x: 123,
y: -1
}
and
{x:123, y:-1}

another example:
    { me: "Python",
    pi: 3.141592653589,
    parsec: 3.0857E16, 
    electron: −1.6021766208E−19
    friend: "JSON",
    off: true,
    on: false,
    set: null }
    
json.loads()
- converts a JSON string into a Python object (also referred to as a JSON object)
- accepts json string as an argument
- returns a Python object (dict, list, str, int, float, bool, or None)    

json.dumps()
- converts a Python object into a JSON string
- accepts a Python object (or python data) as an argument
- returns a json string

"""