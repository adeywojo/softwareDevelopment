import random # For random account number generation
# Initialize the system

# Database to store customer data
database = {} 

def init():

    print("Welcome to Bank Python")
  
    have_account = int(input("Do you have an account with us? 1: Yes, 2: No \n"))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected an invalid option. Please try again.")
        init()

def login():

    print("****** Login ******")
    try:
        account_number_from_user = int(input("Enter your account number: \n"))
        password = input("Enter your password: \n")

        for account_number, user_details in database.items():
            if (account_number == account_number_from_user and user_details[3] == password):
                bank_operations(user_details)
    except:
        print("Invalid account or password. Please try again.")
        login()
    
def register():

    print("****** Register ******")

    email = input("Enter your email address: \n")
    first_name = input("Enter your Firstname: \n")
    last_name = input("Enter your Lastname: \n")
    password = input("Create a Password: \n")
    account_number = generate_account_number()
    # account_number = (f"PY{generate_account_number()}") -- This method can be used if a string prefix is required.

    database[account_number] = [first_name, last_name, email, password]
 
    print(f"Registration Completed Successfully! \n Your account number is {account_number}")

    login()

def bank_operations(user):
    print(f"Welcome {user[1]} , {user[2]}")

    selected_option = int(input("What would you like to do today? 1. Deposit 2. Make a Withdrawal 3. Logout 4. Exit \n"))

    if (selected_option == 1):
        deposit_operation()
    elif (selected_option == 2):
        withdrawal_operation()
    elif (selected_option == 3):
        logout()
    elif (selected_option == 4):
        exit()
    else:
        print("Invalid option selected.")
        bank_operations(user)

def withdrawal_operation():
    print("Withdrawal")

def deposit_operation():
    print("Deposit Operations")

def generate_account_number():
    
    return random.randrange(1111111111,9999999999)
    # learn to to generate a user sequence account number

def logout():
    login()

#### Initializing the Application
init()

