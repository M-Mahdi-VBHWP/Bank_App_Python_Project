from model.account import Account
from service.account_service import AccountService


class AccountController:
    def __init__(self):
        self.__service = AccountService()

    def save(self, user_id, branch_id, account_id, account_number, amount):
        try:
            amount = self.__to_amount(amount)
            account = Account(account_id, account_number, amount)
            self.__service.save(user_id, branch_id, account)
            return True, f"Info : {account} Saved"
        except Exception as e:
            return False, f"Error : {e}"

    def get_all(self):
        try:
            accounts = self.__service.get_all()
            return True, accounts
        except Exception as e:
            return False, f"Error : {e}"

    def get_by_number(self, account_number):
        try:
            accounts = self.__service.get_by_number(account_number)
            return True, accounts
        except Exception as e:
            return False, f"Error : {e}"

    def __to_amount(self, amount):
        if amount.strip() == "":
            raise ValueError("Amount is Required !!!")
        try:
            return float(amount)
        except ValueError:
            raise ValueError("Amount Invalid !!!")
