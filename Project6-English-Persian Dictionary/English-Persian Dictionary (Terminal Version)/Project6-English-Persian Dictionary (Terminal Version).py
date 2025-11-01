import pandas as pd 

df=pd.read_csv('C:\\Users\\Herin\\OneDrive\\Desktop\\Practice\\Mordad Practice\\Practice Data\\dictionary.csv')

dictionary= dict( zip( df['English'], df['Persian'] ))

Active = 'y'

while True:
    
    word = input("Enter the word you want to know the persian translation of : ").lower()

    if word in  dictionary:
        print(f'translation is: {dictionary[word]}')
        
        Active =input('Is there any other word that you wold like to know the translation? y/n :').lower()   
        if Active == 'n':
            print('ok, have a good day!')
            break
            

    else:

        response = input("Unfortunately, this word is not available in the dictionary!\nDo you want to add this new word to the dictionary? y/n :").lower()

        if response == 'n':

            Active =input('Is there any other word that you wold like to know the translation? y/n :').lower()   
            if Active == 'n':
                print('ok good luck!')
                break
        else:

            dictionary[word]= input("ok! please enter the persian translation of this word: ")
            df= pd.DataFrame( list( dictionary.items()) , columns= ['English' ,'Persian'] )

            df.to_csv('C:\\Users\\Herin\\OneDrive\\Desktop\\Practice\\Mordad Practice\\Practice Data\\dictionary.csv' , index=False)

            Active =input('Thank You!\n Is there any other word that you wold like to know the translation? y/n :').lower()
            if Active == 'n':
                print('ok, for now bye!')
                break

    
    
   
           

