import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox


# creating database
con = sqlite3.connect("ACME.db")

#creating table inside database
try:
    con.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY   AUTOINCREMENT, name TEXT NOT NULL, email TEXT, section TEXT NOT NULL, roll TEXT NOT NULL UNIQUE, address  TEXT NOT NULL, gender TEXT, semester TEXT, cgpa TEXT);")
except sqlite3.Error as er:
    messagebox.showinfo("Error", "Something went wrong")


#insertion of student record to the database

def insert_data(name, email, section, roll, address,gender,semester,cgpa):
    conn = sqlite3.connect("ACME.db")
    flag=True
    try:    
        conn.execute("INSERT INTO student(name, email, section, roll, address,gender,semester,cgpa) VALUES( '" + name + "', '" + email +
                 "', '" + section + "', '" + roll + "', '" + address + "', '" + gender + "', '" + semester + "', '" + cgpa + "' );")
        conn.commit()
    except sqlite3.Error as er:
        messagebox.showinfo("Error", "Something went wrong") 
        flag=False   
    conn.close()
    if(flag):
        messagebox.showinfo("Success", "Record Inserted Successfully.")

#insert details gui
options = [
  "Male",
  "FeMale"
]
classes=[
"BSIT",
"BSCS",
"BSSE"
]

semesters=["1st","2nd","3rd","4th","5th","6th","7th" ,"8th"]
cgpas=["1.0","1.25","1.5","1.75","2.0","2.25","2.5","2.75","3.0","3.25","3.5","3.75","4.0"]
def insert():
    add_window = tk.Tk()
    add_window.title("Insert Student Details")
    add_window.configure(bg='#132c33')
    tk.Label(add_window,bg='#132c33',fg="white").grid(row=0, column=0, columnspan=2)
    tk.Label(add_window, text="Student Name:",bg='#132c33',fg="white").grid(row=1, column=0)
    name_entry = tk.Entry(add_window, width=50)
    name_entry.grid(row=1, column=1, padx=25)
    tk.Label(add_window, text="Email:",bg='#132c33',fg="white").grid(row=2, column=0)
    email_entry = tk.Entry(add_window, width=50)
    email_entry.grid(row=2, column=1, padx=25)
    tk.Label(add_window, text="Section:",bg='#132c33',fg="white").grid(row=3, column=0)
   
    cls_clicked = tk.StringVar(add_window) 
    cls_clicked.set( "BSIT" )
    class_entry = tk.OptionMenu( add_window , cls_clicked , *classes )
    class_entry.grid(row=3, column=1)
    class_entry.config(width=36, font=("Georgia", 12))


    tk.Label(add_window, text="Roll Number:",bg='#132c33',fg="white").grid(row=4, column=0, padx=20)
    roll_entry = tk.Entry(add_window, width=50)
    roll_entry.grid(row=4, column=1, padx=25)
    tk.Label(add_window, text="Address:",bg='#132c33',fg="white").grid(row=5, column=0)
    address_entry = tk.Entry(add_window, width=50)
    address_entry.grid(row=5, column=1, padx=25)

    tk.Label(add_window, text="Gender:",bg='#132c33',fg="white").grid(row=6, column=0)
    clicked = tk.StringVar(add_window) 
    clicked.set( "Male" )
    drop = tk.OptionMenu( add_window , clicked , *options )
    drop.grid(row=6, column=1)
    drop.config(width=36, font=("Georgia", 12))



    tk.Label(add_window, text="Semester:",bg='#132c33',fg="white").grid(row=7, column=0)
   
    sem_clicked = tk.StringVar(add_window) 
    sem_clicked.set( "1st" )
    sem_entry = tk.OptionMenu( add_window , sem_clicked , *semesters )
    sem_entry.grid(row=7, column=1)
    sem_entry.config(width=36, font=("Georgia", 12))


    tk.Label(add_window, text="Section:",bg='#132c33',fg="white").grid(row=8, column=0)
   
    cgpa_clicked = tk.StringVar(add_window) 
    cgpa_clicked.set( "1.0" )
    cgpa_entry = tk.OptionMenu( add_window , cgpa_clicked , *cgpas )
    cgpa_entry.grid(row=8, column=1)
    cgpa_entry.config(width=36, font=("Georgia", 12))


    tk.Button(add_window, text='Submit', activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white", command=lambda: submit()).grid(row=9, column=0, columnspan=2, pady=10)

    def submit():
        name = name_entry.get()
        email = email_entry.get()
        section = cls_clicked.get()
        roll = str(roll_entry.get())
        address = str(address_entry.get())
        gender=clicked.get()
        semester=sem_clicked.get()
        cgpa=cgpa_clicked.get()
        if(len(name)==0 or len(email)==0  or len(roll)==0 or len(address)==0 ):
            messagebox.showinfo("Error", "Empty Feild")
            return
        insert_data(name, email, section, roll, address,gender,semester,cgpa)
        add_window.destroy()

    add_window.mainloop()

#Display of results in a table

def display():
    connn = sqlite3.connect("ACME.db")
    display_window = tk.Tk()
    display_window.title("Students Database")
    display_window.configure(bg='#132c33')
    table = ttk.Treeview(display_window,selectmode="extended")
    table["columns"] = ("one", "two", "three", "four", "five","six","seven","eight")
    table.column("one",minwidth=0,width=135)
    table.heading("one", text="Name")
    table.column("two",minwidth=0,width=135)
    table.heading("two", text="Email")
    table.column("three",minwidth=0,width=135)
    table.heading("three", text="Section")
    table.column("four",minwidth=0,width=135)
    table.heading("four", text="Roll No")
    table.column("five",minwidth=0,width=135)
    table.heading("five", text="Address")
    table.column("six",minwidth=0,width=135)
    table.heading("six", text="Gender")
    table.column("seven",minwidth=0,width=135)
    table.heading("seven", text="Semester")
    table.column("eight",minwidth=0,width=135)
    table.heading("eight", text="Cgpa")
    cursor = connn.execute("SELECT rowid,* FROM student;")
    i = 0
    for row in cursor:
        table.insert('', i, text="Student " + str(row[1]), values=(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
        i = i + 1
    table.pack()
    connn.close()


#updation of record in a table

def update():
    update_window = tk.Tk()
    update_window.title("Update Student Details")
    update_window.configure(bg='#132c33')
    tk.Label(update_window, text="Insert Roll Number of Student :",bg='#132c33',fg="white").grid(row=0, column=0, sticky="W", padx=10, columnspan=2)
    s_id = tk.Entry(update_window, width=50)
    s_id.grid(row=1, column=0, sticky="W", padx=10, columnspan=2)
    tk.Button(update_window, text="Search", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: fillup()).grid(row=1, column=2,padx=5, pady=10)

    tk.Label(update_window, text="\nEnter the new values:",bg='#132c33',fg="white").grid(row=2, column=0, sticky="W", padx=10, pady=10, columnspan=2)
    tk.Label(update_window, text="Name:",bg='#132c33',fg="white").grid(row=3, column=0, sticky="W", padx=10, pady=10)
    s_name = tk.Entry(update_window, width=50)
    s_name.grid(row=3, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Email:",bg='#132c33',fg="white").grid(row=4, column=0, sticky="W", padx=10, pady=10)
    s_email = tk.Entry(update_window, width=50)
    s_email.grid(row=4, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Section:",bg='#132c33',fg="white").grid(row=5, column=0, sticky="W", padx=10, pady=10)
   
    cls_clicked = tk.StringVar(update_window) 
    cls_clicked.set( "BSIT" )
    class_entry = tk.OptionMenu( update_window , cls_clicked , *classes )
    class_entry.grid(row=5, column=1)
    class_entry.config(width=36, font=("Georgia", 12))

    tk.Label(update_window, text="Roll No:",bg='#132c33',fg="white").grid(row=6, column=0, sticky="W", padx=10, pady=10)
    s_roll = tk.Entry(update_window, width=50)
    s_roll.grid(row=6, column=1, sticky="W", padx=10, pady=10)
    
    tk.Label(update_window, text="Address:",bg='#132c33',fg="white").grid(row=7, column=0, sticky="W", padx=10, pady=10)
    s_address = tk.Entry(update_window, width=50)
    s_address.grid(row=7, column=1, sticky="W", padx=10, pady=10)
    
    tk.Label(update_window, text="Gender:",bg='#132c33',fg="white").grid(row=8, column=0)
    clicked = tk.StringVar(update_window) 
    clicked.set( "Male" )
    drop = tk.OptionMenu( update_window , clicked , *options )
    drop.grid(row=8, column=1)
    drop.config(width=36, font=("Georgia", 12))


    tk.Label(update_window, text="Semester:",bg='#132c33',fg="white").grid(row=9, column=0)
   
    sem_clicked = tk.StringVar(update_window) 
    sem_clicked.set( "1st" )
    sem_entry = tk.OptionMenu( update_window , sem_clicked , *semesters )
    sem_entry.grid(row=9, column=1)
    sem_entry.config(width=36, font=("Georgia", 12))


    tk.Label(update_window, text="Section:",bg='#132c33',fg="white").grid(row=10, column=0)
   
    cgpa_clicked = tk.StringVar(update_window) 
    cgpa_clicked.set( "1.0" )
    cgpa_entry = tk.OptionMenu( update_window , cgpa_clicked , *cgpas )
    cgpa_entry.grid(row=9, column=1)
    cgpa_entry.config(width=36, font=("Georgia", 12))
    
    tk.Button(update_window, text="Update", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=11, column=0, padx=10, pady=10, columnspan=2)

    def fillup():
        flag=True 
        sid = s_id.get()       
        try: 
            connn = sqlite3.connect("ACME.db")
            cursor = connn.execute("SELECT * FROM student where roll='"+sid+"';")
            connn.commit()
            for row in cursor:
                s_name.insert(0,str(row[1]))
                s_email.insert(0,str(row[2]))        
                cls_clicked.set(str(row[3]))
                s_roll.insert(0,str(row[4]))
                s_address.insert(0,str(row[5]))
                s_roll.config(state='disabled')
                clicked.set(str(row[6]) )
                sem_clicked.set(str(row[7]) )
                cgpa_clicked.set(str(row[8]) )
                
        except sqlite3.Error as er:
            messagebox.showinfo("Error", "No Record Found")
        connn.close()


    def submit():
        sid = s_id.get()
        sname = s_name.get()
        semail = s_email.get()
        ssection = cls_clicked.get()
        sroll = s_roll.get()
        saddress = s_address.get()
        gender=clicked.get()
        semester=sem_clicked.get()
        cgpa=cgpa_clicked.get()
        if(len(sname)==0 or len(semail)==0  or len(sroll)==0 or len(saddress)==0 ):
            messagebox.showinfo("Error", "Empty Feild")
            return
        scon = sqlite3.connect("ACME.db")
        flag=True        
        try:        
            scon.execute("UPDATE student SET name = '" + sname + "',email = '" + semail + "', section = '" + ssection +
                     "', address = '" + saddress + "', gender = '" + gender + "', semester = '" + semester + "', cgpa = '" + cgpa + "' WHERE roll = '" + sid + "';")
            scon.commit()
        except sqlite3.Error as er:
            messagebox.showinfo("Error", "Something went wrong")
            flag=False        
        scon.close()
        if(flag):
            messagebox.showinfo("Success", "Record Updated Successfully.")
        update_window.destroy()
    update_window.mainloop()




#deletion record gui

def delete():
    delete_window = tk.Tk()
    delete_window.title("Delete Student ")
    delete_window.configure(bg='#132c33')
    tk.Label(delete_window, text="Enter Student Roll Number whose details are to be removed:",bg='#132c33',fg="white").grid(row=0, column=0, padx=10, pady=10)
    d_roll = tk.Entry(delete_window, width=50)
    d_roll.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(delete_window, text="Delete Details", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=1, column=0, columnspan=2)
    tk.Label(delete_window,bg='#132c33',fg="white").grid(row=2, column=0, columnspan=2)

    def submit():
        droll = d_roll.get()
        if(len(droll)==0 ):
            messagebox.showinfo("Error", "Empty Feild")
            return
        dcon = sqlite3.connect("ACME.db")
        flag=True
        try:        
            dcon.execute("DELETE FROM student WHERE roll = '" + droll+"';")
            dcon.commit()
            dcon.execute("VACUUM;")
            dcon.commit()
        except sqlite3.Error as er:
            messagebox.showinfo("Error", "Something went wrong")  
            flag=False      
        dcon.close()
        if(flag):
            messagebox.showinfo("Success", " Record Deleted Successfully.")
        delete_window.destroy()
    delete_window.mainloop()


#finding student details gui

def search():
    search_window = tk.Tk()
    search_window.title("Search Student Details")
    search_window.configure(bg='#132c33')
    tk.Label(search_window, text="Enter the Roll Number of Student whose details are to be searched:",bg='#132c33',fg="white").grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    f_roll = tk.Entry(search_window, width=50)
    f_roll.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:",bg='#132c33',fg="white").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window,bg='#132c33',fg="white").grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    details = ttk.Treeview(search_window,selectmode="extended")
    details["columns"] = ("one", "two", "three", "four", "five","six","seven","eight")

    details.column("one",minwidth=0,width=135)
    details.heading("one", text="Name")
    details.column("two",minwidth=0,width=135)
    details.heading("two", text="Email")
    details.column("three",minwidth=0,width=135)
    details.heading("three", text="Section")
    details.column("four",minwidth=0,width=135)
    details.heading("four", text="Roll No")
    details.column("five",minwidth=0,width=135)
    details.heading("five", text="Address")
    details.column("six",minwidth=0,width=135)
    details.heading("six", text="Gender")
    details.column("seven",minwidth=0,width=135)
    details.heading("seven", text="Semester")
    details.column("eight",minwidth=0,width=135)
    details.heading("eight", text="Cgpa")

    def submit():
        for row in details.get_children():
            details.delete(row)

        froll = f_roll.get()
        fcon = sqlite3.connect("ACME.db")
        cursor = fcon.execute("SELECT rowid,* from student WHERE roll = '" + froll + "';")
        fcon.commit()

        i = 0
        for row in cursor:
            details.insert('', i, text="Student " + str(row[1]), values=(row[2], row[3], row[4], row[5], row[6],row[7], row[8],row[9]))
            i = i + 1
        
        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        fcon.close()
    search_window.mainloop()



con.close()


