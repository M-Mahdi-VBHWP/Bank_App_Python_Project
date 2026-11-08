class Bank:
    def __init__(self, bank_id, name, address, phone):
        self.bank_id = bank_id
        self.name = name
        self.address = address
        self.phone = phone
        self.branches = []

    def add_branch(self, branch):
        if branch.branch_id in self.branches:
            raise ValueError("Branch Id is Duplicated !!!")
        self.branches.append(branch.branch_id)

    def from_tuple(self, bank_tuple):
        self.bank_id, self.name, self.address, self.phone = bank_tuple

    def to_tuple(self):
        return (self.bank_id, self.name, self.address, self.phone)

    def __repr__(self):
        return f"Bank(bank_id={self.bank_id}, name={self.name}, address={self.address}, phone={self.phone})"
