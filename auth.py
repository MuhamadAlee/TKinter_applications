from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import tkinter as tk
import Students as sd
import Course as cr
import Teachers as tr
import StudentCourseTeacher as sct

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('ACME.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()

#main Class
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        self.master.configure(bg='#132c33')
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        if(len(self.username.get())==0 or len(self.password.get())==0  ):
            messagebox.showinfo("Error", "Empty Feild")
            return
        with sqlite3.connect('ACME.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            
            self.logf.destroy()
            self.head.destroy()


            

           ###################################### Loadin Menu Items in case of successful login ##################################################################
            
            m1 = PanedWindow(self.master,orient=VERTICAL)
            m1.pack(fill=BOTH, expand=2)


            label_1 = tk.Label(m1, text="\n  ACME UNIVERSITY STUDENT MANAGEMENT PORTAL \n", font=("Georgia", 30),bg="#132c33", fg="white",height=3, width =150)
            label_1.pack()
            m1.add(label_1)
            ####################################################################################################################################################
            
            m2 = PanedWindow(m1, orient=HORIZONTAL)
            m1.add(m2)
            ##########################################111111##############################
            m3 = PanedWindow(m2, orient=VERTICAL)
            m2.add(m3)
            
            button_1 = tk.Button(m3, text="Add Student", command=lambda: sd.insert(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white" )
            button_1.pack()

            m3.add(button_1)
            button_2 = tk.Button(m3, text="Update Student Details", command=lambda: sd.update(),height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_2.pack()
            m3.add(button_2)
            button_3 = tk.Button(m3, text="View Student Details", command=lambda: sd.display(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_3.pack()
            m3.add(button_3)
            button_4 = tk.Button(m3, text="Delete Student", command=lambda: sd.delete(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_4.pack()
            m3.add(button_4)

            button_5 = tk.Button(m3, text="Search Student", command=lambda: sd.search(),height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_5.pack()
            m3.add(button_5)
            button_6 = tk.Button(m3, text="Details", command=lambda: sct.Student_search(),height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_6.pack()
            m3.add(button_6)
###############################################################################
            m4 = PanedWindow(m2, orient=VERTICAL)
            m2.add(m4)




            button_1 = tk.Button(m4, text="Add Course", command=lambda: cr.insert(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white" )
            button_1.pack()

            m4.add(button_1)
            button_2 = tk.Button(m4, text="Update Course Details", command=lambda: cr.update(),height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_2.pack()
            m4.add(button_2)
            button_3 = tk.Button(m4, text="View Course Details", command=lambda: cr.display(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_3.pack()
            m4.add(button_3)
            button_4 = tk.Button(m4, text="Delete Course", command=lambda: cr.delete(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_4.pack()
            m4.add(button_4)

            button_5 = tk.Button(m4, text="Search Course", command=lambda: cr.search(),height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_5.pack()
            m4.add(button_5)
            button_6 = tk.Button(m4, text="Details", command=lambda: sct.Course_search(),height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_6.pack()
            m4.add(button_6)




####################################################################################################################################
###############################################################################
            m5 = PanedWindow(m2, orient=VERTICAL)
            m2.add(m5)




            button_1 = tk.Button(m5, text="Add Teacher", command=lambda: tr.insert(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white" )
            button_1.pack()

            m5.add(button_1)
            button_2 = tk.Button(m5, text="Update Teacher Details", command=lambda: tr.update(),height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_2.pack()
            m5.add(button_2)
            button_3 = tk.Button(m5, text="View Teacher Details", command=lambda: tr.display(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_3.pack()
            m5.add(button_3)
            button_4 = tk.Button(m5, text="Delete Teacher", command=lambda: tr.delete(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_4.pack()
            m5.add(button_4)

            button_5 = tk.Button(m5, text="Search Teacher", command=lambda: tr.search(),height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_5.pack()
            m5.add(button_5)
            button_6 = tk.Button(m5, text="Details", command=lambda: sct.Teacher_search(),height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_6.pack()
            m5.add(button_6)



########################################################################################################################################


            m6 = PanedWindow(m2, orient=VERTICAL)
            m2.add(m6)




            button_1 = tk.Button(m6, text="Add Details", command=lambda: sct.insert(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white" )
            button_1.pack()
            m6.add(button_1)

            
            button_3 = tk.Button(m6, text="View Teacher Details", command=lambda: sct.display(), height=3,width=37,
                                 activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
            button_3.pack()
            m6.add(button_3)
            button_4 = tk.Button(m6, text="Logout", command=lambda: self.master.destroy(), height=3,width=37,
                                 activebackground='red', activeforeground='white',bg='#126e82',fg="white")
            button_4.pack()
            m6.add(button_4)

          













            

            label_2 = tk.Label(self.master, text="\n",bg="#132c33")
            label_2.pack()
############################################################### End Loading Menu Items #########################################################
        else:
            ms.showerror('Oops!','Username Not Found.')

            
    def new_user(self):
        if(len(self.n_username.get())==0 or len(self.n_password.get())==0  ):
            messagebox.showinfo("Error", "Empty Feild")
            return
        flag=True
    	#Establish Connection
        with sqlite3.connect('ACME.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user,[(self.n_username.get())])        
        if c.fetchall():
#            ms.showerror('Error!','Username Taken Try a Diffrent One.')
            flag=False
        
        find_user = ('SELECT * FROM user')
        c.execute(find_user)        
        if c.fetchall():
#            ms.showerror('Error!','Username Taken Try a Diffrent One.')
            flag=False


        if flag:
                 
            self.log()
            #Create New Account 
            insert = 'INSERT INTO user(username,password) VALUES(?,?)'
            c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
            db.commit()
            ms.showinfo('Success!','Account Created!')
        
        else:
            ms.showerror('Error!','Username Taken Try a Diffrent One.')

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        
        self.head = Label(self.master,text = 'LOGIN',bg='#132c33',fg='white',font=("Georgia", 20),pady = 10)
        self.head.pack()
        
        self.logf = Frame(self.master,padx =10,pady = 10)
        self.logf.configure(bg='#132c33')
        Label(self.logf,text = 'Username: ',bg='#132c33',fg='white',font=("Georgia", 12),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,font=("Georgia", 12)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',bg='#132c33',fg='white',font=("Georgia", 12),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,font=("Georgia", 12),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white" ,font=("Georgia", 12),height=1,width=15,command=self.login).grid(row=4,column=1)
        Button(self.logf,text = ' Create Account ',activebackground='#51c4d3', activeforeground='white',bg='#132c33',fg="white" ,font=("Georgia", 12),height=1,width=12,command=self.cr).grid(row=4,column=0)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        self.crf.configure(bg='#132c33')
        Label(self.crf,text = 'Username: ',bg='#132c33',fg='white',font=("Georgia", 12),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,font=("Georgia", 12)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',bg='#132c33',fg='white',font=("Georgia", 12),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,font=("Georgia", 12),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Register',activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white" ,font=("Georgia", 12),height=1,width=15,command=self.new_user).grid(row=4,column=1)
        Button(self.crf,text = 'Go to Login',activebackground='#51c4d3', activeforeground='white',bg='#132c33',fg="white",font=("Georgia", 12),height=1,width=12,command=self.log).grid(row=4,column=0)


