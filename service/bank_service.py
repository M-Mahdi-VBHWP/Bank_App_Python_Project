from data_access.bank_data_access import BankDataAccess
from model.bank import Bank


class BankService:
    def __init__(self):
        self.__data_access = BankDataAccess()

    def get_bank(self):
        bank_list = self.__data_access.get_all()
        if bank_list:
            return bank_list[0]

        bank = Bank("B1", "My Bank", "Tehran", "02100000000")
        self.__data_access.save(bank)
        return bank

    def add_branch(self, branch):
        bank = self.get_bank()
        bank.add_branch(branch)
        self.__data_access.edit(bank)
