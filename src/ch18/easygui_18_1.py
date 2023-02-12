import easygui as gui

gui.msgbox(msg="Hello!", title="My first message box")
gui.msgbox(msg="Hello!", title="My first message box", ok_button="Click me")


# Returns string of the choice
gui.buttonbox(
    msg="What is your favourite colour?",
    title="Choose wisely...",
    choices=["Red", "Yellow", "Blue"]
)


# easygui.indexbox() returns index of the choice
# to gain access to the index outside of the gui, best ot define the choices outside of the function:
colours = ["Purple", "Teal", "Cyan"]
choice = gui.indexbox(
    msg="What's your favourite colour?",
    title="Choose wisely...",
    choices=colours
)
# ("Purple")
# >>> choice
# 0
print(colours[choice])
# "Purple"


# To collect text input from a user:
gui.enterbox(
    msg="What is your favourite colour?",
    title="Favourite colour"
)
# "Purple"


# To select a file or folder - it does not actually open one
# returns a string of the full path
gui.fileopenbox(title="Select a file")
gui.diropenbox(title="Select a folder")
gui.filesavebox()
# These return None if the user closes the dialog without pressing Open or Save


# To exit a program gracefully:
path = gui.fileopenbox(title="Select a file")
if path is None:
    exit()
