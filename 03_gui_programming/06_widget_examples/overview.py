
""" 
widgets built by their constructor

first argument always the "master widget" (parent widget) who owns the constructed object, examples:
- Window
- Frame
- LabelFrame

all widgets fall into 2 categories:
- clickable widgets (buttons, checkbuttons, radiobuttons, etc.)
- non-clickable widgets (labels, text, etc.)

clickable:
- Button - click to take action
- Checkbutton - click to change state (binary)
- Radiobutton - group of check buttons, click to change state (multiple choice - single select at given time)

non-clickable:
- Label - text
- LabelFrame - label with a title
- Message - text fitted to screen width
- Frame - container for other widgets

more complicated:
- entry - configurable text input, use with trace to monitor changes
- menu - menu bar, menu, submenu, cascade, command, separator, can bind to hotkeys
"""
