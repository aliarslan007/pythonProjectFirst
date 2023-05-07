class User(object):
    phone_number = ''
    password = ''
    account_balance = 0.0

    def __init__(self, phone_number, password, account_balance=0.0):
        self.phone_number = phone_number
        self.password = password
        self.account_balance = account_balance

    def display(self):
        print(f' Your account number {self.phone_number}: has ${self.account_balance} balance in your account.')

    def is_valid_credential(self, phone_number, password):
        return self.phone_number == phone_number and self.password == password

    def is_valid_user(self, phone_number):
        return self.phone_number == phone_number

    def deposit(self):
        amount = float(input("Enter desposit amount "))
        if amount < 0:
            print("Pleas enter valid amount ")
        else:
            self.account_balance += amount
            print("Desposited successfully ")

    def withdraw(self):
        amount = float(input("Enter withdraw amount "))
        if (self.account_balance-amount)<0:
            print("Balance not sufficient  ")
        else:
            self.account_balance -= amount
            print("Withdrew successfully ")

    @staticmethod
    def main_menu():
            print('1: Deposit')
            print('2: Withdraw')
            print('3: Balance Inquiry')
            print('4: Logout')
            return int(input(">> "))


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

    def search_Account(self, search_account_number):
        for user in self.users:
            if user.is_valid_user(search_account_number):
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
        # return input(">> ")


bank_account_manager = BankAccountManager()
BankAccountManager.welcome_message()

while True:
    BankAccountManager.main_menu()
    choice = int(input(">> "))
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
            while True:
                inner_choice=User.main_menu()
                if inner_choice == 1:
                    user.deposit()
                elif inner_choice == 2:
                    user.withdraw()
                elif inner_choice == 3:
                    user.display()
                elif inner_choice == 4:
                    break
                else:
                    print("Please enter valid option  ")

    elif choice == 3:
        bank_account_manager.display_all_accounts()

    elif choice == 4:
        search_account = input("Enter Account Number to search: ")
        user = bank_account_manager.search_Account(search_account)
        if user is None:
            print("Account doesn't exist")
        else:
            print(" Account number " + user.phone_number + " exists. ")

    elif choice == 5:
        break

    else:
        print("please enter valid option number. Thank you ")

print('Thank you.')
