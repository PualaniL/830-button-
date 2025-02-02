#Imported tkinter library
import tkinter as tk 

#If button_click() is executed, "Button clicked!" will be printed.
def button_click():
    print("Button clicked!")
#root is assigned the value returned by tk.Tk(), and the title of the root window is set to "Button Example".
root= tk.Tk()
root.title("Button Example")

#A button is created from the attributes: parent 'root', and the command 'cutton-click()'
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

#Calling the main root 'main loop'
root.mainloop()


