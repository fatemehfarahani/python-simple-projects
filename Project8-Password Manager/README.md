# Password Manager

A simple and secure command-line password manager written in Python.  
This project allows you to **store** and **retrieve** your passwords for different accounts (websites, apps, etc.) in an encrypted format using the `cryptography` library.

---

## Features

- **Add new passwords** for any account (website, app, etc.)
- **Retrieve saved passwords** securely
- **All passwords are encrypted** using Fernet symmetric encryption
- **Passwords and encryption key are stored in separate files**
- **User-friendly command-line interface**

---

## How It Works

- When you add a password, it is encrypted and saved in a JSON file (`passwords.json`).
- The encryption key is generated once and saved in a separate file (`key.key`).
- When you retrieve a password, it is decrypted and shown in the terminal.
- The program uses `getpass` to hide your password input.

---

## How to Use

1. **Clone the repository or copy the code into a file (e.g., `password_manager.py`).**

2. **Install the required dependency:**
    ```bash
    pip install cryptography
    ```

3. **Run the script:**
    ```bash
    python password_manager.py
    ```

4. **Follow the on-screen menu:**
    - Add a new password
    - Retrieve a password
    - Quit

5. **When you add a password:**
    - The program will ask for an account name (e.g., website or app name).
    - You will be prompted to enter the password (input is hidden for security).
    - The password is encrypted and saved.

6. **When you retrieve a password:**
    - Enter the account name.
    - If the password exists, it will be decrypted and displayed.

7. **Files created:**
    - `passwords.json` (stores encrypted passwords)
    - `key.key` (stores the encryption key)