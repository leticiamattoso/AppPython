class Main:
    pass

print("Testando o projeto")

from Client import Client

from Account import Account

c1 = Client("Leonardo", "1234-1234")
account = Account(c1._name, 6565, 0)

account.deposit(100)
account.withdraw(50)
account.extract()