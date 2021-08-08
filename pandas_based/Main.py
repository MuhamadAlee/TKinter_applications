import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
    

#insertion to the df

def insert():
    
    add_window = tk.Tk()
    add_window.title("Insert Assessment Details")
    add_window.configure(bg='#132c33')

    tk.Label(add_window,bg='#132c33',fg="white").grid(row=0, column=0, columnspan=2)
    tk.Label(add_window, text="Assessment ID:",bg='#132c33',fg="white").grid(row=1, column=0)
    assessment_id = tk.Entry(add_window, width=50)
    assessment_id.grid(row=1, column=1, padx=25)
    
    tk.Label(add_window, text="Submission Date:",bg='#132c33',fg="white").grid(row=2, column=0)
    submission_date = tk.Entry(add_window, width=50)
    submission_date.grid(row=2, column=1, padx=25)
    
    tk.Label(add_window, text="Module Name:",bg='#132c33',fg="white").grid(row=3, column=0)
    module_name = tk.Entry(add_window, width=50)
    module_name.grid(row=3, column=1, padx=25)


    tk.Label(add_window, text="Staff Id:",bg='#132c33',fg="white").grid(row=4, column=0)
    staff_id = tk.Entry(add_window, width=50)
    staff_id.grid(row=4, column=1, padx=25)

    tk.Label(add_window, text="Module Code:",bg='#132c33',fg="white").grid(row=5, column=0)
    module_code = tk.Entry(add_window, width=50)
    module_code.grid(row=5, column=1, padx=25)

    tk.Label(add_window, text="Weighting :",bg='#132c33',fg="white").grid(row=6, column=0)
    weighting = tk.Entry(add_window, width=50)
    weighting.grid(row=6, column=1, padx=25)


    tk.Label(add_window, text="Component:",bg='#132c33',fg="white").grid(row=7, column=0)
    Component = tk.Entry(add_window, width=50)
    Component.grid(row=7, column=1, padx=25)







    tk.Button(add_window, text='Submit', activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white", command=lambda: submit()).grid(row=8, column=0, columnspan=2, pady=10)

    def submit():
        aid = assessment_id.get()
        sd = submission_date.get()
        md = module_name.get()
        st = staff_id.get()
        cd = module_code.get()
        wg = weighting.get()
        cm = Component.get()
        if(len(aid)==0 or len(sd)==0  or len(md)==0 or len(st)==0 or len(cd)==0 or len(wg)==0  or len(cm)==0 ):
            messagebox.showinfo("Error", "Empty Feild")
            return

        df=pd.read_csv('samplecwk1data.csv')
        new_row={'Assessment ID':aid, 'Submission Dates':sd, 'Module Name':md, 'Staff ID':st,'Module Code':cd, 'Weighting':wg, 'Component':cm}
        df = df.append(new_row, ignore_index=True)
        df.to_csv("samplecwk1data.csv", encoding='utf-8', index=False)
        messagebox.showinfo("Success", "Record added Successfully")
        add_window.destroy()
    add_window.mainloop()


#display Records to csv

def display():
    display_window = tk.Tk()
    display_window.title("Assessment Records")
    display_window.configure(bg='#132c33')
    table = ttk.Treeview(display_window,selectmode="extended")
    table["columns"] = ("one", "two", "three", "four", "five","six","seven")
    table.column("one",minwidth=0,width=135)
    table.heading("one", text="Assessment Id")
    table.column("two",minwidth=0,width=135)
    table.heading("two", text="Submission Dates")
    table.column("three",minwidth=0,width=135)
    table.heading("three", text="Module Name")
    table.column("four",minwidth=0,width=135)
    table.heading("four", text="Staff Id")
    table.column("five",minwidth=0,width=135)
    table.heading("five", text="Module Code")
    table.column("six",minwidth=0,width=135)
    table.heading("six", text="Weighting")
    table.column("seven",minwidth=0,width=135)
    table.heading("seven", text="Component")
    
    df=pd.read_csv('samplecwk1data.csv') 
    i=0
    for index, row in df.iterrows():
        table.insert('', i, text="Assessment" + str(i), values=(row['Assessment ID'], row['Submission Dates'], row['Module Name'], row['Staff ID'],row['Module Code'], row['Weighting'],row['Component']))
        i+=1 
    table.pack()
    display_window.mainloop()
    

#count Records in csv

def count():
    
    df=pd.read_csv('samplecwk1data.csv') 
    i=0
    for index, row in df.iterrows():   
        i+=1
    messagebox.showinfo("Success", "Total Assessments are "+str(i+1)) 

    

#searching in Csv

def search():
    search_window = tk.Tk()
    search_window.title("Search Assessment")
    search_window.configure(bg='#132c33')
    tk.Label(search_window, text="Enter the Assessment Id whose details are to be searched:",bg='#132c33',fg="white").grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    aid = tk.Entry(search_window, width=50)
    aid.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:",bg='#132c33',fg="white").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window,bg='#132c33',fg="white").grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    
    tables = ttk.Treeview(search_window,selectmode="extended")
    tables["columns"] = ("one", "two", "three", "four", "five","six","seven")
    tables.column("one",minwidth=0,width=135)
    tables.heading("one", text="Assessment Id")
    tables.column("two",minwidth=0,width=135)
    tables.heading("two", text="Submission Dates")
    tables.column("three",minwidth=0,width=135)
    tables.heading("three", text="Module Name")
    tables.column("four",minwidth=0,width=135)
    tables.heading("four", text="Staff Id")
    tables.column("five",minwidth=0,width=135)
    tables.heading("five", text="Module Code")
    tables.column("six",minwidth=0,width=135)
    tables.heading("six", text="Weighting")
    tables.column("seven",minwidth=0,width=135)
    tables.heading("seven", text="Component")
    def submit():
        df=pd.read_csv('samplecwk1data.csv') 
        i=0
        for index, row in df.iterrows():
            if(row['Assessment ID']==str(aid.get())):
                tables.insert('', i, text="Assessment" + str(i), values=(row['Assessment ID'], row['Submission Dates'], row['Module Name'], row['Staff ID'],row['Module Code'], row['Weighting'],row['Component']))
            i+=1 
        tables.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    search_window.mainloop()



#deletion record in csv

def delete():
    delete_window = tk.Tk()
    delete_window.title("Delete Assessment ")
    delete_window.configure(bg='#132c33')
    tk.Label(delete_window, text="Enter Assessment Id whose details are to be removed:",bg='#132c33',fg="white").grid(row=0, column=0, padx=10, pady=10)
    aid = tk.Entry(delete_window, width=50)
    aid.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(delete_window, text="Delete Details", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: submit()).grid(row=1, column=0, columnspan=2)
    tk.Label(delete_window,bg='#132c33',fg="white").grid(row=2, column=0, columnspan=2)

    def submit():
        df=pd.read_csv('samplecwk1data.csv') 
        
        for index, row in df.iterrows():
            if(row['Assessment ID']==str(aid.get())):
                df.drop(index,axis=0,inplace=True)               
                messagebox.showinfo("Success", " Record Deleted Successfully.")
                break


        df.to_csv("samplecwk1data.csv", encoding='utf-8', index=False)
    
        delete_window.destroy()
    delete_window.mainloop()



#updation of record in a csv

def update():
    update_window = tk.Tk()
    update_window.title("Update Assessment")
    update_window.configure(bg='#132c33')
    tk.Label(update_window, text="\n\n",bg='#132c33',fg="white").grid(row=0, column=0, sticky="W", padx=10, columnspan=2)    
    tk.Label(update_window, text="Assess Id : ",bg='#132c33',fg="white").grid(row=0, column=0, sticky="W", padx=10, columnspan=2)
    caid = tk.Entry(update_window, width=50)
    caid.grid(row=0, column=1, sticky="W", padx=10, columnspan=2)
    tk.Button(update_window, text="Search", activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white",
              command=lambda: fillup()).grid(row=0, column=2,padx=5, pady=10)

    tk.Label(update_window, text="\nEnter the new values",bg='#132c33',fg="white").grid(row=2, column=0, sticky="W", padx=10, pady=10, columnspan=2)
    
    tk.Label(update_window, text="Assessment ID:",bg='#132c33',fg="white").grid(row=3, column=0)
    assessment_id = tk.Entry(update_window, width=50)
    assessment_id.grid(row=3, column=1, padx=25)
    
    tk.Label(update_window, text="Submission Date:",bg='#132c33',fg="white").grid(row=4, column=0)
    submission_date = tk.Entry(update_window, width=50)
    submission_date.grid(row=4, column=1, padx=25)
    
    tk.Label(update_window, text="Module Name:",bg='#132c33',fg="white").grid(row=5, column=0)
    module_name = tk.Entry(update_window, width=50)
    module_name.grid(row=5, column=1, padx=25)


    tk.Label(update_window, text="Staff Id:",bg='#132c33',fg="white").grid(row=6, column=0)
    staff_id = tk.Entry(update_window, width=50)
    staff_id.grid(row=6, column=1, padx=25)

    tk.Label(update_window, text="Module Code:",bg='#132c33',fg="white").grid(row=7, column=0)
    module_code = tk.Entry(update_window, width=50)
    module_code.grid(row=7, column=1, padx=25)

    tk.Label(update_window, text="Weighting :",bg='#132c33',fg="white").grid(row=8, column=0)
    weighting = tk.Entry(update_window, width=50)
    weighting.grid(row=8, column=1, padx=25)


    tk.Label(update_window, text="Component:",bg='#132c33',fg="white").grid(row=9, column=0)
    Component = tk.Entry(update_window, width=50)
    Component.grid(row=9, column=1, padx=25)

    tk.Button(update_window, text='Submit', activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white", command=lambda: submit()).grid(row=10, column=0, columnspan=2, pady=10)

    def fillup():
        df=pd.read_csv('samplecwk1data.csv') 
        i=0
        for index, row in df.iterrows():
            if(row['Assessment ID']==str(caid.get())):
                assessment_id.insert(0,row['Assessment ID'])
                submission_date.insert(0,row['Submission Dates'])
                module_name.insert(0,row['Module Name'])
                staff_id.insert(0,row['Staff ID'])
                module_code.insert(0,row['Module Code'])
                weighting.insert(0,row['Weighting'])
                Component.insert(0,row['Component'])
                break
    def submit():
        aid = assessment_id.get()
        sd = submission_date.get()
        md = module_name.get()
        st = staff_id.get()
        cd = module_code.get()
        wg = weighting.get()
        cm = Component.get()
        if(len(aid)==0 or len(sd)==0  or len(md)==0 or len(st)==0 or len(cd)==0 or len(wg)==0  or len(cm)==0 ):
            messagebox.showinfo("Error", "Empty Feild")
            return

        df=pd.read_csv('samplecwk1data.csv')
        for index, row in df.iterrows():
            if(row['Assessment ID']==str(caid.get())):
                row['Assessment ID']=aid
                row['Submission Dates']=sd
                row['Module Name']=md
                row['Staff ID']=st
                row['Module Code']=cd
                row['Weighting']=wg
                row['Component']=cm
                break

        df.to_csv("samplecwk1data.csv", encoding='utf-8', index=False)        



        messagebox.showinfo("Success", "Record Updated Successfully.")
        update_window.destroy()
    update_window.mainloop()

















def setup():
    mainWindow = tk.Tk()
    mainWindow.configure(bg='#132c33')
    mainWindow.title('ACME Assessment Database System ')
    mainWindow.attributes('-alpha',0.2)
    #authentication Setup

    label_1 = tk.Label(mainWindow, text="\n  ACME UNIVERSITY STUDENT MANAGEMENT PORTAL \n \n", font=("Georgia", 30),bg="#132c33", fg="white",height=3, width =150)
    label_1.pack()


    button_1 = tk.Button(mainWindow, text="Add Assesment", command=lambda: insert(), height=3,width=77,
                         activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white" )
    button_1.pack()

    button_2 = tk.Button(mainWindow, text="Update Assesment", command=lambda: update(),height=3,width=77,
                         activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
    button_2.pack()

    button_3 = tk.Button(mainWindow, text="View Assesment", command=lambda: display(), height=3,width=77,
                         activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
    button_3.pack()

    button_4 = tk.Button(mainWindow, text="Delete Assesment", command=lambda: delete(), height=3,width=77,
                         activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
    button_4.pack()


    button_5 = tk.Button(mainWindow, text="Search Assesment", command=lambda: search(),height=3,width=77,
                         activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
    button_5.pack()


    button_6 = tk.Button(mainWindow, text="Count Assesment", command=lambda: count(),height=3,width=77,
                         activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
    button_6.pack()


    button_6 = tk.Button(mainWindow, text="Logout", command=lambda: mainWindow.destroy(),height=3,width=77,
                         activebackground='#51c4d3', activeforeground='white',bg='#126e82',fg="white")
    button_6.pack()

    label_7 = tk.Label(mainWindow, text="\n", font=("Georgia", 30),bg="#132c33", fg="white",height=3, width =150)
    label_7.pack()


    mainWindow.mainloop()










if __name__ == '__main__':
    df=pd.read_csv('samplecwk1data.csv')    
    setup()
    print(df.columns)
