class Branch:
    def __init__(self, branch_id, name, address, phone, city):
        self.branch_id = branch_id
        self.name = name
        self.address = address
        self.phone = phone
        self.city = city
        self.accounts = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not isinstance(name, str) or not name.strip() or not all(ch.isalpha() or ch.isspace() for ch in name):
            raise ValueError("Name Invalid !!! (only letters)")
        self.__name = name

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if not isinstance(phone, str) or not phone.isdigit() or len(phone) < 8:
            raise ValueError("Phone Invalid !!!")
        self.__phone = phone

    def add_account(self, account):
        if account.account_number in self.accounts:
            raise ValueError("Account Number is Duplicated !!!")
        self.accounts.append(account.account_number)

    def from_tuple(self, branch_tuple):
        self.branch_id, self.name, self.address, self.phone, self.city = branch_tuple

    def to_tuple(self):
        return (self.branch_id, self.name, self.address, self.phone, self.city)

    name = property(get_name, set_name)
    phone = property(get_phone, set_phone)

    def __repr__(self):
        return f"Branch(branch_id={self.branch_id}, name={self.name}, address={self.address}, phone={self.phone}, city={self.city})"
