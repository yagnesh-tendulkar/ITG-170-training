# class BankAccount:
#     def __init__(self, owner, bal):
#         self.owner = owner
#         self.__balance = bal

#     @property
#     def  balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self,amount):
#         if amount < 0:
#             print("Denied action balance cannot be negative")
#         else:
#             self.__balance = amount
#             print("Action success, balance updated")
# user = BankAccount("emly", 500)
# user.balance = 1000
# user.balance = -50
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance  # Private attribute

    @property
    def balance(self):
        """Getter: Allows viewing but hides the raw variable."""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter: Adds validation logic b efore changing data."""
        if amount < 0:
            print("Action Denied: Balance cannot be negative.")
        else:
            self.__balance = amount
            print(f"Balance updated successfully.")

# Execution
user = BankAccount("John", 500)
user.balance = 1000   # Works via setter
user.balance = -50    # Blocked by validation logic
