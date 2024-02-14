def displayMenu():
    print()
    print("MENU".center(20,'-'))
    print("1.Withdraw")
    print("2.Deposite")
    print("3.Check Balance")
    print("4.Change Pin")
    print("5.Exit")

#Withdraw
def withdraw():
    
    global pin1, balance
    while True:
        print()
        user_pin = input("Enter Your Pin: ")
        if user_pin == pin1:
            while True:
                amount = int(input("Enter Amount to Withdraw: "))

                if amount > balance:
                    print("Insufficeint Balance ! Balance:",balance)
                else:
                    balance-=amount
                    print("Withdraw Sucessfull 🙂! Balance:",balance)
                    break
            break
        else:
            print("Invalid Pin !!")
            
# Deposite
def deposite():
    global balance
    print()
    while True:
        user_pin = input("Enter Your Pin: ")
        if user_pin == pin1:
            amount = int(input("Enter Amount to Deposite: "))
            balance+=amount
            print("Withdraw Sucessfull 🙂! Balance:",balance)
            break
        else:
            print("Invalid Pin!!")
            
# Balance Check 
def check_balance():
    while True:
        user_pin = input("Enter Your Pin: ")
        if user_pin == pin1:
            print("Name: ",name)
            print("Balance: ",balance)
            break
        else:
            print("Invalid Pin 🚫!!")
            
# Pin Change
def changePin():
    global pin1
    while True:
        user_pin = input("Enter Your Pin: ")
        if user_pin == pin1:
            while True:
                new_pin = input("Enter New Pin: ")
                confirm_pin = input("Confirm Pin: ")
                if new_pin == confirm_pin:
                    pin1 = new_pin  # Update the global pin1 variable
                    print("Pin Updated Successfully ☺️!")
                    break
                else:
                    print("Passwords do not match. Please recheck the Pin.")
            break
        else:
            print("Invalid Pin")
            
# Main Function To Call other Functions
def main():
    while True:
        displayMenu()
        ch = int(input("Enter Choice: "))
        
        if ch == 1:
            withdraw()
        elif ch == 2:
            deposite()
        elif ch == 3:
            check_balance()
        elif ch == 4:
            changePin()
        elif ch == 5:
            break
        else:
            print("Wrong Input ❌!!\nPlease Enter  Choice Again.")
    print("Thank You !!!!")
    
# Main Code
# Taking Inputs
print()
name = input("Enter Name: ")
balance = int(input("Set Balance: "))
while True:
    print()
    pin1 = input("Enter Pin: ")
    pin2 = input("Confirm Pin: ")
    if pin1==pin2:
        print("Pin Set Successfully 🫡")
        break
    else:
        print("Password Not Matching")
        
# Calling the Main Function
main()









##```bash
    #python random_password_generator.py
    #```##