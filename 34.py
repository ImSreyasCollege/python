class bank:
    def __init__(self, accno, name, acctype="saving", balance=0) :
        self.accno = accno
        self.name = name
        self.type = acctype
        self.balance = balance
    def deposite(self, amount) :
        self.balance+=amount
        print("available balance is : ", self.balance)
    def withdrow(self, amount) : 
        self.balance-=amount
        print("available balance is : ", self.balance)

name = input("enter the name of the person : ")
accno = int(input("enter the acc number : "))
acctype = input("enter the account type : ")
balance = int(input("enter the balance : "))

obj = bank(accno, name, acctype, balance)

while(True):
    c = int(input("\n1.deposite\n2.withdrow\n3.exit\nEnter the operation : "))
    match c :
        case 1 :
            amount = int(input("enter the amount to deposite : "))
            obj.deposite(amount)
        case 2 :
            amount = int(input("enter the amount to withdrow : "))
            obj.withdrow(amount)
        case 3 :
            exit()
        case _ :
            print("invalid option.")
         

