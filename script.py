import random
from tkinter import *
import pandas as pd
df = pd.read_excel('sheet.xlsx')
mylist = df.values.T[0].tolist()

def click():
  global mylist
  if len(mylist) > 0:
    randomNum = random.randint(0, len(mylist) - 1)
    label.config(text=mylist[randomNum])
    del mylist[randomNum]
  else:
    button.config(state=DISABLED)
    label.config(text='No numbers left, Please restart the program')
    

root = Tk()
root.title('Who\'s the lucky winner !?')
root.geometry('400x400')

button = Button(root, text='Draw the winner !!')
button.config(command=click)
button.pack(pady=80)

label = Label(root)
label.pack()


mainloop()