from tkinter import *
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

root.title("Smash Ultimate Mod Manager")
root.size()
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("500x500+")
root.mainloop()


