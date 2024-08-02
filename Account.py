class Account:
    def __init__(self, holder, number, balance):
        self.balance = 0
        self.number = number
        self.holder = holder

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        if(balance < 0):
            print("O saldo não pode ser negativo.")
        else:
            self._balance = balance

    def withdraw(self, value):
        if(self.balance >= value):
            self.balance -= value
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def deposit(self, value):
        self.balance += value
    
    def extract(self):
        print("Cliente: ", self.holder, " Saldo Atual: ", self._balance)