from data_access.account_data_access import AccountDataAccess
from data_access.branch_data_access import BranchDataAccess
from data_access.user_data_access import UserDataAccess


class AccountService:
    def __init__(self):
        self.__data_access = AccountDataAccess()
        self.__user_data_access = UserDataAccess()
        self.__branch_data_access = BranchDataAccess()

    def save(self, user_id, branch_id, account):
        if not account.account_id.strip() or not account.account_number.strip():
            raise ValueError("Account Id and Account Number are Required !!!")

        for item in self.__data_access.get_all():
            if item.account_id == account.account_id:
                raise ValueError("Account Id is Duplicated !!!")
            if item.account_number == account.account_number:
                raise ValueError("Account Number is Duplicated !!!")

        user = self.__user_data_access.get_by_id(user_id)
        if user is None:
            raise ValueError("User Not Found !!!")

        branch = self.__branch_data_access.get_by_id(branch_id)
        if branch is None:
            raise ValueError("Branch Not Found !!!")

        self.__data_access.save(account)

        branch.add_account(account)
        self.__branch_data_access.edit(branch)

        user.accounts.append(account.account_number)
        self.__user_data_access.edit(user)

    def get_all(self):
        return self.__data_access.get_all()

    def get_by_number(self, account_number):
        return self.__data_access.get_by_number(account_number)
