import tkinter, random
canvas = tkinter.Canvas(width=700, height=650)
canvas.pack()

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

coll=0
positions={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0}
while coll==0:
    canvas.delete(all)
    linia = canvas.create_line(650, 0, 650, 650)
    for i in range(15):
        current=i
        lodicka(positions[i],0+i*30)
        positions[i]+=random.randint(0,10)
        l = canvas.coords('linia')
        coll = canvas.find_overlapping(*linia.coords(l))
        if len(coll) != 0: break
canvas.create_text(250,225,text=current,font="Arial 25")

