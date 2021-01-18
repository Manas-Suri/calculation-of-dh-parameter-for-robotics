import tkinter as tk
from front import Number

front = Number()

def major():
    peeps = front.numberstodirection(int(v.get()), 1, int(e2.get()), int(e3.get()), int(e4.get()), int(e5.get()))
    return peeps

def first_one():
    peep = major()
    list1.insert(0,peep[0])
    list1.insert(1, peep[1])
    list1.insert(2, peep[2])
    list1.insert(3, peep[3])
    #e2.destroy(), e3.delete(0, 'end'),e4.delete(0,'end'),e5.delete(0,'end')
    return peep
    #print (v.get())

def second_one():
    bags = first_one()
    #print(bags)
    #print(int(v.get()))
    absic = front.numberstodirection(int(v.get()),1,int(e2.get()),int(e3.get()),int(e4.get()),int(e5.get()))
    for i in range(len(bags)):
        for j in range(len(absic)):
            bags[i][j] = bags[i][j] * absic[i][j]
            bags[i][j] =round(bags[i][j],2)
    print(bags)
    for i in range(len(bags)):
        list1.insert(i, "")
        list1.insert(i,bags[i])
    #e2.delete(0, 'end'), e3.delete(0, 'end'), e4.delete(0, 'end'), e5.delete(0, 'end')


window = tk.Tk()
v = tk.IntVar()
v.set(1)

Axis = [("X axis",1),
        ("Y axis",2),
        ("Z axis",3)]

l1 = tk.Label(window,text = "Rotation Along")
l1.grid(row = 0,column = 0)
for axis,val in Axis:
    tk.Radiobutton(window,
                   text=axis,
                   pady = 3,
                   variable=v,
                   #command = lamb,
                   value=val).grid(row = 0,column = val)


l2 = tk.Label(window,text = "a")
l2.grid(row = 1,column = 0)

a_value = tk.StringVar()
e2 = tk.Entry(window,textvariable = a_value)
e2.grid(row = 1,column = 1)


l3 = tk.Label(window,text = "b")
l3.grid(row = 1,column = 2)

b_value = tk.StringVar()
e3 = tk.Entry(window,textvariable = b_value)
e3.grid(row = 1,column = 3)


l4 = tk.Label(window,text = "c")
l4.grid(row = 1,column = 4)

c_value = tk.StringVar()
e4 = tk.Entry(window,textvariable = c_value)
e4.grid(row = 1,column = 5)


l5 = tk.Label(window,text = "Angle")
l5.grid(row = 2,column = 0)
Angle_value = tk.StringVar()
e5 = tk.Entry(window)
e5.grid(row = 2,column = 1)


list1 = tk.Listbox(window,height = 6,width = 35)
list1.grid(row = 3,column = 0,rowspan =6,columnspan = 2)

b1 = tk.Button(window,text ="Solution",width = 12,command = first_one)
b1.grid(row =2,column = 3)

b2 = tk.Button(window,text ="Multiply",width = 12,command = second_one)
b2.grid(row =3,column = 3)


window.mainloop()
