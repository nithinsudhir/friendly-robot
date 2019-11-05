from .user import User

class Donor(User):
    def __init__(self, first_name = None, last_name = None, age = 0, email = None, contact_phone = None, blood_type = None, allergens = None):
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age 
        self.email = email 
        self.contact_phone = contact_phone 
        self.blood_type = blood_type 
        self.allergens = allergens 
        self.is_elligible = determine_elgibility(self.age, self.allergens)
        self.user_type = 'Donor'

    def set_eligible(self, eligibility):
        self.is_elligible = eligibility

    # returns a nicely formatted string representation of a donor when printed
    def __str__(self):
        return f'\nBlood Donor\nID: {id(self)}\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nContact: {self.email}\nBlood Type: {self.blood_type}\nAllergens: {self.allergens}\nEligibility: {self.is_elligible}\n'

    def get_is_elligible():
        return self.is_elligible

    def get_user_type(self):
        return self.user_type

def determine_elgibility(age, allergens):
    return True if int(age) < int(75) and allergens == "N/A" else False
