from datetime import date


class Account:
    def __init__(self, account_id, account_number, amount):
        self.account_id = account_id
        self.account_number = account_number
        self._balance = 0.0
        self.status = "active"
        self.open_date = date.today()
        self.transactions = []
        self.deposit(amount)  # the first balance must be a positive number

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self.check_amount(amount)
        self._balance += amount

    def withdraw(self, amount):
        self.check_amount(amount)
        if amount > self._balance:
            raise ValueError("Insufficient Balance !!!")
        self._balance -= amount

    def check_amount(self, amount):
        if not isinstance(amount, (int, float)) or not 0 < amount < float("inf"):
            raise ValueError("Amount Invalid !!!")
        if self.status != "active":
            raise ValueError("Account is not Active !!!")

    def from_tuple(self, account_tuple):
        self.account_id, self.account_number, balance, self.status, open_date = account_tuple
        self._balance = float(balance)
        self.open_date = date.fromisoformat(open_date)

    def to_tuple(self):
        return (self.account_id, self.account_number, f"{self.balance:.2f}", self.status, str(self.open_date))

    balance = property(get_balance)

    def __repr__(self):
        return f"Account(account_id={self.account_id}, account_number={self.account_number}, balance={self.balance:.2f}, status={self.status}, open_date={self.open_date})"
