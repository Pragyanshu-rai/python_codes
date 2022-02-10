import datetime


class Employee:

    # class variable
    raise_percent: float = 4
    total_employees: int = 0

    def __init__(self, first_name: str, last_name: str, pay: float, email: str = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = float(pay)
        self.email = email if email is not None else f"{self.first_name}.{self.last_name}@email.com"
        Employee.total_employees += 1

    def apply_raise(self) -> None:
        self.pay = self.pay + ((self.pay*self.raise_percent)/100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} with email '{self.email}' gets ${self.pay} PA."

    @classmethod
    def set_raise_percent(cls, raise_percent: float) -> None:
        cls.raise_percent = raise_percent

    @classmethod
    def from_string(cls, employee_string: str, splitter: str = '-') -> object:
        return cls(*employee_string.split(splitter))

    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


if __name__ == '__main__':

    emp = Employee('Pragyanshu', 'Rai', 100000, 'pragyanshu@mail.com')
    emp_str = ["Shipra-Rai-100000", "Anish-Kumar-100000"]
    
    for string in emp_str:
        print(Employee.from_string(string))
    
    print(emp)
    print(emp.is_workday(datetime.date.today()))
