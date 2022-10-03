
# Imports tkinter and ttk module
from tkinter import * 
from tkinter.ttk import *
  
# toplevel window
root = Tk()
  
# method to make widget invisible
# or remove from toplevel
def forget(widget):
    widget.forget()
  
# method to make widget visible
def retrieve(widget):
    widget.pack(fill = BOTH, expand = True)
  
# Button widgets
b1 = Button(root, text = "Btn 1")
b1.pack_forget()

b4 = Button(root, text = "Btn 1")
b4.pack_forget()
  
# See, in command forget() method is passed
b2 = Button(root, text = "Btn 2", command = lambda : forget(b1))
b2.pack(fill = BOTH, expand = True)
  
# In command retrieve() method is passed
b3 = Button(root, text = "Btn 3", command = lambda : retrieve(b1 and b4))
b3.pack(fill = BOTH, expand = True)
  
# infinite loop, interrupted by keyboard or mouse
mainloop()
