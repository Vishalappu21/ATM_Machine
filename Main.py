# Mini ATM Machine 


account_balance = 5000

def withdrawal(balance, amount):
    if amount <= 0:
        print("Please enter an amount greater than 0.")
        return balance

    if amount > balance:
        print("Insufficient amount. Please check your balance.")
        return balance

    balance -= amount
    print(f"Withdrawal successful. Remaining balance: {balance}")
    return balance


def deposit(balance, amount):
    if amount <= 0:
        print("Please enter an amount greater than 0.")
        return balance

    balance += amount
    print(f"Deposit successful. Current balance: {balance}")
    return balance

    
while True:
    user_need = int(
        input(
            '1 for check balance\n'
            '2 for Withdrawl\n'
            '3 for Deposit\n'
            '4 for Exit \n'
            'Please select the Option : '
        )
    )
    if user_need == 1:
        print(f'Balance: {account_balance}')
    elif user_need == 2:
        amount_need  = int(input('Please Enter Amount: '))
        account_balance = withdrawal(account_balance,amount_need)

    elif user_need == 3:
        amount_deposit = int(input('Please Enter Amount: '))
        account_balance = deposit(account_balance,amount_deposit)

    elif user_need == 4:
        print('Thanks for Using Vishal ATM...')
        break
    else:
        print('Please enter the valid option... Thank you')
        break
            