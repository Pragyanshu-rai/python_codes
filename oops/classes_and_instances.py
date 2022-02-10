class Employee:

    def __init__(self, first_name: str, last_name: str, pay: float, email: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = email
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} with email '{self.email}' gets ${self.pay} PA."


if __name__ == '__main__':

    emp = Employee('Pragyanshu', 'Rai', 100000, 'pragyanshu@mail.com')

    print(emp)
