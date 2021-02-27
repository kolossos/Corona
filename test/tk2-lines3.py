import tkinter as tk
import numpy as np
from random import randrange

n=100
r=35

root = tk.Tk()

root.attributes("-zoomed",True)
root.overrideredirect(1)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()//1, root.winfo_screenheight()//1))

screen_width = root.winfo_screenwidth()//1
screen_height = root.winfo_screenheight()//1
r=0.45*np.min((screen_width,screen_height))
points=np.arange(n)
x=screen_width//2+r*np.cos(2*np.pi*points/n)
x=x.astype(np.int)
y=screen_height//2+r*np.sin(2*np.pi*points/n)
y=y.astype(np.int)
p=np.array([x,y]).T

def grow(canvas, item, j):
    global i
    global p
    if j==1:
        i=i+1%30+45
    #(x1,y1,x2,y2) = canvas.coords(item)
    new_coords = (p[j,0],p[j,1],p[int(i*j)%n,0],p[int(i*j)%n,1])
    canvas.coords(item, new_coords)
    #canvas.fill="#"+str(randrange(899999)+100000)
    #root.title(str(i))
    root.after(1000, grow, canvas, item,j)


canvas = tk.Canvas(root,bg="black")
canvas.pack(side="top", fill="both", expand=True)

i=1
items=[]
for j in np.arange(n):
    items.append(canvas.create_line(p[j,0],p[j,1],p[int(i*j)%n,0],p[int(i*j)%n,1],width = 3, fill="green"))


#item = canvas.create_oval(10, 10, 100, 100, outline="black", fill="red")
for j in np.arange(n):
    grow(canvas, items[j],j)

root.mainloop()
