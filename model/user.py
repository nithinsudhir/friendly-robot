from abc import ABC, abstractmethod

class User(ABC):

    def get_type(self):
        return self.__class__.__name__
    
    def add_deposit(self):
        print(f"{self.__class__.__name__}'s cannot add deposits")

    def remove_deposit(self):
        print(f"{self.__class__.__name__}'s cannot remove deposits")

    def add_donor(self):
        print(f"{self.__class__.__name__}'s cannot add donors")

    def remove_donor(self):
        print(f"{self.__class__.__name__}'s cannot remove donors")
    
    def request_blood(self):
        print(f"{self.__class__.__name__}'s cannot request blood")

    def count_deposits(self):
        print(f"{self.__class__.__name__}'s cannot count deposits")

    def count_volume(self):
        print(f"{self.__class__.__name__}'s cannot count volume")

    def filter_blood(self):
        print(f"{self.__class__.__name__}'s cannot filter blood")

    def warn_scarce_blood_types(self):
        pass

    def register(self):
        print(f"{self.__class__.__name__}'s cannot register as donors'")

    def donate_blood(self):
        print(f"{self.__class__.__name__}'s cannot donate blood'")

    @abstractmethod
    def print_instructions(self):
        pass