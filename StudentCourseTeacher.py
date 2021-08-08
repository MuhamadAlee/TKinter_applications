import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox


# creating database
con = sqlite3.connect("ACME.db")
#creating table inside database
try:
    con.execute("CREATE TABLE IF NOT EXISTS details(id INTEGER PRIMARY KEY   AUTOINCREMENT, student TEXT NOT NULL,  course TEXT NOT NULL, teacher TEXT NOT NULL,result TEXT NOT NULL);")
except sqlite3.Error as er:
    messagebox.showinfo("Error", "Something went wrong")


#insertion of Teacher record to the database

def insert_data(student,course, teacher,result):
    conn = sqlite3.connect("ACME.db")
    flag=True
    try:    
        conn.execute("INSERT INTO details(student,course,teacher,result) VALUES( '" + student + "', '" + course +
                 "', '" + teacher + "', '" + result + "' );")
        conn.commit()
    except sqlite3.Error as er:
        messagebox.showinfo("Error", "Something went wrong") 
        flag=False   
    conn.close()
    if(flag):
        messagebox.showinfo("Success", "Record Inserted Successfully.")

#insert details gui

students=["NA"]
courses=["NA"]
teachers=["NA"]

def student():
    
    connn = sqlite3.connect("ACME.db")
    cursor = connn.execute("SELECT name FROM student;")
    for row in cursor:
        if(row[0] not in students):
            students.append(row[0])
    connn.close()
    

def course():
    
    connn = sqlite3.connect("ACME.db")
    cursor = connn.execute("SELECT title FROM course;")
    for row in cursor:
        if(row[0] not in courses):
            courses.append(row[0])
    connn.close()
    

def teacher():
    
    connn = sqlite3.connect("ACME.db")
    cursor = connn.execute("SELECT title FROM teacher;")
    for row in cursor:
        if(row[0] not in teachers):
            teachers.append(row[0])
    connn.close()
    






    

def insert():
    
    student()
    course()
    teacher()



    add_window = tk.Tk()
    add_window.title("Insert Details")
    add_window.configure(bg='#132c33')
    
    tk.Label(add_window, text="Student:",bg='#132c33',fg="white").grid(row=0, column=0)
   
    st_clicked = tk.StringVar(add_window) 
    st_clicked.set( "NA" )
    st_entry = tk.OptionMenu( add_window , st_clicked , *students )
    st_entry.grid(row=0, column=1)
    st_entry.config(width=36, font=("Georgia", 12))
    
    tk.Label(add_window, text="Course:",bg='#132c33',fg="white").grid(row=1, column=0)
    cr_clicked = tk.StringVar(add_window) 
    cr_clicked.set( "NA" )
    cr_entry = tk.OptionMenu( add_window , cr_clicked , *courses )
    cr_entry.grid(row=1, column=1)
    cr_entry.config(width=36, font=("Georgia", 12))

    
    tk.Label(add_window, text="Teacher:",bg='#132c33',fg="white").grid(row=2, column=0)
    tr_clicked = tk.StringVar(add_window) 
    tr_clicked.set( "NA" )
    tr_entry = tk.OptionMenu( add_window , tr_clicked , *teachers )
    tr_entry.grid(row=2, column=1)
    tr_entry.config(width=36, font=("Georgia", 12))


    tk.Label(add_window, text="Result:",bg='#132c33',fg="white").grid(row=3, column=0, padx=20)
    sct_result = tk.Entry(add_window, width=50)
    sct_result.grid(row=3, column=1, padx=25)
    
    tk.Button(add_window, text='Submit', activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white", command=lambda: submit()).grid(row=4, column=0, columnspan=2, pady=10)

    def submit():
        student = st_clicked.get()
        course = cr_clicked.get()
        teacher = tr_clicked.get()
        result=str(sct_result.get())
        if(len(result)==0 ):
            messagebox.showinfo("Error", "Empty Feild")
            return
        insert_data(student,course,teacher,result)
        add_window.destroy()

    add_window.mainloop()

#Display of results in a table

def display():
    connn = sqlite3.connect("ACME.db")
    display_window = tk.Tk()
    display_window.title("Details")
    display_window.configure(bg='#132c33')
    table = ttk.Treeview(display_window,selectmode="extended")
    table["columns"] = ("one", "two", "three","four")
    table.column("one",minwidth=0,width=235)
    table.heading("one", text="Student")
    table.column("two",minwidth=0,width=235)
    table.heading("two", text="Course")
    table.column("three",minwidth=0,width=235)
    table.heading("three", text="Teacher")
    table.column("four",minwidth=0,width=235)
    table.heading("four", text="Result")

    cursor = connn.execute("SELECT rowid,* FROM details;")
    i = 0
    for row in cursor:
        table.insert('', i, text="Teacher " + str(row[1]), values=(row[2], row[3], row[4], row[5]))
        i = i + 1
    table.pack()
    connn.close()



def Student_search():
    search_window = tk.Tk()
    search_window.title("Search Student Details")
    search_window.configure(bg='#132c33')
    tk.Label(search_window, text="Enter the Student Code of teacher whose details are to be searched:",bg='#132c33',fg="white").grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    cr_code = tk.Entry(search_window, width=50)
    cr_code.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:",bg='#132c33',fg="white").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window,bg='#132c33',fg="white").grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    details = ttk.Treeview(search_window,selectmode="extended")
    details["columns"] = ("one", "two", "three","four")

    details.column("one",minwidth=0,width=235)
    details.heading("one", text="Student")
    details.column("two",minwidth=0,width=235)
    details.heading("two", text="Course")
    details.column("three",minwidth=0,width=235)
    details.heading("three", text="Teacher")
    details.column("four",minwidth=0,width=235)
    details.heading("four", text="Result")
    
    def submit():
        for row in details.get_children():
            details.delete(row)

        code = cr_code.get()
        fcon = sqlite3.connect("ACME.db")
        cursor = fcon.execute("SELECT rowid,* from details WHERE student = '" + code + "';")
        fcon.commit()

        i = 0
        for row in cursor:
            details.insert('', i, text="Details " + str(row[1]), values=(row[2], row[3], row[4],row[5]))
            i = i + 1
        
        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        fcon.close()
    search_window.mainloop()


def Teacher_search():
    search_window = tk.Tk()
    search_window.title("Search Student Details")
    search_window.configure(bg='#132c33')
    tk.Label(search_window, text="Enter the Name of teacher whose details are to be searched:",bg='#132c33',fg="white").grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    cr_code = tk.Entry(search_window, width=50)
    cr_code.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:",bg='#132c33',fg="white").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window,bg='#132c33',fg="white").grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    details = ttk.Treeview(search_window,selectmode="extended")
    details["columns"] = ("one", "two", "three","four")

    details.column("one",minwidth=0,width=235)
    details.heading("one", text="Student")
    details.column("two",minwidth=0,width=235)
    details.heading("two", text="Course")
    details.column("three",minwidth=0,width=235)
    details.heading("three", text="Teacher")
    details.column("four",minwidth=0,width=235)
    details.heading("four", text="Result")
    
    def submit():
        for row in details.get_children():
            details.delete(row)

        code = cr_code.get()
        fcon = sqlite3.connect("ACME.db")
        cursor = fcon.execute("SELECT rowid,* from details WHERE teacher = '" + code + "';")
        fcon.commit()

        i = 0
        for row in cursor:
            details.insert('', i, text="Details " + str(row[1]), values=(row[2], row[3], row[4],row[5]))
            i = i + 1
        
        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        fcon.close()
    search_window.mainloop()



def Course_search():
    search_window = tk.Tk()
    search_window.title("Course Details")
    search_window.configure(bg='#132c33')
    tk.Label(search_window, text="Enter the Title of Course whose details are to be searched:",bg='#132c33',fg="white").grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    cr_code = tk.Entry(search_window, width=50)
    cr_code.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:",bg='#132c33',fg="white").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window,bg='#132c33',fg="white").grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    details = ttk.Treeview(search_window,selectmode="extended")
    details["columns"] = ("one", "two", "three","four")

    details.column("one",minwidth=0,width=235)
    details.heading("one", text="Student")
    details.column("two",minwidth=0,width=235)
    details.heading("two", text="Course")
    details.column("three",minwidth=0,width=235)
    details.heading("three", text="Teacher")
    details.column("four",minwidth=0,width=235)
    details.heading("four", text="Result")
    
    def submit():
        for row in details.get_children():
            details.delete(row)

        code = cr_code.get()
        fcon = sqlite3.connect("ACME.db")
        cursor = fcon.execute("SELECT rowid,* from details WHERE course = '" + code + "';")
        fcon.commit()

        i = 0
        for row in cursor:
            details.insert('', i, text="Details " + str(row[1]), values=(row[2], row[3], row[4],row[5]))
            i = i + 1
        
        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        fcon.close()
    search_window.mainloop()


con.close()


