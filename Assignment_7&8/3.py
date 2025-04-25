# Write a Python program to create a class representing a bank. Include methods for managing
# customer accounts and transactions.

class Bank:
    pin = None
    balance =0
    counter = 1001
    _accNo = None 
    
    def __init__(self):
        print("Welcome to Arshad Bank")
        self.pin = int(input("Enter your pin: "))
        print("Congrats your pin is created!")
        self._accNo = Bank.counter
        Bank.counter += 1
        
        print("Your acc no is:", self._accNo)
    
        
    def checkbalance(self):
        try:
            x = int(input("To check balance enter your pin: "))
            if x == self.pin:
                print("Your balance is:", self.balance)
            else:
                print("Wrong pin")
        except:
            print("Wrong pin")
    
    def get_accNo(self):
        return self._accNo
    
    def set_accNo(self, accNo):
        if type(accNo) == int:
            self._accNo = accNo
        else:
            print("Wrong acc no")
    def deposit(self):
        try:
            x = int(input("To deposit enter your pin: "))
            if x == self.pin:
                self.balance += int(input("Enter amount to deposit: "))
            else:
                print("Wrong pin")
        except:
            print("Wrong pin")
            
    def withdraw(self):
        try:
            x = int(input("To withdraw enter your pin: "))
            if x == self.pin:
                self.balance -= int(input("Enter amount to withdraw: "))
            else:
                print("Wrong pin")
        except:
            print("Wrong pin")
        


Arshad = Bank()
print("Enter your choice")
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Arshad.checkbalance()
    elif choice == 2:
        Arshad.deposit()
    elif choice == 3:
        Arshad.withdraw()
    elif choice == 4:
        break
    else:
        print("Enter a Valid choice!")
