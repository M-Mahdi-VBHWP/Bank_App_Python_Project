import os
import pickle


class AccountDataAccess:
    def __init__(self):
        self.file_name = "accounts.dat"
        self.__account_list = self.get_all()

    def save(self, account):
        self.get_all()
        self.__account_list.append(account)
        file = open(self.file_name, "wb")
        pickle.dump(self.__account_list, file)
        file.close()

    def edit(self, account):
        self.get_all()
        for index, item in enumerate(self.__account_list):
            if item.account_id == account.account_id:
                self.__account_list[index] = account
                file = open(self.file_name, "wb")
                pickle.dump(self.__account_list, file)
                file.close()
                return
        raise ValueError("Account Not Found !!!")

    def get_all(self):
        # todo : raise exception !!!
        if os.path.exists(self.file_name):
            file = open(self.file_name, "rb")
            self.__account_list = pickle.load(file)
            file.close()
        else:
            self.__account_list = []
        return self.__account_list.copy()

    def get_by_number(self, account_number):
        return [item for item in self.get_all() if account_number in item.account_number]
