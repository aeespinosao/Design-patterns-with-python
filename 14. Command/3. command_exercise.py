"""
Command Coding Exercise
Implement the Account.process()  method to process different account commands.
The rules are obvious:
success indicates whether the operation was successful
You can only withdraw money if you have enough in your account
"""

from enum import Enum

class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False
        
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == command.Action.WITHDRAW:
            self.withdraw(command)
        elif command.action == command.Action.DEPOSIT:
            self.deposit(command)
            
    def withdraw(self, command):
        if self.balance >= command.amount:
            self.balance -= command.amount
            command.success = True
            return
        command.success = False
        

    def deposit(self, command):
        self.balance += command.amount
        command.success = True
