import tkinter as tk 
import json
import os

TASKS_FILE ='tasks.json'


def save_tasks():

    tasks = task_list.get(0 , tk.END)

    with open ( TASKS_FILE , 'w' , encoding='utf8') as file:
        json.dump(list(tasks) , file)

def load_tasks():

    if os.path.exists(TASKS_FILE):

        with open ( TASKS_FILE , 'r' , encoding='utf8') as file:
            tasks = json.load(file)

            for i, task in enumerate(tasks):
                task_list.insert(tk.END, task)
                if task.startswith("✔️ "):
                    task_list.itemconfig(i, fg='green')
            update_status()        
        




def add_task ():
    task = entry_task.get()

    if task :
        task_list.insert(tk.END , task)
        entry_task.delete(0, tk.END)
        update_status()
        save_tasks()
    


def delete_task():
    selected = task_list.curselection()

    if selected :
        task_list.delete( selected[0])
        update_status()
        save_tasks()


def mark_done():

    selected = task_list.curselection()

    if selected:
        task = task_list.get(selected[0])

        if not task.startswith("✔️ "):
            task_list.delete( selected[0])
            task_list.insert( selected[0] ,"✔️ " + task )
            task_list.itemconfig( selected[0], fg='green' )
            update_status()
            save_tasks()


def edit_task():

    selected = task_list.curselection()
    
    if selected:

        task = task_list.get(selected[0])

        if task.startswith("✔️ "):
            task= task[2:].lstrip()

        entry_task.delete(0,tk.END)
        entry_task.insert (0, task)

        main_window.edit_index = selected[0]
        btn_save_edit.pack(pady=5)
        update_status()



def save_edit():

    if hasattr (main_window , 'edit_index'):

        edited_task = entry_task.get()

        if edited_task:

            old_task = task_list.get(main_window.edit_index)

            if old_task.startswith("✔️ "):
                edited_task = "✔️ " + edited_task
                task_list.delete(main_window.edit_index)
                task_list.insert(main_window.edit_index, edited_task)
                task_list.itemconfig(main_window.edit_index, fg='green')

            else :

                task_list.itemconfig(main_window.edit_index, fg='black')
                task_list.delete(main_window.edit_index)
                task_list.insert(main_window.edit_index , edited_task)

            entry_task.delete(0, tk.END)
            update_status()
            save_tasks()
            del main_window.edit_index
            btn_save_edit.pack_forget()


def  update_status():
    total= task_list.size()
    done=0

    for i in range(total) :
        task = task_list.get(i)

        if task.startswith("✔️ "):
            done+=1
        
    Remaining = total - done

    label_status .config(text=f'Total tasks: {total} | Done tasks: {done} | Remaining tasks:{Remaining }' , fg='red')


def clear_all_tasks():
    task_list.delete(0,tk.END)
    update_status()
    save_tasks()

main_window= tk.Tk()
main_window.title('TO-DO APP')
main_window.geometry("480x640") 
main_window.resizable(False, False)  
main_window.configure(bg="#ffe082")


font_main = ("Segoe UI", 12)


entry_task = tk.Entry( main_window , width=25, font=font_main)
entry_task.pack(pady=20)

btn_frame = tk.Frame(main_window, bg="#ffe082")
btn_frame.pack(pady=5)


btn_add= tk.Button(btn_frame , text='Add Task'  , command= add_task , width=12, font=font_main, bg="#4fc3f7", fg="white", bd=0, activebackground="#0288d1")
btn_add.grid(row=0, column=0, padx=3)

btn_delete= tk.Button(btn_frame, text='Delete Task' , width=12 , command= delete_task , font=font_main, bg="#e57373", fg="white", bd=0, activebackground="#b71c1c")
btn_delete.grid(row=0, column=1, padx=3)

btn_done= tk.Button(btn_frame, text='Done' , width=12 , command= mark_done, font=font_main, bg="#81c784", fg="white", bd=0, activebackground="#388e3c")
btn_done.grid(row=0, column=3, padx=3)

task_list = tk.Listbox( main_window , width= 32 , height=15 , font=font_main, bg="white", fg="#333", bd=0, highlightthickness=0, selectbackground="#ffd54f")
task_list .pack( pady=10)


btn_edit= tk.Button(btn_frame, text='Edit' , width=12, command= edit_task ,  font=font_main, bg="#ffb74d", fg="white", bd=0, activebackground="#f57c00")
btn_edit.grid(row=0, column=2, padx=3)

btn_save_edit= tk.Button(main_window , text='Save Edit' , width=12 , command= save_edit, font=font_main, bg="#4fc3f7", fg="white", bd=0, activebackground="#0288d1")

btn_clear_all= tk.Button(main_window ,text='Clear All Tasks' , width=12 , command= clear_all_tasks, font=font_main, bg="#bdbdbd", fg="black", bd=0, activebackground="#757575")
btn_clear_all.pack(pady=5)

label_status = tk.Label( main_window , text='' , font=font_main, bg="#ffe082", fg="#333")
label_status.pack(pady=5)


load_tasks()
update_status()
main_window.mainloop()