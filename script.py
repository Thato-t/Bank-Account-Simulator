dbs = [{'name': 'Thato', 'pin': 12, 'balance': 200, 'savings': 3000}]
welcome_msg = '\n~~Welcome to bank simulator~~\n'.upper()

class Account:
    def __init__(self):
        self.name = ''
        self.pin  = ''
        self.balance = 0
        self.savings = 0

    def __str__(self):
        return f'Account(name={self.name}, pin={self.pin}, balance={self.balance}, savings={self.savings})'

    def login(self):
        self.name = input('Enter your name: ')
        self.pin = input('Enter your pin, it must be two digits: ')
        for db in dbs:
            if db['name'] == self.name and db['pin'] == int(self.pin):
                print(f'Welcome {self.name}')
                return True
            else:
                print('Account not found. Please try again.')
                return None

    def create_account(self):
        self.name += input('Enter your name: ')
        self.pin += input('Enter your pin, it must be two digits: ')
        details = { 'name': self.name, 'pin': int(self.pin) }
        dbs.append(details)
        print(f'Welcome {self.name}')
        return True

    def balance(self):
        print(f'You have {self.amount} in you account.')

    def deposit(self):
        amount = input('Enter the amount to deposit: ')
        self.balance += int(amount)
        print(f'You have deposited R{amount}. Your new balance is R{self.balance}.')

user = Account()


def balances():
    while True:
        # user.balance()
        print(1, 'Deposit')
        print(2, 'Withdraw current balance')
        print(3, 'Withdraw from savings')
        print(4, 'Exit\n')
        choice = input('Enter your choice: ')

        if choice == '1':
            user.deposit()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            exit()
        else:
            print(f'{choice} is no valid try again one last time or exit the programme')



def flow():
    while True:
        print(welcome_msg)
        print(1, 'Login')
        print(2, 'Create account')
        print(3, 'Exit\n')
        choice = input('Enter your choice: ')
        if choice == '1':
            user.login()
            balances()
        elif choice == '2':
            user.create_account()
            balances()

        elif choice == '3':
            exit()
        else:
            print('Invalid choice. Please try again.')

        
        

            
flow()