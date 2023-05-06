class User(object):
    phone_number = ''
    password = ''
    account_balance = 0.0

    def __init__(self, phone_number, password, account_balance=0.0):
        self.phone_number = phone_number
        self.password = password
        self.account_balance = account_balance
    
    def display(self):
        print(f'{self.phone_number} has {self.account_balance} in his account.')

    def is_valid_credential(self, phone_number, password):
        return self.phone_number == phone_number and self.password == password
    
    @staticmethod
    def main_menu():
        print('1: Deposit')
        print('2: Withdraw')
        print('3: Balance Inquiry')
        print('4: Logout')


class BankAccountManager(object):
    users = []

    def display_all_accounts(self):
        for user in self.users:
            user.display()

    def open_account(self, phone_number, password, account_balance=0.0):
        user = User(phone_number=phone_number, password=password, account_balance=account_balance)
        self.users.append(user)

    def login(self, phone_number, password):
        for user in self.users:
            if user.is_valid_credential(phone_number, password):
                return user

    @staticmethod
    def welcome_message():
        print('Welcome to Alee Bank Ltd.')

    @staticmethod
    def main_menu():
        print('1: Open Account')
        print('2: Login')
        print('3: Display All Accounts')
        print('4: Search Account')
        print('5: Exit')



bank_account_manager = BankAccountManager()
BankAccountManager.welcome_message()

while True:
    BankAccountManager.main_menu()
    choice = int(input())
    if choice == 1:
        phone_number = input('Phone Number: ')
        password = input('Password: ')
        account_balance = float(input('Opening Balance: '))
        bank_account_manager.open_account(phone_number, password, account_balance)

    elif choice == 2:
        phone_number = input('Phone Number')
        password = input('Password')
        user = bank_account_manager.login(phone_number, password)
        if user is None:
            print('Invalid  Credentials')
        else:
            User.main_menu()

            
    else:
        break

print('Thank you.')
