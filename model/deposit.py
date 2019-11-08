class Deposit:
    def __init__(self, blood_type, is_valid, expiry_date, amount):
        self.blood_type = blood_type
        self.is_valid = is_valid
        self.expiry_date = expiry_date
        self.amount = amount

    def get_blood_type(self):
        return self.blood_type
    
    def get_amount(self):
        return self.amount

    # returns a nicely formatted string representation of a blood deposit when printed
    def __str__(self):
        return f'\nBlood Deposit\nID: {id(self)}\nAmount: {self.amount} mL\nType: {self.blood_type}\nValid: {self.is_valid}\nExpiry: {self.expiry_date}\n'

    def __eq__(self, other):
        if not isinstance(other, Deposit):
            return false
        return self.blood_type == other.blood_type and self.is_valid == other.is_valid and self.expiry_date == other.expiry_date and self.amount == other.amount