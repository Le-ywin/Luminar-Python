# class Bank

# meth1 : name, ac_type, balance

# meth2 : amount_deposit

# meth3 : amount_withdrawal

# meth4 : show balance



class Bank:

    def __init__(self,name,ac_type,balance):
        
        self.name = name

        self.balance = balance

    def deposit(self,amount):

        self.balance += amount

        print(f"{amount}rs/- deposited successfully.")

    def withdrawal(self,amount):

        if amount > self.balance:

            print("Insufficient Balance!!!")

        else:

            self.balance -= amount

            print(f"{amount}rs/- withdrawn successfully.")

    def s_balance(self):

        print(f"{self.name} Balance Amount : {self.balance}")


my_accout = Bank(name="RAMADAS S",ac_type="Savings Account",balance=25000)

my_accout.deposit(1000)

my_accout.s_balance()

my_accout.withdrawal(2000)