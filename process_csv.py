from dataclasses import dataclass

from typing import Tuple, List
import csv


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

# user1 = User(first_name='Jana', last_name='Jahodová', phone_number='12345678')
# user2 = User(first_name='Šárka', last_name='Šarlotová', phone_number='12345678')
# user1.__eq__(user2)

def process_csv(path: str) -> Tuple[List[User], List[str]]:
    # TODO finish this function
    with open ("./users.csv", newline='') as users_file:
        csv_reader_object = csv.reader(users_file)
        users_list = []
        list_of_string = []
        for count, row in enumerate(csv_reader_object, -1):
            if csv_reader_object.line_num == 1:
                continue
            else:
                first_name = row[0]     #1. hodnota řádku
                last_name = row[1]
                phone_number = row[2]
                field_name = []
                if not first_name.isalpha():
                    field_name.append("invalid first name")

                if not last_name.isalpha():
                    field_name.append("invalid last name")

                if not phone_number.isdigit():
                    field_name.append("invalid phone number")

                if first_name.isalpha() and last_name.isalpha() and phone_number.isdigit():
                    user = User(first_name=first_name, last_name=last_name, phone_number=phone_number)
                    users_list.append(user)
                else:
                    error = ', '.join(field_name)
                    list_of_string.append(f'[ERROR - row {count}] {error}')

    return tuple((users_list, list_of_string))  #double round brackets


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
# Phone number can contain only numbers - string, ve kterém budou jenom čísla
# Errors should be returned as list of strings in format
# (one string for each invalid row)
# [ERROR - row {row_number}] invalid {field name}, invalid {field name}, ....
# You are allowed manipulate everything but function is_correct
# You can check if your solution is correct
# by executing `python process_csv.py`.

