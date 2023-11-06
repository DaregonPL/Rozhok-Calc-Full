from tkinter import *

root = Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Rozhok Calc')
root.wm_attributes('-topmost', 1)
screen = Frame(root, bg = '#000000', borderwidth = 0)
screen.pack(anchor = 'nw')
output = Label(screen, bg = '#000000')
output.pack(padx = 10, pady = 10)
