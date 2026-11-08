import os
import pickle


class BranchDataAccess:
    def __init__(self):
        self.file_name = "branches.dat"
        self.__branch_list = self.get_all()

    def save(self, branch):
        self.get_all()
        self.__branch_list.append(branch)
        file = open(self.file_name, "wb")
        pickle.dump(self.__branch_list, file)
        file.close()

    def edit(self, branch):
        self.get_all()
        for index, item in enumerate(self.__branch_list):
            if item.branch_id == branch.branch_id:
                self.__branch_list[index] = branch
                file = open(self.file_name, "wb")
                pickle.dump(self.__branch_list, file)
                file.close()
                return
        raise ValueError("Branch Not Found !!!")

    def get_all(self):
        # todo : raise exception !!!
        if os.path.exists(self.file_name):
            file = open(self.file_name, "rb")
            self.__branch_list = pickle.load(file)
            file.close()
        else:
            self.__branch_list = []
        return self.__branch_list.copy()

    def get_by_id(self, branch_id):
        for item in self.get_all():
            if item.branch_id == branch_id:
                return item
        return None

    def get_by_name(self, name):
        return [item for item in self.get_all() if name.lower() in item.name.lower()]
