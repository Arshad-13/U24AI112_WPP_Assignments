# 1. Write a class called Password_manager. The class should have a list called old_passwords that
# holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
# There should be a method called get_password that returns the current password and a method
# called set_password that sets the user’s password. The set_password method should only
# change the password if the attempted password is different from all the user’s past passwords.
# Finally, create a method called is_correct that receives a string and returns a boolean True or
# False depending on whether the string is equal to the current password or not.

class password:
    def __init__(self):
        self.old_passwords = []
        self.current_password = None
        
    def get_password(self):
        return self.current_password

    def set_password(self, password):
        if password != self.old_passwords:
            self.old_passwords.append(password)
            self.current_password = password
        else:
            print("Password already exists")

    def is_correct(self, password):
        if password == self.current_password:
            return True
        else:
            return False
        

p = password()

while True:
    x = int(input("1.Do you want to set password: \n2.Do you want to check password: \n3.Do you want to see your recent password\n4.Do you want to check you password\n5.Exit\n "))
    if x == 1:
        p.set_password(input("Enter password: "))
    elif x == 2:
        print(p.is_correct(input("Enter password: ")))
    elif x == 3:
        print(p.old_passwords)
    elif x == 4:
        print(p.get_password())
    elif x == 5:
        break

    
