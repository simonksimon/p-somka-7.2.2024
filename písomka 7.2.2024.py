import tkinter as tk, random
from tkinter import Canvas
root=tk.Tk()
canvas: Canvas = tk.Canvas(width=700, height=650)
canvas.pack()

a=20
b=30
safety=0
st=False

def lodicka(x, y, i):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y - 25, x + 10 + plachta, y - 10, x, y - 5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)
    canvas.tagbind(canvas.line(x, y, x, y - 25, x + 10 + plachta, y - 10, x, y - 5),i)

def start(e):
    global a,b,safety,st
    v="0"
    for i in range(15):
        globals()["var_" + str(i)]=a
    for y in range(651):
        safety+=1
        if safety==1000:
            print("Safety overheated.")
            exit
        b = 30
        for i in range(15):
            #canvas.delete("all")
            #canvas.create_line(650, 0, 650, 650, fill="red")
            c=globals()["var_" + str(i)]
            current=canvas.find_closest(c-20, b)
            change=random.randint(1, 10)
            canvas.move(current,change,0)
            globals()["var_" + str(i)]+=change
            #globals()["var_" + str(i)]=random.randint(1, 10)
            #c = globals()["var_" + str(i)]
            print(i,c,b)
            canvas.after(1)
            if c==650 or c>650:
                v=str(i)
                st=True
                break
        if st == True:
            break
    canvas.create_text(350, 325, fill="darkblue", font="Times 15",text=v+"won.")

for i in range(15):
    lodicka(a,b,i)
    b+=35
canvas.create_line(650,0,650,650,fill="red")

canvas.bind("<Button-1>",start)
root.mainloop()