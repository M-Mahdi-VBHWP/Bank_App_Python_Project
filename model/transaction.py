from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.transaction_type = ""
        self.amount = amount
        self.created_at = datetime.now()
        self.account_number = ""
        self.to_account_number = ""

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        if not isinstance(amount, (int, float)) or not 0 < amount < float("inf"):
            raise ValueError("Amount Invalid !!!")
        self.__amount = amount

    def deposit(self, account):
        account.deposit(self.amount)
        account.transactions.append(self.transaction_id)
        self.transaction_type = "deposit"
        self.account_number = account.account_number

    def withdraw(self, account):
        account.withdraw(self.amount)
        account.transactions.append(self.transaction_id)
        self.transaction_type = "withdraw"
        self.account_number = account.account_number

    def transfer(self, src, dst):
        if src.account_number == dst.account_number:
            raise ValueError("Source and Destination are the same !!!")

        src.withdraw(self.amount)
        try:
            dst.deposit(self.amount)
        except ValueError:
            src.deposit(self.amount)  # rollback
            raise

        src.transactions.append(self.transaction_id)
        dst.transactions.append(self.transaction_id)
        self.transaction_type = "transfer"
        self.account_number = src.account_number
        self.to_account_number = dst.account_number

    def from_tuple(self, transaction_tuple):
        self.transaction_id, self.transaction_type, amount, created_at, self.account_number, self.to_account_number = transaction_tuple
        self.amount = float(amount)
        self.created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")

    def to_tuple(self):
        return (self.transaction_id, self.transaction_type, f"{self.amount:.2f}", self.created_at.strftime("%Y-%m-%d %H:%M:%S"), self.account_number, self.to_account_number)

    amount = property(get_amount, set_amount)

    def __repr__(self):
        return f"Transaction(transaction_id={self.transaction_id}, transaction_type={self.transaction_type}, amount={self.amount:.2f}, created_at={self.created_at:%Y-%m-%d %H:%M:%S}, account_number={self.account_number}, to_account_number={self.to_account_number})"
