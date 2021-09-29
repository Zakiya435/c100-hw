class atm:
    def __init__(self,cardNo,pin, userId,bal):
        self.cardNo=cardNo
        self.pin=pin
        self.userId = userId
        self.bal = bal

    def CashWithdrawl(self):
        amount = int(input("Enter the amount to withdraw"))
        self.bal = self.bal-amount
        print(self.bal)

    def BankInquiry(self):
        print("This is your balance: "+self.bal)

    def Deposit(self):
       amount = int(input("Enter the amount to deposit"))
       self.bal = self.bal+amount
       print(self.bal)

one = atm(123,1000,786,110000)
choice = int(input("For Withdraw press 1, for checking press 2, for deposit press 3: "))

if choice == '1':
    one.CashWithdrawl()
elif choice == '2':
    one.BankInquiry()
elif choice == '3':
    one.Deposit()
