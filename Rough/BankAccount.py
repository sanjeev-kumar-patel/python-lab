class BankAccount:
    miniBalance = 1000
    def __init__(self,passWord) :
        self.__passWord = passWord
    
    def deposit(self, val):
        self.miniBalance = self.miniBalance + val
        return self.miniBalance

    def withdraw(self, val):
        if self.miniBalance > val:
            self.miniBalance = self.miniBalance - val
            print("Successful")
            print("Left amount is", self.miniBalance)
        else:
            print("Not enough amount")
ba = BankAccount()
print(ba.deposit(200))
ba.withdraw(500)