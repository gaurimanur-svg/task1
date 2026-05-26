import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List App")
root.geometry("450x500")

def add_task():
    task = entry.get()

    if task !="":
        listbox.insert(tk.END,"[ ]"+ task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning" ,"Enter a task")
                               

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()

        if new_task != "":
            listbox.delete(selected)
            listbox.insert(selected,"[ ]" + new_task)
            entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Warning", "Enter updated task")
    except:
       messagebox.showwarning("warning","Select a task")

def delete_task():
    try:
       selected = listbox.curselection()[0]
       listbox.delete(selected)
    except:
        messagebox.showwarning("Warning","select a task")

def complete_task():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        if "[x]" not in task:
             updated_task = task.replace("[ ]", "[x]")  
             listbox.delete(selected)
             listbox.insert(selected,updated_task)
    
    except:
        messagebox.showwarning("Warning","Select a task")

title= tk.Label(root, text="TO-DO LIST",
font=("Arial", 20, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, width=30,font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

update_btn = tk.Button(root,text="Update Task",width=15,command=update_task)
update_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=15,command=delete_task)
delete_btn.pack(pady=5)

complete_btn =tk.Button(root,text="Complete task", width=15,
command=complete_task)
complete_btn.pack(pady=5)                    

listbox =tk.Listbox(root,width=40,
height=15, font=("Arial", 12))
listbox.pack(pady=20)   

root.mainloop()
                    
                         
       
       

                        
        
                   
                                      
        





                 
   






                       






