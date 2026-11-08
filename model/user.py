import hashlib


class User:
    def __init__(self, user_id, national_code, name, phone, address, password):
        self.user_id = user_id
        self.national_code = national_code
        self.name = name
        self.phone = phone
        self.address = address
        self.password_hash = self.hash_password(password)
        self.accounts = []

    def hash_password(self, password):
        if not isinstance(password, str) or len(password) < 4:
            raise ValueError("Password Invalid !!!")
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not isinstance(name, str) or not name.strip() or not all(ch.isalpha() or ch.isspace() for ch in name):
            raise ValueError("Name Invalid !!! (only letters)")
        self.__name = name

    def get_national_code(self):
        return self.__national_code

    def set_national_code(self, national_code):
        if not isinstance(national_code, str) or not national_code.isdigit() or len(national_code) != 10:
            raise ValueError("National Code Invalid !!!")
        self.__national_code = national_code

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if not isinstance(phone, str) or not phone.isdigit() or len(phone) < 8:
            raise ValueError("Phone Invalid !!!")
        self.__phone = phone

    def login(self, password):
        return self.password_hash == self.hash_password(password)

    def update_profile(self, **data):
        for key, value in data.items():
            if key not in ("national_code", "name", "phone", "address"):
                raise ValueError(f"Field {key} can not be updated !!!")
            setattr(self, key, value)

    def from_tuple(self, user_tuple):
        self.user_id, self.national_code, self.name, self.phone, self.address = user_tuple

    def to_tuple(self):
        return (self.user_id, self.national_code, self.name, self.phone, self.address)

    name = property(get_name, set_name)
    national_code = property(get_national_code, set_national_code)
    phone = property(get_phone, set_phone)

    def __repr__(self):
        return f"User(user_id={self.user_id}, national_code={self.national_code}, name={self.name}, phone={self.phone}, address={self.address})"
