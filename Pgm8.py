from tkinter import  *
top = Tk()

top.geometry("600x600")
c= Canvas(top, bg="pink", width="600", height="600")
circle=c.create_oval(60,60,150,150,fill="green")
square=c.create_rectangle(200,300,300,400,fill="red")
line=c.create_line(100,400,150,300,fill="green")
c.pack()

uname=Label(top,text="User Name").place(x="150",y="150")
e=Entry(top,width="20").place(x="230",y="150")
e1=Entry(top,width="20").place(x="230",y="180")
password = Label(top,text="Password").place(x="150",y="180")
button = Button(top,text="SUBMIT",activeforeground="white",activebackground="green").place(x="190",y="220")
top.mainloop()