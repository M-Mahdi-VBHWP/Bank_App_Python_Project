import os
import pickle


class BankDataAccess:
    def __init__(self):
        self.file_name = "banks.dat"
        self.__bank_list = self.get_all()

    def save(self, bank):
        self.get_all()
        self.__bank_list.append(bank)
        file = open(self.file_name, "wb")
        pickle.dump(self.__bank_list, file)
        file.close()

    def edit(self, bank):
        self.get_all()
        for index, item in enumerate(self.__bank_list):
            if item.bank_id == bank.bank_id:
                self.__bank_list[index] = bank
                file = open(self.file_name, "wb")
                pickle.dump(self.__bank_list, file)
                file.close()
                return
        raise ValueError("Bank Not Found !!!")

    def get_all(self):
        # todo : raise exception !!!
        if os.path.exists(self.file_name):
            file = open(self.file_name, "rb")
            self.__bank_list = pickle.load(file)
            file.close()
        else:
            self.__bank_list = []
        return self.__bank_list.copy()
