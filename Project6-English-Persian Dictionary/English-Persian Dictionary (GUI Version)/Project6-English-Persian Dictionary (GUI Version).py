import tkinter as tk 
from tkinter import messagebox , ttk
import pandas as pd



df=pd.read_csv('C:\\Users\\Herin\\OneDrive\\Desktop\\Practice\\Mordad Practice\\Practice Data\\dictionary.csv')
dictionary= dict( zip( df['English'], df['Persian'] ))


main_window = tk.Tk()
main_window.title('English to word dictionary')
main_window.geometry('800x300')
main_window.configure(bg='skyblue')
main_window.resizable(False, False)


def open_sub_window():

    sub_window = tk.Toplevel(main_window)
    sub_window.title('Add New Word To Dictionary')
    sub_window.geometry('800x300')
    sub_window.configure(bg='skyblue')
    sub_window.resizable(False, False)
    sub_window.grab_set()

    eng_lable=ttk.Label(sub_window , text= 'Enter the English word :' , padding=5 , background='skyblue' , font=('Arial Rounded MT Bold ', 11))
    eng_lable.place(x=265 , y=60)

    eng_entry= ttk.Entry(sub_window , width=50 )
    eng_entry.place(x=270 , y=90)

    trans_lable=ttk.Label(sub_window , text= 'Enter the word translation :', padding=5, background='skyblue', font=('Arial Rounded MT Bold ', 11))
    trans_lable.place(x=265 , y=120)

    trans_entry= ttk.Entry(sub_window , width=50 )
    trans_entry.place(x=270 , y=150)

    message= ttk.Label( sub_window, text='', padding=5 , background='skyblue', font=('Arial Rounded MT Bold ', 10))



    def add_new_word():

        eng_word = eng_entry.get().lower()
        translation =trans_entry.get().lower()

        if eng_word  in dictionary and dictionary[eng_word]==translation:

            messagebox.showinfo('Duplicate Entry','This word and its translation already exist in the dictionary !' , parent=sub_window)
            return

        elif eng_word and translation :

            dictionary[eng_word]= translation
            df= pd.DataFrame( list( dictionary.items()) , columns= ['English' ,'Persian'] )

            df.to_csv('C:\\Users\\Herin\\OneDrive\\Desktop\\Practice\\Mordad Practice\\Practice Data\\dictionary.csv' , index=False)

            message.config(text='Thank you! the new word was added successfully.')
            message.place(x=280 , y=210)
        
            def ask():

                answer = messagebox.askyesno('ًQuestion', 'Is there any other word that you wold like to know the translation?', parent=sub_window)

                if answer :
                        sub_window.destroy()

                else:
                    message.config( text='ok, for now bye!')
                    sub_window.after(5000,  sub_window.destroy)
                    message.place(x=350 , y=210)

            sub_window.after(2000, ask)        

        else :
            message.config(text='you have to enter both the english word and the translation!.')
            message.place(x=250 , y=190)
            sub_window.after(1000, message.place_forget)


    add_button= ttk.Button (sub_window, text='Add' , style='My.TButton' ,cursor='hand2',width=15, command =add_new_word)
    add_button.place(x=600, y=210 )

        


def search_word():

    word = entry1.get().lower()

    if word in dictionary :
        translate.config( text=f'translation is:  { dictionary[word]}')
        translate.place(x=350 , y=200)
        main_window.after(5000, translate.place_forget)

    else:

        answer = messagebox.askyesno('this word is not available in the dictionary', 'Do you want to add this new word to the dictionary?')

        if answer :

            open_sub_window()

        else:
            translate.config( text='ok, have a good day!')
            translate.place(x=330 , y=200)
            main_window.after(1000, translate.place_forget)



style = ttk.Style()
style.theme_use("clam")  # or : "alt", "default", "vista", "xpnative"

style.configure(
    'My.TButton',
    font=('Arial Rounded MT Bold ', 10, 'bold'),
    padding=13
    )

style.map(
    'My.TButton',
    background=[('active', '#ff99cc')],  
    foreground=[('active', 'black')]
)

lable1=ttk.Label(main_window , text= '...Enter The Word You Want To Translate...' , padding=20 , background='skyblue' , font=('Arial Rounded MT Bold ', 15 ), width=50)
lable1.place(x=200 , y=70)

entry1= ttk.Entry(main_window , width=50 , font=('Arial Rounded MT Bold ', 12 ) )
entry1.place(x=200 , y=145)

button1= ttk.Button (main_window, text='Search...' , style='My.TButton',cursor="hand2", width=15 ,command=search_word)
button1.place(x=600, y=210 )

button2= ttk.Button(main_window, text='Add new word', style='My.TButton' ,cursor="hand2",width=15, command= open_sub_window)
button2.place(x=80, y=210 )

translate = ttk.Label( main_window, text='', padding=5, background='skyblue', font=('Arial Rounded MT Bold ', 15))


main_window.mainloop()
