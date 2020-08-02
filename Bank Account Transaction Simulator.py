from time import sleep, asctime
import sys

#A dictionary that stores the database of customers
bank_customers = { 'Tariq':{'J_pip34': 0}, 'Ronaldo':{'P@12cr7':0},
                  'Salah':{'Marh@ba&11':0} }
validator = []
keys = []

# All current passwords in database is stored here to prevent duplicate passwords
for dicts in bank_customers:   
	for words in bank_customers[dicts].items():
		validator.append(words)
        
for i in validator:
    keys.append(i[0])

    def create_account():
        global username,password
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        print("Creating Account....This may take a while")
        sleep(3)
        while True:
                if password in keys:
                        print("Your password is already being used,Be a bit creative")
                        password = input("Please enter your password")
                else:
                        bank_customers[username] = {password:0}
                        keys.append(password)
                        break
        while True:
            if len(password) < 5:
                print("Your password is too short")
                password = input("Please enter your password: ")
                bank_customers[username] = {password:0}                    
            elif len(password) >= 5:
                print("Good")
                break

    def account_login():
        global username, password
        username = input("Please enter your Username: ")
        password = input("Please enter your password: ")
        if username not in bank_customers:
            print("Invalid Customer, please create an account")  
            create_account()
        elif username in bank_customers:
            print("You're valid")
        while True:
            if len(password) < 5:
                print("Your password is too short")
                password = input("Please enter your password")
            elif len(password) >= 5:
                break
        global account
        account = print("Your username is", username, "and your password is", password)

    def deposit():
        deposit_amount = int(input("How much would you like to deposit: "))
        bank_customers[username][password] += deposit_amount                       # This variable adds amount to be deposited to bank account
        sleep(2)
        print("You have", bank_customers[username][password], "cedis in your bank account")
        sleep(2)
        print("You deposited money into your account on", asctime())

    def withdraw():
        withdrawal = int(input("How much money would you like to withdraw: "))     
        if withdrawal < bank_customers[username][password]:
            bank_customers[username][password] -= withdrawal
            withdrawn = bank_customers[username][password]
            sleep(2)
            print("You have withdrawn", withdrawal," cedis from your bank account")
            sleep(2)
            print("Your remaining balance is",withdrawn,"cedis")
            sleep(2)
            print("You withdrew money from your account on", asctime())
        elif withdrawal > bank_customers[username][password]:
            print("You have insufficient funds to carry out this process")

    def disp_curr_bal():
        sleep(1)
        print("Your current balance is ", bank_customers[username][password], "cedis")
    
    def main():
        print("What banking transaction would you like to perform", username,": ")
        choice = (int(input("1-Deposit,2-Withdrawal,3-Display Current Balance,4-SignUp/SignIn Menu,5-exit: ")))
        if choice == 1:
            deposit()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            disp_curr_bal()
        elif choice == 4:
            user_menu()
        elif choice == 5:
            print("We hope you enjoyed our services\nBye")
            sys.exit()
        main()

    def user_menu():
        print("Welcome to the Ecobank banking app: ")
        question1 = (input("Do you have an account. Yes/No"))
        while True:
            if question1 == 'No' :
                question2 = (input("Do you want to create a bank account.Yes/No"))
                if question2 == 'Yes':
                    create_account()
                    main()
                elif question2 == "No":
                    print('Bye')
                    sys.exit()
            else:
                if question1 == "Yes":
                    account_login()
                    main()
                elif question1 != "Yes" or "yes":
                    question1 = (input("Do you have an account. Yes/No")) 
             
user_menu()
