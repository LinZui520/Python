class Student:
    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Mobile: {self.mobile}"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Mobile: {self.mobile}"
