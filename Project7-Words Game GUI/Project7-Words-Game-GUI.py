import random
import tkinter as tk 
from tkinter import ttk 
import numpy as np


# --- Define letters for each level ---
level1_letters = list("CATDOG")
level2_letters = list("APPLEBANANAPEARGRAPEPLUM")
level3_letters = list("ELEPHANTKANGAROOPENGUINCROCODILEOSTRICHFLAMINGOGORILLA")


# --- Color palette for empty cells and text ---

colors = [ "#FF6F61", "#6B5B95",   "#88B04B",  "#F7CAC9",  "#92A8D1",
           "#F7786B",   "#034F84",  "#B565A7",   "#955251", "#009B77", 
           "#FFD662",   "#DD4124",   "#45B8AC",  "#EFC050", "#5B5EA6",
           "#9B2335", "#DFCFBE",  "#55B4B0", "#E15D44",  "#7FCDCD",  ]

# --- Positive feedback messages ---
my_list=['nice!' ,'Exelent','very good','bravo!','good job']

# --- Words required and time for each level ---
level_words={ 1:2 ,2:5, 3:7 }
level_times={ 1:120 , 2:180 , 3:300 }

# --- Game state variables ---
level= 1
time_left = level_times[level]

entered_words = set()
correct_words=0
game_over= False

# --- Function to display the letter table for the current level ---
def show_table(letters):  
    
    # Remove previous table
    for widget in center_Frame.winfo_children():
        widget.destroy()              

   # Fill up to 36 cells and shuffle
    while len(letters) < 36:

        letters.append('')
    random.shuffle(letters)

    letters_np = np.array(letters).reshape(6,6)

    style.configure("My.TLabel", font=('Segoe UI', 18, 'bold'), padding=6, relief='ridge', width=4 , height=2 )
        
    # Create the table with colored empty cells
    for row in range(6):
        for col in range(6):

            letter= letters_np[row, col]
            if letter == '':
                bg_color = random.choice(colors)
            else:
                bg_color = 'white'

            lable1=ttk.Label( center_Frame , text= letter , style="My.TLabel", anchor='center', background=bg_color)
            lable1.grid(row=row , column=col ,padx=5, pady=5)

    return letters_np

# --- Countdown timer function ---
def countdown():
       
        global time_left , game_over

        if time_left > 0 and not game_over:
           time_left -=1
           time_lable.config(text=f'Time : {time_left}')
           main_window.after(1000, countdown)

        else:
            if not game_over:

                result_lable.config( text='Game Over' , width=50 , font=('Segoe UI', 40 , 'bold' )  , foreground='red')
                result_lable.place(x=x, y=y)

                game_over= True

# --- Function to check the user's entered word ---
def check_word():

    global time_left, correct_words , level , game_over , letters, letters_np 

    word = user_entry.get().upper()

    # Check for duplicate word
    if word in entered_words:
            result_lable.config(text="You already entered this word!" , font=('Segoe UI', 10 , 'bold'))
            return

    entered_words.add(word)
    
    # Check if all letters are in the table
    latters_flat = [char for row in letters_np for char in row]

    for char in word :

        if char not in latters_flat:
 
           
            result_lable.config(text='invald word!')
            result_lable.place(x=x, y=y)
            main_window.after(2000 , result_lable.place_forget)
            user_entry.delete(0, tk.END)
            return

    # If valid word
    result_lable.config(text=random.choice(my_list))
    result_lable.place(x=x, y=y)
    main_window.after(2000 , result_lable.place_forget)

    correct_words +=1
    
    num_word_lable.config( text= f'Number of Word :{correct_words}')
    user_entry.delete(0, tk.END)

    # Level up if enough words guessed
    if correct_words == level_words[level]:

        level+=1


        if level >3 :

            result_lable.config(text='YOU WON!' ,width=50 , font=('Segoe UI', 40 , 'bold' ), foreground='green')
            result_lable.place(x=x, y=y)
            game_over= True

        else:

            if level == 2:
                letters = level2_letters.copy()
                
            elif level == 3:
                letters = level3_letters.copy()
            
            letters_np = show_table(letters)

            correct_words=0
            time_left = level_times[level]
            result_lable.config(text='LEVEL UP!',width=50 , font=('Segoe UI', 40 , 'bold' ), foreground='hotpink')
            result_lable.place(x=x, y=y)

            level_lable.config(text=f'Level :{level} ')

            countdown()

# --- Function to start the game after closing the guide window ---
def start_game():
    sub_window.destroy()

    global letters, letters_np, correct_words, level, game_over, entered_words, time_left

    correct_words = 0
    level = 1
    game_over = False
    entered_words = set()
    time_left = level_times[level]

    letters = level1_letters.copy()
    letters_np = show_table(letters)

    level_lable.config(text=f'Level :{level}')
    num_word_lable.config(text=f'Correct words :{correct_words}')
    time_lable.config(text=f'Time : {time_left}')
    countdown()


# --- Tkinter window and widgets setup ---
main_window = tk.Tk()
main_window .title('Word Game')
main_window.geometry('1000x600')
main_window.resizable(False, False)

center_Frame=ttk.Frame(main_window)
center_Frame.pack(side="top", pady=50)

style = ttk.Style()

# --- Guide subwindow ---
sub_window= tk.Toplevel(main_window)
sub_window.title("Guide")
sub_window.geometry('500x300')
sub_window.resizable(False, False)
sub_window.configure(bg='lightpink')
sub_window.transient(main_window) 
sub_window.grab_set() 

Guide_lable1=ttk.Label( sub_window, text='Rules of the word guessing game:', width=30 , font=('Segoe UI', 15, 'bold'), background='lightpink', foreground='darkblue')
Guide_lable1.place(x=50 , y=20)

Guide_lable2=ttk.Label( sub_window, text='You have to guess a certain number of words at the specified time.\nIn the first level:2 woeds in 2 minutes,\nIn the second level:5 words in 3 minutes\nAnd in the third or final level:7 words in 5 minutes.' 
,width=60 , font=('Segoe UI', 10, 'bold') , background='lightpink')
Guide_lable2.place(x=50 , y=70)

Guide_lable3=ttk.Label( sub_window, text='good luck!' , width=20 , font=('Segoe UI', 15, 'bold') , background='lightpink',foreground='darkblue')
Guide_lable3.place(x=50 , y=160)

start_button= ttk.Button(sub_window, text='Start Game', width=12 , padding=12)
start_button.place(x=210 , y=220)
start_button.config(command=start_game)




lable2=ttk.Label(main_window, text='Guess a word :' , font=('Segoe UI', 20, 'bold'), anchor='center')
lable2.place(x=400, y=420)


time_lable= ttk.Label(main_window , text=f'Time : {time_left} ' , width=18 , font=('Segoe UI', 15, 'bold'), foreground='red')
time_lable.place(x=20 , y=40)

level_lable=ttk.Label(main_window, text=f'Level :{level}' , width=10 , font=('Segoe UI', 15, 'bold'))
level_lable.place(x=20 , y=70)

num_word_lable= ttk.Label(main_window , text=f'Correct words :{correct_words}' , width=18 , font=('Segoe UI', 15, 'bold'))
num_word_lable.place(x=20 , y=100)



user_entry=ttk.Entry(main_window, width=50 , font=('Segoe UI', 15 , 'bold' ))
user_entry.place(x=200 , y=490)

ckeck_button = ttk.Button(text='Check', width=6 ,padding=5 ,command=check_word)
ckeck_button.place(x=200 , y=530)


result_lable=tk.Label(main_window, text='' , width=50 , font=('Segoe UI', 40 , 'bold' )  , foreground= random.choice(colors))

main_window.update_idletasks() 

w = result_lable.winfo_reqwidth()
h = result_lable.winfo_reqheight()

x = (1000 - w) // 2
y = (600 - h) // 2

main_window.mainloop()