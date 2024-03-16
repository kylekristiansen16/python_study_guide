
# ! I need to set my python interpreter to python3.9 bc it's the only python I've installed with tkinter support !

""" 
GUI's developed in response to the old school mainframe and terminal

there was a need to develop a GUI that would allow users to interact with the computer in a more intuitive way
because prior to the gui, it was only text based

GUI sometimes called visual programming
- The term stresses the fact that an application's look is as important as its functionality, but it's not just 
    a matter of what you see on the screen, but also what you can do to change its state, and how you force the 
    application to submit to your will.
    
this requires a completely different approach to programming
"""

""" 
widgets (or controls) = gui elements designed to receive gesures from the user
focus widget = the widget that is currently receiving gestures from the user
title bar = the bar at the top of the window that contains the title of the window
closing button = the button at the top right of the window that closes the window
icon = a small picture that usually helps the user to quickly identify the issue
label = a piece of text inside a window which literally explains the window's purpose

the traditional programming paradigm in which the programmer is responsible for responding to literally all the 
    user's actions is completely useless in visual programming
Because the number of all possible user moves is so substantial that continuous checking of the window's state 
    changes, along with controlling all widget behavior, making the coding extremely heavy, and the code becomes badly bloated

hence.... event driven programming
"""

# not event driven:
# while True:
#     wait_for_user_action()
#     if user_pressed_button_yes():
#     :
#     elif user_pressed_button_no():
#     :
#     elif user_move_mouse_coursor_over_button_yes():
#     :
#     elif user_move_mouse_coursor_over_button_no():
#     :
#     elif user_pressed_Tab_key():
#         if isfocused(button_yes):
#         :
#         elif isfocused(button_no):
#        :
#     :
#     :

""" 
First of all, detecting, registering and classifying all of a user's actions is beyond the programmer's control – there 
is a dedicated component called the event controller which takes care of this. It's automatic and completely opaque. You 
don't need to do anything (or almost anything) to make the machinery run, but you are obliged to do something else

Let's imagine that we have a function named DoSomething() which... does something. We want the function to be invoked 
when a user clicks a button called DO IT!.

In the classical paradigm we would have to:

 - discover the click and check if it happened over our button;
 - redraw the button to reflect the click (e.g., to show that it is actually pressed)
 - invoke the function.

In the event-driven paradigm our duties look completely different:

 - the event controller detects the clicks on its own;
 - it identifies the target of the click on its own;
 - it invokes the desired function on its own;
 - all these actions take place behind the scenes! Really!
"""

""" 
new concept... event

types:
 - pressing the mouse button;
 - releasing the mouse button (actually, an ordinary mouse click consists of these two subsequent events)
 - moving the mouse cursor;
 - dragging something under the mouse cursor;
 - pressing and releasing a key;
 - tapping a screen;
 - tracking the passage of time;
 - monitoring a widgets state change;
 - and many, many more...
"""