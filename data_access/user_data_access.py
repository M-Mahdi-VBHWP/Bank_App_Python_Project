import os
import pickle


class UserDataAccess:
    def __init__(self):
        self.file_name = "users.dat"
        self.__user_list = self.get_all()

    def save(self, user):
        self.get_all()
        self.__user_list.append(user)
        file = open(self.file_name, "wb")
        pickle.dump(self.__user_list, file)
        file.close()

    def edit(self, user):
        self.get_all()
        for index, item in enumerate(self.__user_list):
            if item.user_id == user.user_id:
                self.__user_list[index] = user
                file = open(self.file_name, "wb")
                pickle.dump(self.__user_list, file)
                file.close()
                return
        raise ValueError("User Not Found !!!")

    def delete(self, user_id):
        self.get_all()
        self.__user_list = [item for item in self.__user_list if item.user_id != user_id]
        file = open(self.file_name, "wb")
        pickle.dump(self.__user_list, file)
        file.close()

    def get_all(self):
        # todo : raise exception !!!
        if os.path.exists(self.file_name):
            file = open(self.file_name, "rb")
            self.__user_list = pickle.load(file)
            file.close()
        else:
            self.__user_list = []
        return self.__user_list.copy()

    def get_by_id(self, user_id):
        for item in self.get_all():
            if item.user_id == user_id:
                return item
        return None

    def get_by_name(self, name):
        return [item for item in self.get_all() if name.lower() in item.name.lower()]
