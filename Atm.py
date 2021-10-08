class atm:
    def __init__(self, cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def BalanceEnquiry(self):
        print("your balance is: $100")

    def CashWithdrawl(self,amount):
        new_amount = 100-amount
        print("you withdrawed: " + str(amount) + "your remaining balance is: " + str(new_amount))
