from model.user import User
from service.user_service import UserService


class UserController:
    def __init__(self):
        self.__service = UserService()

    def save(self, user_id, national_code, name, phone, address, password):
        try:
            user = User(user_id, national_code, name, phone, address, password)
            self.__service.save(user)
            return True, f"Info : {user} Saved"
        except Exception as e:
            return False, f"Error : {e}"

    def edit(self, user_id, national_code, name, phone, address):
        try:
            user = self.__service.edit(user_id, national_code=national_code, name=name, phone=phone, address=address)
            return True, f"Info : {user} Edited"
        except Exception as e:
            return False, f"Error : {e}"

    def delete(self, user_id):
        try:
            self.__service.delete(user_id)
            return True, f"Info : {user_id} Deleted"
        except Exception as e:
            return False, f"Error : {e}"

    def login(self, user_id, password):
        try:
            user = self.__service.login(user_id, password)
            return True, f"Info : Welcome {user.name}"
        except Exception as e:
            return False, f"Error : {e}"

    def get_all(self):
        try:
            users = self.__service.get_all()
            return True, users
        except Exception as e:
            return False, f"Error : {e}"

    def get_by_name(self, name):
        try:
            users = self.__service.get_by_name(name)
            return True, users
        except Exception as e:
            return False, f"Error : {e}"
