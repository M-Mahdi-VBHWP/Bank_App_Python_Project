from data_access.user_data_access import UserDataAccess


class UserService:
    def __init__(self):
        self.__data_access = UserDataAccess()

    def save(self, user):
        if not user.user_id.strip():
            raise ValueError("User Id is Required !!!")

        if self.__data_access.get_by_id(user.user_id) is not None:
            raise ValueError("User Id is Duplicated !!!")

        self.__check_national_code(user.user_id, user.national_code)
        self.__data_access.save(user)

    def edit(self, user_id, **data):
        user = self.__data_access.get_by_id(user_id)
        if user is None:
            raise ValueError("User Not Found !!!")

        if "national_code" in data:
            self.__check_national_code(user_id, data["national_code"])

        user.update_profile(**data)
        self.__data_access.edit(user)
        return user

    def delete(self, user_id):
        user = self.__data_access.get_by_id(user_id)
        if user is None:
            raise ValueError("User Not Found !!!")

        if user.accounts:
            raise ValueError("User has Accounts !!!")

        self.__data_access.delete(user_id)

    def login(self, user_id, password):
        user = self.__data_access.get_by_id(user_id)
        if user is None or not user.login(password):
            raise ValueError("User Id or Password is Wrong !!!")
        return user

    def get_all(self):
        return self.__data_access.get_all()

    def get_by_name(self, name):
        return self.__data_access.get_by_name(name)

    def __check_national_code(self, user_id, national_code):
        for item in self.__data_access.get_all():
            if item.user_id != user_id and item.national_code == national_code:
                raise ValueError("National Code is Duplicated !!!")
