import tkinter 
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()
root.title("Restaurant Manager Login")
root.geometry("700x520+200+50")
root.configure(bg="pink")
root.resizable(0,0)

#functions
def exitt():
    root.destroy()
    main.destroy()
def reset():
    user_name_entry.delete(0,END)
    password_entry.delete(0,END)
def login():
    input1=user_name_entry.get()
    input2=password_entry.get()
    if input1=="admin" and input2=="123":
        global main
        main = tkinter.Toplevel(root)
        main.title("Bill and Profit Calculation")
        main.geometry("1000x600+100+50")
        main.configure(background="pink")
        main.resizable(0,0)
        #functions
        def reset_values():
            entry11.delete(0,END)
            entry22.delete(0,END)
            entry33.delete(0,END)
            entry44.delete(0,END)
            entry55.delete(0,END)
            entry66.delete(0,END)
            entry77.delete(0,END)
            
        def calculate_values():
            try: a1=int(entry11.get())
            except: a1=0
            try: a2=int(entry22.get())
            except: a2=0
            try: a3=int(entry33.get())
            except: a3=0
            try: a4=int(entry44.get())
            except: a4=0
            try: a5=int(entry55.get())
            except: a5=0
            try: a6=int(entry66.get())
            except: a6=0
            try: a7=int(entry77.get())
            except: a7=0
            b1=a1*60
            b2=a2*30
            b3=a3*20
            b4=a4*25
            b5=a5*80
            b6=a6*20
            b7=a7*100
            total=b1+b2+b3+b4+b5+b6+b7 
            #bill = StringVar()
            bill="Rs."+str(total)
            messagebox.showinfo("total amount", "total amount is "+str(total))
            labl333 = Entry(frame3,textvariable=bill,font=("Arial", 13,), bg="white",fg="blue",)
            labl333.place(x=140,y=100,width=100,height=30)

        #heading
        heading = Label(main, text="Bill and Profit Calculation", font=("arial", 25, "bold"), bg="black",fg="white")
        heading.pack(ipady=20, ipadx=10, fill=X)
        #frame
        frame = Frame(main, bg="orange", bd=5, relief=SUNKEN)
        frame.place(x=30,y=130, width=280, height=400)
        labl_head = Label(frame, text="Price of items", font=("arial", 15,), bg="orange",fg="black")
        labl_head.pack(pady=25)

        labl1 = Label(frame, text="sandwitch ..... Rs.60/plate",  font=("Segoe script", 10,), bg="orange",fg="black",)
        labl1.place(x=20,y=80, width=230, height=30)

        labl2 = Label(frame, text="cookies ..... Rs.30/plate", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl2.place(x=20,y=120, width=230, height=30)

        labl3 = Label(frame, text="tea ..... Rs.20/cup", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl3.place(x=20,y=160, width=230, height=30)

        labl4 = Label(frame, text="juice ..... Rs.25/glass", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl4.place(x=20,y=200, width=230, height=30)

        labl5 = Label(frame, text="pancakes ..... Rs.80/pack", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl5.place(x=20,y=240, width=230, height=30)

        labl6 = Label(frame, text="pastery ..... Rs.25/pastery", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl6.place(x=20,y=280, width=230, height=30)

        labl7 = Label(frame, text="special shake ..... Rs.100/glass", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl7.place(x=20,y=320, width=230, height=30)

        # frame 2
        frame2 = Frame(main, bg="orange", bd=5, relief=SUNKEN)
        frame2.place(x=370,y=130, width=250, height=400)
        labl_head2 = Label(frame2, text="Enter prices", font=("arial", 15,), bg="orange",fg="black")
        labl_head2.pack(pady=25)

        labl11 = Label(frame2, text="sandwitch ......", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl11.place(x=20,y=80, width=120, height=30)
        entry11 = Entry(frame2, font=("arial", 10,), bg="white",fg="black",)
        entry11.place(x=150,y=80, width=60, height=25)

        labl22 = Label(frame2, text="cookies ......", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl22.place(x=20,y=110, width=120, height=30)
        entry22 = Entry(frame2 ,font=("arial", 10,), bg="white",fg="black",)
        entry22.place(x=150,y=110, width=60, height=25)

        labl33 = Label(frame2, text="tea ......", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl33.place(x=20,y=140, width=120, height=30)
        entry33 = Entry(frame2, font=("arial", 10,), bg="white",fg="black",)
        entry33.place(x=150,y=140, width=60, height=25)

        labl44 = Label(frame2, text="juice ......", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl44.place(x=20,y=170, width=120, height=30)
        entry44 = Entry(frame2, font=("arial", 10,), bg="white",fg="black",)
        entry44.place(x=150,y=170, width=60, height=25)

        labl55 = Label(frame2, text="pancakes ......", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl55.place(x=20,y=200, width=120, height=30)
        entry55 = Entry(frame2, font=("arial", 10,), bg="white",fg="black",)
        entry55.place(x=150,y=200, width=60, height=25)

        labl66 = Label(frame2, text="pastery ......", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl66.place(x=20,y=230, width=120, height=30)
        entry66 = Entry(frame2, font=("arial", 10,), bg="white",fg="black",)
        entry66.place(x=150,y=230, width=60, height=25)

        labl77 = Label(frame2, text="special shake ...", font=("Segoe script", 10,), bg="orange",fg="black",)
        labl77.place(x=20,y=260, width=120, height=30)
        entry77 = Entry(frame2, font=("arial", 10,), bg="white",fg="black",)
        entry77.place(x=150,y=260, width=60, height=25)

        btn1 = Button(frame2, text="Reset", font=("arial", 10,), bg="#8fb18b",fg="white",command=reset_values,)
        btn1.place(x=20,y=320, width=100, height=30)

        btn2 = Button(frame2, text="Calculate", font=("arial", 10,), bg="#8fb18b",fg="white",command=calculate_values)
        btn2.place(x=130,y=320, width=100, height=30)

        # frame 3
        frame3 = Frame(main, bg="orange", bd=5, relief=SUNKEN)
        frame3.place(x=680,y=130, width=280, height=200)
        labl111 = Label(frame3, text="BILL",font=("Arial", 10,"bold"), bg="black",fg="White",)
        labl111.pack(ipady=20,fill=X)
        labl222 = Label(frame3, text="Total amount",font=("Arial", 13,), bg="orange",fg="black")
        labl222.place(x=20,y=100,width=100,height=30)
        labl3333 = Entry(frame3,text="Rs.",font=("Arial", 13,), bg="white",fg="blue",)
        labl3333.place(x=140,y=100,width=100,height=30)


        main.mainloop()
    elif input1=="" and input2=="":
        messagebox.showwarning("No input","Please fill the data")
    elif input1=="":   
        messagebox.showwarning("Input is missing","Please enter the username")
    elif input2=="":
        messagebox.showwarning("Input is missing","Please fill the password")
    elif input1!="admin" and input2!="123":
        messagebox.showerror("wrong input","username and password are incorrect")
    elif input1!="admin":
        messagebox.showerror("wrong input","username is incorrect")
    elif input2!="123":
        messagebox.showerror("wrong input","password is incorrect")
    else:
        pass
# heading
label=Label(root,text="Restaurant Management Login",bg="pink",fg="black",font=("verdana",20))
label.pack(pady=30,ipady=5,ipadx=17)

#image
img=PhotoImage(file="C:\\Users\\Dell\\Desktop\\Abdullah uet data\\python\\Restaurant management system\\imge.png")
labl=Label(root,image=img,bg="pink",).pack()

#user name and password
user_name = Label(root,text="user name : ",bg="pink",fg="black",font=("verdana",12,"bold"))
user_name.place(x=150,y=260)
password = Label(root,text="password : ",bg="pink",fg="black",font=("verdana",12,"bold"))
password.place(x=150,y=300)

user_name_entry = Entry(root,bg="white",fg="black",font=("verdana",12))
user_name_entry.place(x=300,y=260)
password_entry = Entry(root,bg="white",fg="black",font=("verdana",12,),show="*")
password_entry.place(x=300,y=300)

#buttons
btn1 = Button(root,text="Login",width=8,height=1,bg="red",fg="black",font=("verdana",10),command=login)
btn1.place(x=190,y=380)
btn2 = Button(root,text="Reset",width=8,height=1,bg="#5e85d1",fg="black",font=("verdana",10),command=reset)
btn2.place(x=290,y=380)
btn3 = Button(root,text="Exit",width=8,height=1,bg="Yellow",fg="black",font=("verdana",10),command=exitt)
btn3.place(x=390,y=380)

#end of code
root.mainloop()