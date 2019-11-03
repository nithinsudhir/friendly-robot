class Blood:
    def __init__(self,type,is_valid, expiry_date, amount):
        self.type = type
        self.is_valid = is_valid
        self.expiry_date = expiry_date
        self.amount = amount

    def print_details(self):
        print(str(self.amount)+ "ml of blood type: "+ self.type + " with "+ str(self.is_valid)+ " validity, expiring on "+ self.expiry_date)

    def get_type(self):
        return self.type

    def get_amount(self):
        return self.amount