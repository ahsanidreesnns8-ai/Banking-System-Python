#2025-CYS-112
#Ahsan Idrees
#Banking System
#Allied Bank
import time
from datetime import datetime
class Bank:
    def __init__(self,acc_name,acc_pin,issue_date,exp_date,balance):
        self.acc_name=acc_name
        self.acc_pin=int(acc_pin)
        self.exp_date=exp_date
        self.issue_date=issue_date
        self.balance=balance
        self.transactions=[]

    def deposit(self):
        print('\nHere is your account details..')
        print(f'\nName: {self.acc_name}')
        print(f'\nAccount Pin: {self.acc_pin}')
        print(f'\nAccount Balance: {self.balance}')
        print(f'\nIssuance date: {self.issue_date}')
        print(f'\nExpiry Date: {self.exp_date}')
        
        deposit_amount=int(input("\nEnter your deposit amount: "))
        count=0
        while True:
             user_pin=int(input("Enter your Account pin: "))
             count+=1
             if user_pin==self.acc_pin:
                 self.balance+=deposit_amount
                 print('Searching...')
                 for i in range(101):
                     print(f'\r{i}',end='')
                     time.sleep(0.1)
                 print()
                 print(f'You have deposited {deposit_amount} Rs.')
                 print(f'Total Amount in Your Account is: {self.balance} Rs.')
                 print(datetime.now().strftime("Date: %Y-%m-%d | Time: %H:%M:%S"))
                 print()
                 break
             elif user_pin!=self.acc_pin:
                 print('Searching...')
                 for i in range(101):
                     print(f'\r{i}',end='')
                     time.sleep(0.1)
                 print()
                 print("You have entered wrong key.")
                 print("Please enter the right key.")
             if count==3:
                print("You have reached maximum number of Limits")
                print('Please wait for 24 Hours.')
                break

    def withdraw(self):
        print('\nHere is your account details..')
        print(f'\nName: {self.acc_name}')
        print(f'\nAccount Pin: {self.acc_pin}')
        print(f'\nAccount Balance: {self.balance}')
        print(f'\nIssuance date: {self.issue_date}')
        print(f'\nExpiry Date: {self.exp_date}')
        withdrawal_amount=int(input("\nEnter how many amount you want to withdraw: "))
        while True:
            if withdrawal_amount>self.balance:
                print(f'You can not withdraw this amount beacause amount in your account is {self.balance} Rs. currently.')
                break
            count=0
            user_pin=int(input("\nEnter your Account pin: "))
            count+=1
            if withdrawal_amount>self.balance:
                print(f'You can not withdraw this amount beacause amount in your account is {self.balance} Rs. currently.')
                break
            if int(user_pin)==int(self.acc_pin):
                self.balance-=withdrawal_amount
                print('Searching...')
                for i in range(101):
                    print(f'\r{i}',end='')
                    time.sleep(0.1)
                print()
                print('-'*17)
                print(f"You have withdrawn {withdrawal_amount} Rs. from you account.")
                print(f"Your ramaining balance is: {self.balance} Rs.")
                print(datetime.now().strftime("Date: %Y-%m-%d | Time: %H:%M:%S"))
                print('-'*17)
                break
            elif user_pin!=self.acc_pin:
                if count==3:
                    print("Account Block..")
                    print("You have reached your maximum Limits")
                    break
                print('Searching...')
                for i in range(101):
                    print(f'\r{i}',end='')
                    time.sleep(0.1)
                print()
                print("Access denied...")
                print("You have entered a wrong key...")
    
    def print_bill(self):
        print("\n" + "="*50)
        print(f"{'APNA BANK (LTD.)':^50}")
        print("="*50)
        print(f"Account Holder : {self.acc_name}")
        print(f"Account Pin    : {self.acc_pin}")
        print(f"Issue Date     : {self.issue_date}")
        print(f"Expiry Date    : {self.exp_date}")
        print("-"*50)
        print(f"{'Transaction':<20}{'Amount':>12}{'Balance':>15}")
        print("-"*50)
        for t_type, amount, bal in self.transactions:
            print(f"{t_type:<20}{amount:>10} Rs   {bal:>10} Rs")
        print("-"*50)
        print(f"{'Current Balance':<20}{self.balance:>10} Rs")
        print("="*50)
        print(f"{'Thank You for Banking with Us!':^50}")
        print("="*50)
        print(datetime.now().strftime("Date: %Y-%m-%d | Time: %H:%M:%S"))
        
Account1=Bank('Ahsan', 1230 , '1-1-2026', '31-12-2026', 10000)
Account1.deposit()
Account1.withdraw()
Account1.print_bill()