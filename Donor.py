class Donor:
    def __init__(self,first_name, last_name, age, email, contact_phone,blood_type, allergens):
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age 
        self.email = email 
        self.contact_phone = contact_phone 
        self.blood_type = blood_type 
        self.allergens = allergens 
        self.is_elligible = determine_elgibility(age, allergens)


    def set_eligible(self, eligibility):
        self.is_elligible = eligibility

def determine_elgibility(age, allergens):
    return True if age < 75 and allergens == "NA" else False