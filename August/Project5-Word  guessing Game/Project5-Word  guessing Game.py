import random


words={'love':'A special feeling we have for someone' ,'mom':'The one who gives us life','fastfood':'The kind of food that is prepared quickly','yeonjun':'a memeber of the boy band kpop,The name of this band starts with T','apple':'A kind of fruit','cherry':'A kind of fruit','pink':'A Color'}

chosen_word = random.choice(list(words))

chosen_word=chosen_word 
hidden_word =[]

for character in chosen_word:
    hidden_word .append('_.')

print("guess what the word is. you have 10 chances!")
print("you can guess the whole word or a letter of the word \n")

for word , hint in words.items():
    if chosen_word == word:
       print(f'HINT: {hint}')

print(''.join(hidden_word),'\n')

chances=10
guessed_letters=set()

while chances > 0 :
    
    print(f"{chances} chance left...")
    user_geuss=input(f"what is your guess?").lower().strip()

    

    #check the whole word
    if  len(user_geuss) == len(hidden_word) :
        if user_geuss == chosen_word:

            hidden_word=[user_geuss]
            print('amazing!YOU WON!')
            print(''.join(hidden_word))
            break
        else:
            chances-=1
            print('ops! wrong guess! tray again')
            


        

    #check the letters of word
    elif len(user_geuss) == 1:

        if user_geuss in guessed_letters:
                print('you have already entered this letter! tray again...')
                continue

        

        guess=False

        for index , value in enumerate(chosen_word):
            if value == user_geuss:

                hidden_word[index]= user_geuss
                guessed_letters.add(user_geuss)
                guess=True

                
        if guess == True:
            print('nice!')    


        else:
            chances-=1
            print("incorrect guess! tray again...")

        print(''.join(hidden_word))

        if '_.' not in hidden_word:
            print('Congratulations! You Won')
            break

        if chances == 0 and  '_.' in hidden_word:
            print("GAME OVER!\n Time is Running Out. ")
            print(f"the word was : {chosen_word} !")

                  


    elif len(user_geuss) !=1 and len(user_geuss) != len(chosen_word):
        print("you can only guess the whole word at ones or just one letter of the word!tray again.")


    
 
   
       
     


