dbs = {}
welcome_msg = '\n~~Welcome to python bank~~\n'.upper()

class Account:
    def __init__(self):
        self.name = ''
        self.pin  = ''
        self.balance = 0
        self.savings = 0

    def __str__(self):
        return f'Thank you for using our bank {self.name}, you have R{self.balance} into your account and R{self.savings} in your savings account.'

    def login(self):
        self.name = input('Enter your name: ')
        self.pin = input('Enter your pin, it must be two digits: ')
        for db in dbs:
            if db['name'] == self.name and db['pin'] == float(self.pin):
                print(f'Welcome {self.name}')
                return True
            else:
                print('Account not found. Please try again.')
                return None

    def create_account(self):
        global dbs
        self.name += input('Enter your name: ')
        self.pin += input('Enter your pin, it must be two digits: ')
        dbs = { 'name': self.name, 'pin': self.pin, 'balance': 0, 'savings': 0 }
        print(f'\nWelcome {self.name}')
        print(f'You have R{self.balance} in your account')
        return True

    def deposit(self):
        amount = input('Enter the amount to deposit: ')
        self.balance += float(amount)
        dbs['balance'] = self.balance 
        print(f'You have deposited R{amount}. Your new balance is R{self.balance}.')
        return True

    def deposit_to_savings(self):
        if not self.balance: return
        amount = input('Enter the amount to deposit: ')
        if float(amount) > self.balance:
            print(f'R{amount} is greater than R{self.balance}')
        else:
            self.savings += float(amount)
            self.balance -= float(amount)
            dbs['savings'] = self.savings
            print(f'You have deposited R{amount} to your savings. Your new balance is R{self.balance}. New savings balance R{self.savings}')

    def withdraw(self):
        if self.balance:
            amount = input('Enter the amount you want to withdraw: ')
            if amount.isalpha():
                print('Enter a number')
            else:
                self.balance -= float(amount)
                dbs['balance'] = self.balance
                print(f'You have withdrawed R{amount}, you are left with R{self.balance}')
        else:
            print(f'You have R{self.balance}, so you can\'t make any withdrawals')

    def withdraw_savings(self):
        if self.savings:
            amount = input('Enter the amount you want to withdraw: ')
            if amount.isalpha():
                print('Enter a number')
            else:
                self.savings -= float(amount)
                self.balance += float(amount)
                dbs['balance'] = self.balance
                dbs['savings'] = self.savings
                print(f'You have withdrawed R{amount}, you are left with R{self.savings}. current balance is R{self.balance}')
        else:
            print(f'You have R{self.savings}, so you can\'t make any withdrawals')


user = Account()

def balances():
    while True:
        # user.balance()
        print(1, 'Deposit')
        print(2, 'Deposit to savings')
        print(3, 'Withdraw current balance')
        print(4, 'Withdraw from savings')
        print(5, 'Exit\n')
        choice = input('Enter your choice: ')

        if choice == '1':
            user.deposit()
        elif choice == '2':
            user.deposit_to_savings()
        elif choice == '3':
            user.withdraw()
        elif choice == '4':
            user.withdraw_savings()
        elif choice == '5':
            print(f'\n{user}\n')
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
            print('Thank you for using PYTHON bank')
            exit()
        else:
            print('Invalid choice. Please try again.')
            
flow()