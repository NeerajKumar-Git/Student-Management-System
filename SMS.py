from tkinter import * 
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1366x768+0+0')

        # Declaring Variables =============================================================>>

        self.roll_number = StringVar()
        self.name_var = StringVar()
        self.contact_var = StringVar()
        self.gender_var = StringVar()
        self.mail_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()
        # ===============================================================>>

        set_title = Label(self.root,text='Student Management System',font=('times new roman',35,'bold'))
        set_title.pack(side=TOP)

        # =================================================================>>

        student_frame=Frame(self.root,bg='steelblue')
        student_frame.place(x=20,y=70,width=550,height=650)

        student_title = Label(student_frame,text='Student Details Editor',bg='steelblue',fg='snow',font=('times new roman',25,'bold'))
        student_title.grid(row=0,columnspan=2,pady=20)

        rollnumber = Label(student_frame,text='Roll Number: ',bg='steelblue',fg='snow',font=('times new roman',22,'bold'))
        rollnumber.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        rollnumber_input = Entry(student_frame,textvariable=self.roll_number,width=20,bd=3,relief=GROOVE,font=("",22))
        rollnumber_input.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        name = Label(student_frame,text='Name: ',fg='snow',bg='steelblue',font=('times new roman',22,'bold'))
        name.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        name_input = Entry(student_frame,bd=3,textvariable=self.name_var,relief=GROOVE,width=20,font=("",22))
        name_input.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        mail = Label(student_frame,text='Email: ',bg='steelblue',fg='snow',font=('times new roman',22,'bold'))
        mail.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        mail_input = Entry(student_frame,width=20,bd=3,textvariable=self.mail_var,relief=GROOVE,font=("",22))
        mail_input.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        gender = Label(student_frame,text='Gender: ',bg='steelblue',fg='snow',font=('times new roman',22,'bold'))
        gender.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        gender_input = ttk.Combobox(student_frame,width=19,textvariable=self.gender_var,state='readonly',font=("",22))
        gender_input['values']=('Male',"Female","Other")
        gender_input.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        contact = Label(student_frame,text='Contact: ',bg='steelblue',fg='snow',font=('times new roman',22,'bold'))
        contact.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        contact_input = Entry(student_frame,bd=3,textvariable=self.contact_var,relief=GROOVE,width=20,font=("",22))
        contact_input.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        date = Label(student_frame,text='D.O.B: ',bg='steelblue',fg='snow',font=('times new roman',22,'bold'))
        date.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        date_input = Entry(student_frame,bd=3,textvariable=self.dob_var,relief=GROOVE,width=20,font=("",22))
        date_input.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        address = Label(student_frame,text='Address: ',bg='steelblue',fg='snow',font=('times new roman',22,'bold'))
        address.grid(row=7,column=0,padx=10,pady=10,sticky=W)

        self.address_input = Text(student_frame,bd=3,relief=GROOVE,height=2,width=20,font=("",22))
        self.address_input.grid(row=7,column=1,padx=10,pady=10,sticky=W)
        # ==================================================================>>

        btn_frame = Frame(student_frame,bg='steelblue')
        btn_frame.place(x=15,y=550)

        Addbtn = Button(btn_frame,width=13,text='Add',font=('',10,'bold'),cursor='hand2',command=self.add_students)
        Addbtn.grid(row=0,column=0,padx=7,pady=5)

        delbtn = Button(btn_frame,width=13,command=self.delete_data,text='Delete',font=('',10,'bold'),cursor='hand2')
        delbtn.grid(row=0,column=1,padx=7,pady=5)

        updbtn = Button(btn_frame,width=13,command=self.update_data,text='Update',font=('',10,'bold'),cursor='hand2')
        updbtn.grid(row=0,column=2,padx=7,pady=5)

        clrbtn = Button(btn_frame,width=13,command=self.clear,text='Clear',font=('',10,'bold'),cursor='hand2')
        clrbtn.grid(row=0,column=3,padx=7,pady=5)


        # ==================================================================>>
        details_frame=Frame(self.root,bg='steelblue')
        details_frame.place(x=550+20+20,y=70,width=750,height=650)
        #=====================================================================>>

        search_label = Label(details_frame,text='Search By: ',bg='steelblue',fg='snow',font=('times new roman',15,'bold'))
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        search_input = ttk.Combobox(details_frame,textvariable=self.search_by,width=10,state='readonly',font=("",12))
        search_input['values']=('Roll_Number',"Name","Contact")
        search_input.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        txt_input = Entry(details_frame,textvariable=self.search_text,bd=2,relief=GROOVE,width=18,font=("",12))
        txt_input.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        searchbtn = Button(details_frame,command=self.search_data,width=13,text='Search',font=('',10,'bold'),cursor='hand2')
        searchbtn.grid(row=0,column=3,padx=10,pady=10)

        showallbtn = Button(details_frame,width=13,text='Show All',command=self.fetch_data,font=('',10,'bold'),cursor='hand2')
        showallbtn.grid(row=0,column=4,padx=10,pady=10)
        # ============Table Frame=================================================================>>

        table_frame = Frame(details_frame,bd=5,relief=RIDGE,bg='steelblue')
        table_frame.place(x=11,y=50,width=750-20,height=650-60)

        # ============Tree View====================================================================>>
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # =====================================================================>>
        
        self.student_table['columns']=['Roll_Number','Name','Mail','Gender','Contact','DOB','Address']
        self.student_table['show']='headings'

        self.student_table.heading('Roll_Number',text='Roll Number: ')
        self.student_table.heading('Name',text='Name: ')
        self.student_table.heading('Mail',text='Email: ')
        self.student_table.heading('Gender',text='Gender: ')
        self.student_table.heading('Contact',text='Contact: ')
        self.student_table.heading('DOB',text='D.O.B: ')
        self.student_table.heading('Address',text='Address: ')

        self.student_table.column('Roll_Number',width = 85)
        self.student_table.column('Name',width = 150)
        self.student_table.column('Mail',width = 200)
        self.student_table.column('Gender',width = 70)
        self.student_table.column('Contact',width = 100)
        self.student_table.column('DOB',width = 150)
        self.student_table.column('Address',width =150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


        # ===============================================================================>>
        
    def add_students(self):
        if self.roll_number.get()=="" or self.name_var.get()==""  or self.contact_var.get()=="" or self.dob_var.get()=="" or self.gender_var.get()=="":
            messagebox.showerror('Error','All Fields are Required!!')
        if not '@' in self.mail_var.get() :
            messagebox.showerror('Error','Please Enter a Valid MailID')
        if not '.' in self.mail_var.get() :
            messagebox.showerror('Error','Please Enter a Valid MailID')
        if self.mail_var.get().endswith('.'):
            messagebox.showerror('Error','Please Enter a Valid MailID')

        if len(self.contact_var.get())!=10:
            messagebox.showerror('Error','Please Enter a Valid Contact Number')
        else:
            con = pymysql.connect(host='localhost',user='root',password='',database='SMS')
            cur = con.cursor()
            cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s)',(
                                        self.roll_number.get(),
                                        self.name_var.get(),
                                        self.mail_var.get(),
                                        self.gender_var.get(),
                                        self.contact_var.get(),
                                        self.dob_var.get(),
                                        self.address_input.get('1.0',END)
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Successful",'Record has been inserted')
    #get data into table from database=================================================>>
 
    def fetch_data(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='SMS')
        cur = con.cursor()
        cur.execute('select * from students')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    #clear data after adding the details================================================>>

    def clear(self):
        self.roll_number.set("")
        self.name_var.set("")
        self.contact_var.set("")
        self.gender_var.set("")
        self.mail_var.set("")
        self.dob_var.set("")
        self.address_input.delete("1.0",END)

    #get data from the details to the student editor
    
    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.roll_number.set(row[0])
        self.name_var.set(row[1])
        self.contact_var.set(row[4])
        self.gender_var.set(row[3])
        self.mail_var.set(row[2])
        self.dob_var.set(row[5])
        # self.address_input.delete("1.0",END)
        self.address_input.insert(END,row[6])

    def update_data(self):
        if self.roll_number.get()=="" or self.name_var.get()==""  or self.contact_var.get()=="" or self.dob_var.get()=="" or self.gender_var.get()=="":
            messagebox.showerror('Error','All Fields are Required!!')
        if not '@' in self.mail_var.get():
            messagebox.showerror('Error','Please Enter a Valid MailID')
        if not '.' in self.mail_var.get() :
            messagebox.showerror('Error','Please Enter a Valid MailID')
        if self.mail_var.get().endswith('.'):
            messagebox.showerror('Error','Please Enter a Valid MailID')

        if len(self.contact_var.get())!=10:
            messagebox.showerror('Error','Please Enter a Valid Contact Number')
        else:
            con = pymysql.connect(host='localhost',user='root',password='',database='SMS')
            cur = con.cursor()
            cur.execute('update students set Name=%s,Mail=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where Roll_Number=%s',(
                                        self.name_var.get(),
                                        self.mail_var.get(),
                                        self.gender_var.get(),
                                        self.contact_var.get(),
                                        self.dob_var.get(),
                                        self.address_input.get('1.0',END),
                                        self.roll_number.get()
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()


    def delete_data(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='SMS')
        cur = con.cursor()
        cur.execute('delete from students where Roll_Number=%s',self.roll_number.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='SMS')
        cur = con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


root=Tk()
obj = Student(root)
root.mainloop()