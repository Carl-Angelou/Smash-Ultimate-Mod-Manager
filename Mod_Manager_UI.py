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

# Naming and Sizing
root.title("Smash Ultimate Mod Manager")
root.resizable(0,0)
root.geometry(str(int(primary_mon_width/3)) + 'x' + str(int(primary_mon_height/2)) + '+' + str(int(primary_mon_width/3)) + '+' + str(int(primary_mon_height/6)))

# -------------------- Functions for Clickable Objects ----------------------
def BrowseFiles(): # https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
    filename = filedialog.askdirectory(initialdir='/', title='Select a Folder') # https://pythonassets.com/posts/browse-file-or-folder-in-tk-tkinter/
    print('\nBrowse File - Filename: ' + filename)
    ListFiles(filename)

def ListFiles(filename): # https://www.javatpoint.com/file-explorer-using-tkinter-in-python
    # print('filename = ' + filename)
    os.chdir(filename[0] + ':')
    file_list = os.listdir(filename)
    print(file_list) # Print out all files from directory

    file_list = sorted(file_list) # Sorts files alphabetically
    
    if listbox_files.size() > 0:
        listbox_files.delete(0, END)

    for values in file_list:
        listbox_files.insert(END, values)

# -------------------- Menu Layout ----------------------
# Frame Layout
Tk.grid(root)
root.columnconfigure(0, weight=5)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

menu_left = Frame(root, bg='blue') # Left Menu Frame
menu_left.grid(row=0, column=0, sticky='nsew')

menu_right = Frame(root) # Right Menu Frame
menu_right.grid(row=0, column=1, padx=20, sticky='nsew')

# Right Menu Layout
menu_right.rowconfigure(0, weight=1) # https://www.youtube.com/watch?v=i577cFu8eBI (skip to end of video)
menu_right.rowconfigure(1, weight=1) # Row 1: Used for BROWSE FILES Button
menu_right.rowconfigure(2, weight=2)
menu_right.rowconfigure(3, weight=1) # Row 3: Used for ADD SKINS Button
menu_right.rowconfigure(4, weight=1) # Row 4: Used for CHANGE SKINS Button
menu_right.rowconfigure(5, weight=1) # Row 5: Used for DELETE SKINS Button
menu_right.rowconfigure(6, weight=2)
menu_right.rowconfigure(7, weight=1) # Row 7: Used for ADD STAGES Button
menu_right.rowconfigure(8, weight=1) # Row 8: Used for CHANGE STAGES Button
menu_right.rowconfigure(9, weight=1) # Row 9: Used for DELETE STAGES Button
menu_right.rowconfigure(10, weight=5)
menu_right.columnconfigure(0, weight=1)

label_file_browse = Label(menu_right, text='Please select your Smash\nUltimate Mods folder...', font=('verdana', '8'), width=18, padx=20)
label_file_browse.grid(row=0, column=0)

button_file_browse = Button(menu_right, text='Browse Files', font='verdana', command=BrowseFiles)
button_file_browse.grid(row=1, column=0)

button_skins = Button(menu_right, text='Add Skins', font='verdana', width=13, height=2, command=BrowseFiles)
button_skins.grid(row=3, column=0)

button_skins = Button(menu_right, text='Change Skins', font='verdana', width=13, height=2, command=BrowseFiles)
button_skins.grid(row=4, column=0)

button_skins = Button(menu_right, text='Delete Skins', font='verdana', width=13, height=2, command=BrowseFiles)
button_skins.grid(row=5, column=0)

button_stages = Button(menu_right, text='Add Stages', font='verdana', width=13, height=2, command=BrowseFiles)
button_stages.grid(row=7, column=0)

button_stages = Button(menu_right, text='Change Stages', font='verdana', width=13, height=2, command=BrowseFiles)
button_stages.grid(row=8, column=0)

button_stages = Button(menu_right, text='Delete Stages', font='verdana', width=13, height=2, command=BrowseFiles)
button_stages.grid(row=9, column=0)

# Left Menu Layout
listbox_files = Listbox(menu_left, width=41, activestyle='dotbox', font=('verdana', '12'))
listbox_files.pack(side=LEFT, fill=BOTH)

scrollbar_files = Scrollbar(menu_left)
scrollbar_files.pack(side=RIGHT, fill=BOTH)
listbox_files.config(yscrollcommand=scrollbar_files.set)
scrollbar_files.config(command=listbox_files.yview)

# TESTING LISTBOX AND SCROLLBAR WITH 100 VALUES
# for values in range(100): 
#     listbox_files.insert(END, values)

root.mainloop()


