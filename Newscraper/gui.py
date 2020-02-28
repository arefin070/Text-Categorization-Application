
from tkinter import *
from tkinter import font
from tkinter import messagebox
import TC_BN_Backend as backend


root = Tk()
root.geometry("1080x720")
helv36 = font.Font(family='Helvetica', size=13)


userInput = Text(root, height=20, width=130)

userInput.place(x=20,y=20)


output = Label(root, text = '',font=helv36)

output.place(x=100,y=400)

def callback():
    output.config(text=backend.getValue(userInput.get("1.0",END)))




MyButton1 = Button(root, text="অনুসন্ধান করুন", width=10, command=callback)
MyButton1.grid(row=1, column=1)
MyButton1.place(x=10,y=350)

outputLabel = Label(root, text = 'ফলাফল',font=helv36)

outputLabel.place(x=10,y=400)
root.mainloop()

