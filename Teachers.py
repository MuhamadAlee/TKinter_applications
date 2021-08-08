import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox


# creating database
con = sqlite3.connect("ACME.db")

#creating table inside database
try:
    con.execute("CREATE TABLE IF NOT EXISTS teacher(id INTEGER PRIMARY KEY   AUTOINCREMENT, title TEXT NOT NULL,  section TEXT NOT NULL, code TEXT NOT NULL UNIQUE);")
except sqlite3.Error as er:
    messagebox.showinfo("Error", "Something went wrong")


#insertion of Teacher record to the database

def insert_data(title,section, code):
    conn = sqlite3.connect("ACME.db")
    flag=True
    try:    
        conn.execute("INSERT INTO teacher(title,section,code) VALUES( '" + title + "', '" + section +
                 "', '" + code + "' );")
        conn.commit()
    except sqlite3.Error as er:
        messagebox.showinfo("Error", "Something went wrong") 
        flag=False   
    conn.close()
    if(flag):
        messagebox.showinfo("Success", "Record Inserted Successfully.")

#insert details gui

classes=[
"BSIT",
"BSCS",
"BSSE"
]

def insert():
    add_window = tk.Tk()
    add_window.title("Insert Teacher Details")
    add_window.configure(bg='#132c33')
    tk.Label(add_window,bg='#132c33',fg="white").grid(row=0, column=0, columnspan=2)
    tk.Label(add_window, text="Teacher Name:",bg='#132c33',fg="white").grid(row=1, column=0)
    cr_title = tk.Entry(add_window, width=50)
    cr_title.grid(row=1, column=1, padx=25)
    tk.Label(add_window, text="Section:",bg='#132c33',fg="white").grid(row=2, column=0)
   
    cls_clicked = tk.StringVar(add_window) 
    cls_clicked.set( "BSIT" )
    class_entry = tk.OptionMenu( add_window , cls_clicked , *classes )
    class_entry.grid(row=2, column=1)
    class_entry.config(width=36, font=("Georgia", 12))


    tk.Label(add_window, text="Teacher Code:",bg='#132c33',fg="white").grid(row=3, column=0, padx=20)
    cr_code = tk.Entry(add_window, width=50)
    cr_code.grid(row=3, column=1, padx=25)
    
    tk.Button(add_window, text='Submit', activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white", command=lambda: submit()).grid(row=4, column=0, columnspan=2, pady=10)

    def submit():
        title = cr_title.get()
        section = cls_clicked.get()
        code = str(cr_code.get())
        if(len(title)==0 or len(section)==0  or len(code)==0 ):
            messagebox.showinfo("Error", "Empty Feild")
            return
        insert_data(title,section,code)
        add_window.destroy()

    add_window.mainloop()

#Display of results in a table

def display():
    connn = sqlite3.connect("ACME.db")
    display_window = tk.Tk()
    display_window.title("Teacher Database")
    display_window.configure(bg='#132c33')
    table = ttk.Treeview(display_window,selectmode="extended")
    table["columns"] = ("one", "two", "three")
    table.column("one",minwidth=0,width=235)
    table.heading("one", text="Teacher Name")
    table.column("two",minwidth=0,width=235)
    table.heading("two", text="Section")
    table.column("three",minwidth=0,width=235)
    table.heading("three", text="Code")
    cursor = connn.execute("SELECT rowid,* FROM teacher;")
    i = 0
    for row in cursor:
        table.insert('', i, text="Teacher " + str(row[1]), values=(row[2], row[3], row[4]))
        i = i + 1
    table.pack()
    connn.close()


#updation of record in a table

def update():
    update_window = tk.Tk()
    update_window.title("Update Teacher Details")
    update_window.configure(bg='#132c33')
    tk.Label(update_window, text="Insert Code of teacher :",bg='#132c33',fg="white").grid(row=0, column=0, sticky="W", padx=10, columnspan=2)
    s_id = tk.Entry(update_window, width=50)
    s_id.grid(row=1, column=0, sticky="W", padx=10, columnspan=2)
    tk.Button(update_window, text="Search", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: fillup()).grid(row=1, column=2,padx=5, pady=10)

    tk.Label(update_window, text="\nEnter the new values:",bg='#132c33',fg="white").grid(row=2, column=0, sticky="W", padx=10, pady=10, columnspan=2)
    tk.Label(update_window, text="Teacher Name:",bg='#132c33',fg="white").grid(row=3, column=0, sticky="W", padx=10, pady=10)
    cr_title = tk.Entry(update_window, width=50)
    cr_title.grid(row=3, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Section:",bg='#132c33',fg="white").grid(row=4, column=0, sticky="W", padx=10, pady=10)
   
    cls_clicked = tk.StringVar(update_window) 
    cls_clicked.set( "BSIT" )
    class_entry = tk.OptionMenu( update_window , cls_clicked , *classes )
    class_entry.grid(row=4, column=1)
    class_entry.config(width=36, font=("Georgia", 12))

    tk.Label(update_window, text="Teacher Code:",bg='#132c33',fg="white").grid(row=5, column=0, sticky="W", padx=10, pady=10)
    cr_code = tk.Entry(update_window, width=50)
    cr_code.grid(row=5, column=1, sticky="W", padx=10, pady=10)
    
    tk.Button(update_window, text="Update", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=6, column=0, padx=10, pady=10, columnspan=2)

    def fillup():
        flag=True 
        sid = s_id.get()       
        try: 
            connn = sqlite3.connect("ACME.db")
            cursor = connn.execute("SELECT * FROM teacher where code='"+sid+"';")
            connn.commit()
            for row in cursor:
                cr_title.insert(0,str(row[1]))
                cls_clicked.set(str(row[2]))
                cr_code.insert(0,str(row[3]))
                
        except sqlite3.Error as er:
            messagebox.showinfo("Error", "No Record Found")
        connn.close()


    def submit():
        sid = s_id.get()
        title = cr_title.get()
        section = cls_clicked.get()
        code = cr_code.get()
        if(len(title)==0 or len(section)==0  or len(code)==0 ):
            messagebox.showinfo("Error", "Empty Feild")
            return
        scon = sqlite3.connect("ACME.db")
        flag=True        
        try:        
            scon.execute("UPDATE teacher SET title = '" + title + "',section = '" + section + "', code = '" + code +"';")
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
    delete_window.title("Delete Teacher ")
    delete_window.configure(bg='#132c33')
    tk.Label(delete_window, text="Enter Teacher Code whose details are to be removed:",bg='#132c33',fg="white").grid(row=0, column=0, padx=10, pady=10)
    cr_code = tk.Entry(delete_window, width=50)
    cr_code.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(delete_window, text="Delete Details", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=1, column=0, columnspan=2)
    tk.Label(delete_window,bg='#132c33',fg="white").grid(row=2, column=0, columnspan=2)

    def submit():
        code = cr_code.get()
        if(len(code)==0 ):
            messagebox.showinfo("Error", "Empty Feild")
            return
        dcon = sqlite3.connect("ACME.db")
        flag=True
        try:        
            dcon.execute("DELETE FROM teacher WHERE code = '" + code+"';")
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


#finding Teacher details gui

def search():
    search_window = tk.Tk()
    search_window.title("Search Teacher Details")
    search_window.configure(bg='#132c33')
    tk.Label(search_window, text="Enter the Teacher Code of teacher whose details are to be searched:",bg='#132c33',fg="white").grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    cr_code = tk.Entry(search_window, width=50)
    cr_code.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:",bg='#132c33',fg="white").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window,bg='#132c33',fg="white").grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    details = ttk.Treeview(search_window,selectmode="extended")
    details["columns"] = ("one", "two", "three")

    details.column("one",minwidth=0,width=235)
    details.heading("one", text="Teacher Name")
    details.column("two",minwidth=0,width=235)
    details.heading("two", text="Section")
    details.column("three",minwidth=0,width=235)
    details.heading("three", text="Code")
    
    def submit():
        for row in details.get_children():
            details.delete(row)

        code = cr_code.get()
        fcon = sqlite3.connect("ACME.db")
        cursor = fcon.execute("SELECT rowid,* from teacher WHERE code = '" + code + "';")
        fcon.commit()

        i = 0
        for row in cursor:
            details.insert('', i, text="Details " + str(row[1]), values=(row[2], row[3], row[4]))
            i = i + 1
        
        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        fcon.close()
    search_window.mainloop()



con.close()


