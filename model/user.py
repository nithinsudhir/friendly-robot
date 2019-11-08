from abc import ABC, abstractmethod

class User(ABC):

    def get_user_type(self):
        return self.user_type