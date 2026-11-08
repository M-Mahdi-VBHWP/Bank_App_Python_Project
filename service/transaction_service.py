from data_access.account_data_access import AccountDataAccess
from data_access.transaction_data_access import TransactionDataAccess
from model.transaction import Transaction


class TransactionService:
    def __init__(self):
        self.__data_access = TransactionDataAccess()
        self.__account_data_access = AccountDataAccess()

    def deposit(self, account_number, amount):
        account = self.__get_account(account_number)
        transaction = Transaction(self.__next_id(), amount)

        transaction.deposit(account)
        self.__account_data_access.edit(account)
        self.__data_access.save(transaction)
        return transaction

    def withdraw(self, account_number, amount):
        account = self.__get_account(account_number)
        transaction = Transaction(self.__next_id(), amount)

        transaction.withdraw(account)
        self.__account_data_access.edit(account)
        self.__data_access.save(transaction)
        return transaction

    def transfer(self, src_number, dst_number, amount):
        src = self.__get_account(src_number)
        dst = self.__get_account(dst_number)
        transaction = Transaction(self.__next_id(), amount)

        transaction.transfer(src, dst)
        self.__account_data_access.edit(src)
        self.__account_data_access.edit(dst)
        self.__data_access.save(transaction)
        return transaction

    def get_by_type(self, types):
        return self.__data_access.get_by_type(types)

    def __get_account(self, account_number):
        for account in self.__account_data_access.get_all():
            if account.account_number == account_number:
                return account
        raise ValueError(f"Account {account_number} Not Found !!!")

    def __next_id(self):
        return f"T{len(self.__data_access.get_all()) + 1:04d}"
