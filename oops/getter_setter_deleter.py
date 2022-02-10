class Employee:

    # class variable
    raise_percent = 4
    total_employees = 0

    def __init__(self, first_name: str, last_name: str, pay: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.total_employees += 1

    def apply_raise(self) -> None:
        self.pay = self.pay + ((self.pay*self.raise_percent)/100)

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # getter (can also be a function)
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # getter
    @property
    def email(self) -> str:
        return f"{self.first_name}.{self.last_name}@email.com"

    # setter
    @full_name.setter
    def full_name(self, full_name) -> None:
        self.first_name, self.last_name = full_name.split(" ")

    # deleter
    @full_name.deleter
    def full_name(self) -> None:
        print("fullname deleted")
        self.first_name = None
        self.last_name = None

    def __repr__(self) -> str:
        return f"Employee('{self.first_name}', '{self.last_name}', '{self.pay}')"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} with email '{self.email}' gets ${self.pay} PA."


if __name__ == '__main__':

    emp = Employee('Pragyanshu', 'Rai', 100000)

    print(emp.__repr__())
    print(emp)
    emp.full_name = "Shipra Rai"
    print(emp.email)
    print(emp.full_name)
    print(emp)
    del emp.full_name
    print(emp)
