from data_access.branch_data_access import BranchDataAccess
from service.bank_service import BankService


class BranchService:
    def __init__(self):
        self.__data_access = BranchDataAccess()
        self.__bank_service = BankService()

    def save(self, branch):
        if not branch.branch_id.strip():
            raise ValueError("Branch Id is Required !!!")

        if self.__data_access.get_by_id(branch.branch_id) is not None:
            raise ValueError("Branch Id is Duplicated !!!")

        self.__data_access.save(branch)
        self.__bank_service.add_branch(branch)

    def edit(self, branch):
        old_branch = self.__data_access.get_by_id(branch.branch_id)
        if old_branch is None:
            raise ValueError("Branch Not Found !!!")

        branch.accounts = old_branch.accounts
        self.__data_access.edit(branch)

    def get_all(self):
        return self.__data_access.get_all()

    def get_by_name(self, name):
        return self.__data_access.get_by_name(name)
