from datetime import datetime
from termcolor import colored

class Account:
    
    class Transaction:
        def __init__(self, trans={}, dt=datetime.now()):
            self.trans = trans
            self.dt = dt
            self.next = None
            self.prev = None
            
     
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        self.balance = 0
    
    
    def __len__(self):
        return self.size
    
    
    def isEmpty(self):
        return self.size == 0
    
    
    def isValidAmt(amt):# static method
        if (type(amt) == float or type(amt) == int):
            if amt > 0:
                return True
            else:
                return False
        else:
            return False
        
    
    def deposit(self, amt):
        if Account.isValidAmt(amt) == True:
            self.balance += amt
            new_transaction = self.Transaction({'Deposit':'$'+colored(' +{}'.format(amt),'green')}, datetime.now())
            if self.first is None:
                self.first = self.last = new_transaction
                self.size += 1 
            else:
                new_transaction.prev = self.last
                new_transaction.next = None
                self.last.next = new_transaction
                self.last = new_transaction
                self.size += 1  
        else:
            print("Invalid deposit!")
        
        
    def withdraw(self, amt):
        if Account.isValidAmt(amt) == True:
            if self.balance >= amt and self.balance != 0:
                self.balance -= amt
                new_transaction = self.Transaction({'Withdrawal':'$'+colored(' -{}'.format(amt),'white')}, datetime.now())
                if self.first is None:
                    self.first = self.last = new_transaction
                    self.size += 1
                else:
                    new_transaction.prev = self.last
                    new_transaction.next = None
                    self.last.next = new_transaction
                    self.last = new_transaction
                    self.size += 1  
            else:
                print("Insufficient balance!")
        else:
            print("Invalid withdrawal!")
   

    def getHistory(self):
        print('Available Balance:\n    $ {}'.format(self.balance), end = '\n')
        if self.size == 0:
            print("No Transaction found.")
        else:
            print("Transaction History:"+'\n'+("-"*65))
            n = self.last
            for i in range(self.size):
                for keys in n.trans.keys():
                    for values in n.trans.values():
                        print(f'{keys: <20}', f'{values: <25}', n.dt)
                n = n.prev