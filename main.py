is_exit = True



class Banking:
    balance = 0.0
    number_code = [[1,1]]
    code = 1234
    is_login = False

    def deposit(self):
        if self.is_login:
            amount = float(input("Enter desposit amount "))
            self.balance += amount
            print("Desposited successfully ")
        else:
            print("Please Login First ")

    def withdraw(self):
        if self.is_login:
            amount = float(input("Enter amount to withdraw "))
            if amount>self.balance:
                print("Balance not sufficient ")
            else:
                self.balance -= amount
                print("Amount withrdraw successfully ")
        else:
            print("Please Login First ")

    def login(self, ):
        if self.is_login:
            print(" Already Logged In")
        else:
            print("Enter Number and Password ")
            user_number = int(input("> Enter login number "))
            user_code = int(input("> Enter login number "))
            new_element=[user_number,user_code]
            if new_element in self.number_code:
                print("Login successfully  ")
                self.is_login = True
            else:
                print("Login not successful")

    def signup(self):
        print("Enter Number and Password to sign up")
        try:
            user_number = int(input("> Enter signup number "))
            user_code = int(input("> Enter signup number "))
            new = [user_number, user_code]
            if new in self.number_code:
                print("Number already registered ")
            else:
                self.number_code.append(new)
                print("SignUp Successfully  ")

        except ValueError:
            print("Enter correct values ")




print("Welcome to Bank System in Python ")
banking = Banking()


def target(val):
    if val.upper() == "S":
        banking.signup()
    elif val.upper() == "L":
        banking.login()
    elif val.upper() == "D":
        banking.deposit()
    elif val.upper() == "O":
        if banking.is_login==False:
            print(" Already logged out ")
        else:
            banking.is_login=False
            print(" Logged Out Successfully  ")
    elif val.upper() == "W":
        banking.withdraw()
    elif val.upper() == "B":
        print("your balance is = "+str((banking.balance)))
    else:
        print("Please enter correct option ")



while True:
    print("""
    > SignUp - Write S
    > Login  - Write L
    > Balance- Write B
    > Deposit- Write D
    > Withdraw-Write W
    > LogOut - Write O
    > Exit   - Write E
    """)
    value=input("> ")
    if value.upper()=="E":
        break
    else:
        target(value)
