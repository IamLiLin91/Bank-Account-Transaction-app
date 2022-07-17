# Bank-Account-Transaction-app
## Background
A bank account is a financial account that is maintained by a bank or financial institution, and is used to record the financial transactions between the bank and the customer. With the advent of smartphones, banks have introduced mobile banking, and account holders are now able to track their transaction history this has allowed them to make a more informed financial decisions in a timely manner.

An example of a mobile banking transaction is shown below:

![image](https://user-images.githubusercontent.com/109471364/179405516-0e026c70-e7fd-491c-95c7-eecf4ffcaf6b.png)

## Task
Your task is to implement a simple banking account transaction program, that tracks and records each transaction done within that account. You are to use a doubly-linked list where each node represents a transaction. To simplify the problem, we shall only consider 2 types of transaction:

- Deposit: To represent any fund addition to the account
- Withdrawal: To represent any fund deduction from the account

In order to do this, you are to implement the class Account that has all the necessary attributes and methods to process and record any transaction associated with an instance of the bank account. It MUST include the following:

- subclass Transaction that holds the following variables for each transaction instance:

   * trans which stores the transaction type and amount as a key-value pair
   * dt which stores the datetime of the transaction (Hint: you may use the datetime module)
   * next which holds the memory address of the next transaction (default value of None)
   * prev which holds the memory address of the prev transaction (default value of None)
- constructor method that initializes the following when an instance of a bank account is created:

   * last which holds the latest transaction made (default value of None)
   * first which holds the earliest transaction made (default value of None)
   * size (default value of 0) which represents the number of transactions
   * balance (default value of 0)
- method __len__ that returns the number of transactions.
- method isEmpty that returns True is there was no recorded transaction
- static method isValidAmt that takes in a transaction amount (withdraw or deposit) and returns True if the input is valid (accepts only positive numbers)
- method deposit that takes in the deposit amount as input and adds it to the balance.
- method withdraw that takes in the the withdrawal amount as input and deducts it from the balance. It should print an error message if the withdrawal amount exceeds the balance.
- method getHistory that prints out the account transaction history. It should display the latest transaction first.
- any other classes, attributes or methods that you think is necessary

You are to use docstrings to summarize the functionality and list down the members (subclasses, varibles, methods) within the class. Each subclasses and methods should have their own docstrings.
