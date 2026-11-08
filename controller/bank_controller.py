from service.bank_service import BankService


class BankController:
    def __init__(self):
        self.__service = BankService()

    def get_info(self):
        try:
            bank = self.__service.get_bank()
            return True, bank
        except Exception as e:
            return False, f"Error : {e}"
