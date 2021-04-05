# This is a mock ATM Project
import datetime

allowedUsers = ['Yinka', 'Wale', 'Anu']
allowedPassword = ['psYinka', 'psWale', 'psAnu']

name = input('Enter your name: \n')

if name in allowedUsers:
    password = input('Your password: \n') 
    userId = allowedUsers.index(name)

    if password == allowedPassword[userId]:
        print('Welcome %s' % name + '!')
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('The time is: ' + str(datetime.datetime.now()))
        selectedOption = int(input('Please select an option: '))
        
        if selectedOption == 1:
            withdrawnAmount = float(input('How much would you like to withdraw?'))
            print('Take your cash.')
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')

        elif selectedOption == 2:
            depositedAmount = float(input('How much would you like to deposit?'))
            print('Your current balance is $ %d' % depositedAmount)
            #depositedAmount += depositedAmount
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')
            
        elif selectedOption == 3:
            reportedIssue = input('What issue would you like to report? ')
            print('Thank you for contacting us.')
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')
            
        else:
            print('Invalid option selected. Please try again.')
    else:
        print('Password is incorrect, please try again')

else:
    print('Name not found, try again')
