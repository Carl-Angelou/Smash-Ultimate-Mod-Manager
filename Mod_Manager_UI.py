from tkinter import *
from tkinter import filedialog
from screeninfo import get_monitors
import pymsgbox
import os

# ---------------- Monitor resolution & display default message box ---------------------- TODO: MAKE IT APPLY TO FILE DIALOG (make file dialog at center of screen)
primary_mon_width = 0
primary_mon_height = 0
primary_mon_x = 0

for m in get_monitors(): # https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
    # print(str(m))
    if m.is_primary == True:
        primary_mon_width = m.width
        primary_mon_height = m.height
        primary_mon_x = m.x

print('\nprimary_mon_width: ' + str(primary_mon_width))
print('primary_mon_height: ' + str(primary_mon_height))
print('primary_mon_x: ' + str(primary_mon_x))

# Changes default message box location to half height and width of primary display
pymsgbox.rootWindowPosition = '+' + str(int(primary_mon_width/10)) + '+' + str(int(primary_mon_height/3))

# -------------------- MAIN Window Properties ----------------------
root = Tk() # Create Root (MAIN) Window

# GLOBAL VARIABLES
global filename
filename = 'N/A'

# Naming and Sizing
root.title("Smash Ultimate Mod Manager")
root.resizable(0,0)
root.geometry(str(int(primary_mon_width/3)) + 'x' + str(int(primary_mon_height/2)) + '+' + str(int(primary_mon_width/3)) + '+' + str(int(primary_mon_height/6)))

# -------------------- Functions for Clickable Objects ----------------------
def BrowseFiles(): # https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
    filename1 = filedialog.askdirectory(initialdir='/', title='Select a Folder') # https://pythonassets.com/posts/browse-file-or-folder-in-tk-tkinter/
    filename = filename1
    print('\nBrowse File - Filename: ' + filename)

def ListFiles(): # https://www.javatpoint.com/file-explorer-using-tkinter-in-python
    file_list = os.listdir(os.path.abspath(filename))

# -------------------- Menu Layout ----------------------
# Frame Layout
Tk.grid(root)
root.columnconfigure(0, weight=5)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

menu_left = Frame(root, bg='red') # Left Menu Frame
menu_left.grid(row=0, column=0, sticky='nsew')

menu_right = Frame(root, bg='gold') # Right Menu Frame
menu_right.grid(row=0, column=1, sticky='nsew')

# Right Menu Layout
menu_right.rowconfigure(0, weight=1) # https://www.youtube.com/watch?v=i577cFu8eBI (skip to end of video)
menu_right.rowconfigure(1, weight=1) # Row 1: Used for BROWSE FILES Button
menu_right.rowconfigure(2, weight=10)
menu_right.rowconfigure(3, weight=1) # Row 2: Used for SKINS Button
menu_right.rowconfigure(4, weight=1) # Row 3: Used for STAGES Button
menu_right.rowconfigure(5, weight=5)
menu_right.columnconfigure(0, weight=1)

label_file_browse = Label(menu_right, text='Please select your Smash\nUltimate Mods folder...', font=('verdana', '10'))
label_file_browse.grid(row=0, column=0)

button_file_browse = Button(menu_right, text='Browse Files', font='verdana', command=BrowseFiles)
button_file_browse.grid(row=1, column=0)

button_skins = Button(menu_right, text='Skins', font='verdana', width=13, height=5, command=BrowseFiles)
button_skins.grid(row=2, column=0)

button_stages = Button(menu_right, text='Stages', font='verdana', width=13, height=5, command=BrowseFiles)
button_stages.grid(row=3, column=0)

# Left Menu Layout


root.mainloop()


