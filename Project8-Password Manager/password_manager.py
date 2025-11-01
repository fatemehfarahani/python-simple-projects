import json 
import os 
from getpass import getpass
from cryptography.fernet import Fernet

Passwords_file = 'passwords.json'
Key_file = 'key.key'



def generate_key():

    key = Fernet.generate_key()

    with open(Key_file  , 'wb') as key_file:

        key_file.write(key)


def load_key():
    
    return open (Key_file , 'rb').read()


def encrypt_password(password , key):
    
    f = Fernet(key)
    return f.encrypt(password.encode())



def decrypt_password(encrypted_password , key):
    
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()


def save_password(passwords):
    
    with open( Passwords_file , 'w') as file:
        json.dump(passwords , file )



def load_password():
    
    if os.path.exists(Passwords_file):
        with open(Passwords_file , 'r') as file:
            return json.load(file)
    else:
        return {}


def add_password(account , password , key):

    passwords = load_password()
    encrypted_password = encrypt_password(password , key)

    passwords[account] = encrypted_password.decode()
    save_password(passwords)

    Print(f'Password for {account} added successfully.')



def retrieve_password(account , key):
    
    passwords= load_password()

    if account in passwords:
        encrypted_password = passwords[account].encode()
        return decrypt_password(encrypted_password  , key)
    
    else: 
        print(f'No password found for account: {account}')
        return None


def main():
    
    if not os.path.exists(Key_file):
        print(f'')
        generate_key()

    key = load_key()

    while True:

        print('\n--- Password Manager ---')
        print('1. Add a new password')
        print('2. Retrieve a password')
        print('3. Quit')
        choice = input('Enter your choice: ')

        if choice == '1':
            account = input('Enter the account name (e.g., website or app name): ')
            password = getpass('Enter the password: ')

            add_password (account , password , key )


        elif choice == '2':
            
            account = input('Enter the account name:')
            password = retrieve_password ( account , key)
            if password:
                print(f'Password for {account}: {password}')


        elif choice == '3':
            
            print ('Exiting the Password Manager')
            break

        else :
            print('Invalid choice. Please try again.')

if  __name__ == '__main__':
    
    main()