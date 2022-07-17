from bank import Account

# Test Case 1
acc = Account()
print(f"Is account empty? {acc.isEmpty()}")
print(f"Number of transactions: {acc.size}")
'''
Expected output:

Is account empty? True
Number of transactions: 0
'''


# Test Case 2
acc.deposit(1000)
acc.deposit(2000)
acc.deposit(888)
print(f"Account Balance: {acc.balance}")
print(f"Number of transactions: {acc.size}")
'''
Expected output:

First deposit: 1000

Deposit: 2000

Deposit: 888
Account Balance: 3888.0
Number of transactions: 3
'''


# Test Case 3
acc.withdraw(888)
acc.withdraw(500)
print(f"Account Balance: {acc.balance}")
print(f"Number of transactions: {acc.size}")
'''
Expected output:

withdraw: 888

withdraw: 500
Account Balance: 2500.0
Number of transactions: 5
'''


# Test Case 4
acc.getHistory()
'''
Expected output:

2022-02-01 22:28:19.448604 {'w': 500}
2022-02-01 22:28:19.448604 {'w': 888}
2022-02-01 22:28:19.448122 {'d': 888}
2022-02-01 22:28:19.447130 {'d': 2000}
2022-02-01 22:28:19.447130 {'d': 1000}
'''


# Test Case 5
print(acc.isValidAmt(50))
print(acc.isValidAmt("wang"))
print(Account.isValidAmt(50))
print(Account.isValidAmt("wang"))
'''
Expected output:

True
False
True
False
'''


# Test Case 6
acc.deposit("wang")
acc.withdraw("wang")
acc.withdraw(1000000)
acc.getHistory()
'''
Expected output:

Invalid deposit amt: wang

Invalid withdraw amt: wang

Insufficient balance
2022-02-01 22:35:19.652944 {'w': 500}
2022-02-01 22:35:19.652944 {'w': 888}
2022-02-01 22:35:19.651944 {'d': 888}
2022-02-01 22:35:19.651944 {'d': 2000}
2022-02-01 22:35:19.650943 {'d': 1000}
'''
