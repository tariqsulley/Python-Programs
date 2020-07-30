import time
from time import sleep 
from sys import exit as ex

#A dictionary that stores the database of customers
Bank_Customers ={ 'Tariq':{'J_pip34': 0}, 'Ronaldo':{'P@12cr7':0},
                  'Salah':{'Marh@ba&11':0} }
validator = []
Keys = []

# All current passwords in database is stored here to prevent duplicate passwords
for dicts in Bank_Customers:   
	for words in Bank_Customers[dicts].items():
		validator.append(words)
        
for i in validator:
    Keys.append(i[0])



    def create_account():
        
        global username,password
        username = input("Please enter your username")
        password = input("Please enter your password")
        print("Creating Account....This may take a while")
        sleep(3)
        while True:
                if password in Keys:
                        print("Your password is already being used,Be a bit creative")
                        password = input("Please enter your password")
                else:
                        Bank_Customers[username] = {password:0}
                        Keys.append(password)
                        break
        while True:
            if len(password) < 5:
                print("Your password is too short")
                password = input("Please enter your password")
                Bank_Customers[username] = {password:0}                    
            elif len(password) >= 5:
                print("Good")
                break

    def account_login():
        global username, password
        username = input("Please enter your Username")
        password = input("Please enter your password")
        if username not in Bank_Customers:
            print("Invalid Customer, please create an account")  
            create_account()

        elif username in Bank_Customers:
            print("You're valid")
        while True:
            if len(password) < 5:
                print("Your password is too short")
                password = input("Please enter your password")
            elif len(password) >= 5:
                break

        global Account
        Account = print("Your username is", username, "and your password is", password)

    def deposit():
        deposit_amount = int(input("How much would you like to deposit"))
        Bank_Customers[username][password] += deposit_amount                       # This variable adds amount to be deposited to bank account
        sleep(2)
        print("You have", Bank_Customers[username][password], "cedis in your bank account")
        sleep(2)
        print("You deposited money into your account on",time.asctime())


    def withdraw():
        withdrawal = int(input("How much money would you like to withdraw:"))     
        if withdrawal < Bank_Customers[username][password]:
            Bank_Customers[username][password] -= withdrawal
            withdrawn = Bank_Customers[username][password]
            sleep(2)
            print("You have withdrawn", withdrawal, " cedis from your bank account")
            sleep(2)
            print("Your remaining balance is", withdrawn , "cedis")
            sleep(2)
            print("You withdrew money from your account on",time.asctime())
        elif withdrawal > Bank_Customers[username][password]:
            print("You have insufficient funds to carry out this process")

    def disp_curr_bal():
        sleep(1)
        print("Your current balance is ", Bank_Customers[username][password], "cedis")
    def Main():
        print("What banking transaction would you like to perform", username)
        choice = (int(input("1-Deposit,2-Withdrawal,3-Display Current Balance,4-SignUp/SignIn Menu,5-exit:")))
        if choice == 1:
            deposit()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            disp_curr_bal()
        elif choice == 4:
            UserMenu()
        elif choice == 5:
            print("We hope you enjoyed our services\nBye")
            ex()
        Main()

    def UserMenu():
        print("Welcome to the Ecobank banking app")
        Question1 = (input("Do you have an account. Yes/No"))
        while True:
            if Question1 == 'No' :
                Question2 = (input("Do you want to create a bank account.Yes/No"))
                if Question2 == 'Yes':
                    create_account()
                    Main()
                elif Question2 == "No":
                    print('Bye')
                    ex()
              
            else:
                if Question1 == "Yes":
                    account_login()
                    Main()
                elif Question1 != "Yes" or "yes":
                    Question1 = (input("Do you have an account. Yes/No")) 
         
        
        
UserMenu()
