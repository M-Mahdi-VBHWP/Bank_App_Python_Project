from model.branch import Branch
from service.branch_service import BranchService


class BranchController:
    def __init__(self):
        self.__service = BranchService()

    def save(self, branch_id, name, address, phone, city):
        try:
            branch = Branch(branch_id, name, address, phone, city)
            self.__service.save(branch)
            return True, f"Info : {branch} Saved"
        except Exception as e:
            return False, f"Error : {e}"

    def edit(self, branch_id, name, address, phone, city):
        try:
            branch = Branch(branch_id, name, address, phone, city)
            self.__service.edit(branch)
            return True, f"Info : {branch} Edited"
        except Exception as e:
            return False, f"Error : {e}"

    def get_all(self):
        try:
            branches = self.__service.get_all()
            return True, branches
        except Exception as e:
            return False, f"Error : {e}"

    def get_by_name(self, name):
        try:
            branches = self.__service.get_by_name(name)
            return True, branches
        except Exception as e:
            return False, f"Error : {e}"
