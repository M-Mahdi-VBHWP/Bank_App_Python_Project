# import os
# import tempfile
#
# # run inside a temp folder, so the real .dat files are not touched
# os.chdir(tempfile.mkdtemp())

# =====================================
# bank models - PASSED
# =====================================
# from model.user import User
# from model.account import Account
# from model.transaction import Transaction
#
# user = User("U1", "0012345678", "Ali", "09120000000", "Tehran", "1234")
# print(user)
# print(user.to_tuple())
# print(user.login("1234"), user.login("0000"))
#
# account1 = Account("A1", "1001", 1000)
# account2 = Account("A2", "1002", 100)
# Transaction("T0001", 500).deposit(account1)
# Transaction("T0002", 300).transfer(account1, account2)
# print(account1, account2)
# print(account1.to_tuple())
# print(Transaction("T0003", 5).to_tuple())

# =====================================
# bank data access objects - PASSED
# =====================================
# from data_access.user_data_access import UserDataAccess
# from data_access.branch_data_access import BranchDataAccess
# from model.branch import Branch
#
# user_da = UserDataAccess()
# user_da.save(user)
# print(user_da.get_all())
#
# branch_da = BranchDataAccess()
# branch_da.save(Branch("BR1", "Central", "Main Street", "02112345678", "Tehran"))
# print(branch_da.get_all())

# =====================================
# bank business logic - PASSED
# =====================================
# from service.account_service import AccountService
# from service.transaction_service import TransactionService
#
# account_service = AccountService()
# account_service.save("U1", "BR1", Account("A10", "2001", 1000))
# account_service.save("U1", "BR1", Account("A11", "2002", 50))
#
# transaction_service = TransactionService()
# transaction_service.deposit("2001", 500)
# transaction_service.withdraw("2001", 100)
# transaction_service.transfer("2001", "2002", 200)
# print(account_service.get_all())
# print(transaction_service.get_by_type(("deposit", "withdraw")))
# print(transaction_service.get_by_type(("transfer",)))

# =====================================
# bank controllers - PASSED
# =====================================
# from controller.user_controller import UserController
# from controller.branch_controller import BranchController
# from controller.account_controller import AccountController
# from controller.transaction_controller import TransactionController
#
# user_controller = UserController()
# print(user_controller.save("U2", "0087654321", "Sara", "09130000000", "Shiraz", "abcd"))
# print(user_controller.login("U2", "abcd"))
# print(user_controller.edit("U2", "0087654321", "Sara Ahmadi", "09130000000", "Shiraz"))
# print(user_controller.delete("U2"))
# print(user_controller.save("U5", "0011223344", "12345", "09130000000", "Shiraz", "abcd"))   # error : name must be letters
# print(BranchController().save("BR9", "999", "Main Street", "02112345678", "Tehran"))        # error : name must be letters
#
# account_controller = AccountController()
# print(account_controller.save("U1", "BR1", "A20", "3001", "250"))
# print(account_controller.save("U1", "BR1", "A21", "3002", ""))      # error : amount is required
# print(account_controller.save("U1", "BR1", "A21", "3002", "abc"))   # error : amount invalid
# print(account_controller.save("U1", "BR1", "A21", "3002", "-5"))    # error : amount invalid
# print(account_controller.get_by_number("300"))
#
# transaction_controller = TransactionController()
# print(transaction_controller.deposit("2001", "100"))
# print(transaction_controller.transfer("2001", "2002", "50"))
# print(transaction_controller.transfer("2001", "2001", "50"))       # error : same account
# print(transaction_controller.withdraw("2001", "100"))
# print(transaction_controller.withdraw("2001", "999999"))           # error : insufficient balance
# print(transaction_controller.get_by_type(("deposit", "withdraw")))
# print(transaction_controller.get_by_type(("transfer",)))
# print(transaction_controller.deposit("9999", "10"))                # error : account not found
