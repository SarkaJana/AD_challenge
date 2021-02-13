from dataclasses import dataclass

from typing import Tuple, List


@dataclass
class User:
    """
    Represent user in system
    """
    first_name: str
    last_name: str
    phone_number: str

    def __eq__(self, other: "User"):
        if not isinstance(other, User):
            return False
        return other.first_name == self.first_name and \
               other.last_name == self.last_name and \
               other.phone_number == self.phone_number

    def __str__(self):
        return f"[USER] {self.first_name} " \
               f"{self.last_name} - {self.phone_number}"


def process_csv(path: str) -> Tuple[List[User], List[str]]:
    # TODO finish this function
    pass


def is_correct(users: [User], errors: [str]):
    assert users[0] == User("John", "Doe", "777777777")
    assert users[1] == User("Foo", "Bar", "123456789")
    assert users[2] == User("Jane", "Doe", "888888888")
    assert users[3] == User("Bar", "Foo", "123456789")
    assert users[4] == User("Jason", "Doe", "999999999")

    assert errors[0] == "[ERROR - row 2] invalid first name, invalid last name"
    assert errors[1] == "[ERROR - row 5] invalid phone number"

    return True


users, errors = process_csv("users.csv")

if is_correct(users, errors):
    print("This solution is correct")

# The goal is to finish process_csv function to return valid User classes
# from CSV with valid data and a list of errors.
# with valid data and list of errors.
# Users should be returned as list of instances of User class
# Validation rules are simple:
# First and last name can contain only alphabet letter
# Phone number can contain only numbers
# Errors should be returned as list of strings in format
# (one string for each invalid row)
# [ERROR - row {row_number}] invalid {field name}, invalid {field name}, ....
# You are allowed manipulate everything but function is_correct
# You can check if your solution is correct
# by executing `python process_csv.py`.

