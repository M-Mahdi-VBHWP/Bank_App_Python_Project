from service.transaction_service import TransactionService


class TransactionController:
    def __init__(self):
        self.__service = TransactionService()

    def deposit(self, account_number, amount):
        try:
            amount = self.__to_amount(amount)
            transaction = self.__service.deposit(account_number, amount)
            return True, f"Info : {transaction} Deposited"
        except Exception as e:
            return False, f"Error : {e}"

    def withdraw(self, account_number, amount):
        try:
            amount = self.__to_amount(amount)
            transaction = self.__service.withdraw(account_number, amount)
            return True, f"Info : {transaction} Withdrawn"
        except Exception as e:
            return False, f"Error : {e}"

    def transfer(self, src_number, dst_number, amount):
        try:
            amount = self.__to_amount(amount)
            transaction = self.__service.transfer(src_number, dst_number, amount)
            return True, f"Info : {transaction} Transferred"
        except Exception as e:
            return False, f"Error : {e}"

    def get_by_type(self, types):
        try:
            transactions = self.__service.get_by_type(types)
            return True, transactions
        except Exception as e:
            return False, f"Error : {e}"

    def __to_amount(self, amount):
        if amount.strip() == "":
            raise ValueError("Amount is Required !!!")
        try:
            return float(amount)
        except ValueError:
            raise ValueError("Amount Invalid !!!")
