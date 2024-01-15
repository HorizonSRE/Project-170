from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Creating Buttons and Labels using Class")
root.geometry("900x900")

class CreatingElement:
    def __init__(self):
        print("This is a Class that Creates Elements")
    def createNewElement(self):
        label=Label(root, text="98.0")
        label.pack()

obj_of_CreatingElement=CreatingElement()
btn1=Button(root, text="Grade 1", command=obj_of_CreatingElement.createNewElement)
btn1.pack(padx=20, pady=10)
root.mainloop()