class Employee:

    # class variable
    raise_percent = 4
    total_employees = 0

    def __init__(self, first_name: str, last_name: str, pay: float, email: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = email
        Employee.total_employees += 1

    def apply_raise(self) -> None:
        self.pay = self.pay + ((self.pay*self.raise_percent)/100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} with email '{self.email}' gets ${self.pay} PA."


if __name__ == '__main__':

    emp = Employee('Pragyanshu', 'Rai', 100000, 'pragyanshu@mail.com')

    print(emp)
    emp.apply_raise()
    print(emp)
    print(emp.__dict__ )
    print(Employee.total_employees)
