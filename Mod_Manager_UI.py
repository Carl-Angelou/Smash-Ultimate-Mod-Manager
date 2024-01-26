from tkinter import *
from tkinter import filedialog
from screeninfo import get_monitors
import pymsgbox

# ---------------- Monitor resolution & display default message box ----------------------
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
pymsgbox.rootWindowPosition = '+' + str(int(primary_mon_width/3)) + '+' + str(int(primary_mon_height/3))

# ---------------- MAIN Window Functionality ----------------------
root = Tk() # Create Root (MAIN) Window

# Naming and Sizing
root.title("Smash Ultimate Mod Manager")
root.minsize(int(primary_mon_width/3), int(primary_mon_height/2)) # TODO: MAKE CODE MORE CONCISE
root.maxsize(int(primary_mon_width/3), int(primary_mon_height/2))
root.geometry(str(int(primary_mon_width/3)) + 'x' + str(int(primary_mon_height/2)) + '+' + str(int(primary_mon_width/3)) + '+' + str(int(primary_mon_height/6)))

def BrowseFiles(): # https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
    filename = filedialog.askdirectory(initialdir='/', title='Select a Folder')

# Button Layout
button_file_browse = Button(root, text='Browse Files', command=BrowseFiles)

# Grid Layout
button_file_browse.grid(column=1, row=1)

root.mainloop()


