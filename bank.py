owner = "Praveen"
balance = 0

def deposit(amount):
    global balance
    balance += amount
    return "Successfull Deposit:",amount
 
def withdraw(amount):
    global balance
    if amount > 0:
        if amount <= balance:
            balance -= amount
            return True  
        else:
            return False  
    else:
        print("Withdrawal amount must be positive.")
        return False  

def get_balance():
    return balance

def get_owner():
    return owner
