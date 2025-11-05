import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

CSV_FILE = r'expenses.csv Path'

def load_expenses():
    return pd.read_csv(CSV_FILE, parse_dates=['date'])

def save_expenses(date, category, amount, description):
    df = load_expenses()

    new_row = pd.DataFrame({
        'date': [date.strftime('%Y-%m-%d')], 
        'category': [category],
        'amount': [float(amount)],
        'description': [description]
    })

    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(CSV_FILE, index=False)
    print('Expense added successfully!')


def show_summary(df):

    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    print('\nTotal expenses:', df['amount'].sum())
    print('\nExpenses by category:')
    print(df.groupby('category')['amount'].sum())

    print('\nExpenses by month:')
    df['month'] = df['date'].dt.to_period('M')
    print(df.groupby('month')['amount'].sum())


def plot_by_category(df):

    by_category = df.groupby('category')['amount'].sum()
    by_category.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Expenses by category')
    plt.ylabel('')
    plt.show()


def plot_by_month(df):

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['month'] = df['date'].dt.to_period('M')

    by_month = df.groupby('month')['amount'].sum()
    by_month.plot(kind='bar')
    plt.title('Expenses by month')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.show()


def filter_by_category(df, category):

    filtered = df[df['category'].str.lower() == category.lower()]
    print(filtered)


def main():
   

    while True:
        
        print('\n--- Expense Tracker ---')
        print('1. Add new expense')
        print('2. Show summary')
        print('3. Plot expenses by category')
        print('4. Plot expenses by month')
        print('5. Filter by category')
        print('6. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            date_string = input("Enter date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_string, '%Y-%m-%d')
            except:
                print('Invalid date format!')
                continue
            category = input('Enter category: ')
            amount = input('Enter amount: ')
            description = input('Enter description: ')
            save_expenses(date, category, amount, description)

        elif choice == '2':
            df = load_expenses()
            show_summary(df)

        elif choice == '3':
            df = load_expenses()
            plot_by_category(df)

        elif choice == '4':
            df = load_expenses()
            plot_by_month(df)

        elif choice == '5':
            df = load_expenses()
            category = input("Enter category to filter: ")
            filter_by_category(df, category)

        elif choice == '6':
            print('Good Bye!')
            break

        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
        