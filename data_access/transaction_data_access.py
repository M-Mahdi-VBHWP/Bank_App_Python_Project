import os
import pickle


class TransactionDataAccess:
    def __init__(self):
        self.file_name = "transactions.dat"
        self.__transaction_list = self.get_all()

    def save(self, transaction):
        self.get_all()
        self.__transaction_list.append(transaction)
        file = open(self.file_name, "wb")
        pickle.dump(self.__transaction_list, file)
        file.close()

    def get_all(self):
        # todo : raise exception !!!
        if os.path.exists(self.file_name):
            file = open(self.file_name, "rb")
            self.__transaction_list = pickle.load(file)
            file.close()
        else:
            self.__transaction_list = []
        return self.__transaction_list.copy()

    def get_by_type(self, types):
        return [item for item in self.get_all() if item.transaction_type in types]
