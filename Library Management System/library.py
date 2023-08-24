from tkinter import *
import tkinter.messagebox as msg

class multiple():
    def __init__(self,root):
        self.root=root
        self.root.geometry("550x550")
        self.root.title("Library Management System")
        self.root.config(bg="powderblue")

        title=Label(self.root,text="Home Page", bg="powderblue", font=("bold","30"))
        title.pack()

        admin_button=Button(self.root,text="Admin", command = self.admin_page)
        admin_button.place(x=270,y=150)

        user_button=Button(self.root,text="User", command = self.user_page)
        user_button.place(x=270,y=350)

    def admin_page(self):
        window=Tk()
        window.title("Admin page")
        window.geometry("600x550")
        window.config(bg="powderblue")

        book_name_label=Label(window,text="Book name:",bg="powderblue", font=("bold",'15'))
        book_name_label.place(x=170,y=150)

        author_name_label=Label(window,text="Author name:",bg="powderblue", font=("bold",'15'))
        author_name_label.place(x=170,y=250)

        quantity_label=Label(window,text="Quantity:",bg="powderblue", font=("bold",'15'))
        quantity_label.place(x=170,y=350)

        self.book_entry=Entry(window)
        self.book_entry.place(x=300, y=155)

        self.author_entry=Entry(window)
        self.author_entry.place(x=300, y=255)

        self.quantity_entry=Entry(window)
        self.quantity_entry.place(x=300, y=355)

        admin_submit=Button(window,text="Submit", command=self.admin_data)
        admin_submit.place(x=270,y=455)

    def user_page(self):
        window1=Tk()
        window1.title("User page")
        window1.geometry("600x450")
        window1.config(bg="powderblue")

        user_book_name_label=Label(window1,text="Book name:",bg="powderblue", font=("bold",'15'))
        user_book_name_label.place(x=170,y=150)

        user_author_name_label=Label(window1,text="Author name:",bg="powderblue", font=("bold",'15'))
        user_author_name_label.place(x=170,y=250)

        self.user_book_entry=Entry(window1)
        self.user_book_entry.place(x=300, y=155)

        self.user_author_entry=Entry(window1)
        self.user_author_entry.place(x=300, y=255)

        user_submit=Button(window1,text="Submit", command=self.user_data)
        user_submit.place(x=270,y=400)

    def admin_data(self):
        import mysql.connector

        mydb=mysql.connector.connect(host="localhost", port=3306, user='root',password='tubelight', database='library_management')
        mycursor= mydb.cursor()

        book_name=self.book_entry.get()
        authorname=self.author_entry.get()
        qty=self.quantity_entry.get()

        mycursor.execute("insert into admin values(%s,%s,%s)",(book_name,authorname,qty))
        mydb.commit()
        msg.showinfo("Admin Books","Book added to stock")

    def user_data(self):
        import mysql.connector

        mydb=mysql.connector.connect(host="localhost", port=3306, user='root',password='tubelight', database='library_management')
        mycursor= mydb.cursor()

        book_name=self.user_book_entry.get()
        author=self.user_author_entry.get()

        mycursor.execute("select quantity from admin where book_name=%s and author=%s",(book_name,author))
    
        q=0
        for i in mycursor:
            q=int(i[0])
        if q>=1:
            q=q-1
            mycursor.execute("Update admin set quantity=%s where book_name=%s and author=%s",(q, book_name,author))
            mycursor.execute("insert into user value(%s,%s)",(book_name,author))
            mydb.commit()
            msg.showinfo("Book Availability","Book available")

        else:
            msg.showerror("Book Availability","Book not available")




root=Tk()

obj=multiple(root)

root.mainloop()