class getTen():

    number = None

    def __init__(self) -> None:
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.number <= 10:
            val = self.number
            self.number += 1
            return val

        else: 
            raise StopIteration

if __name__ == "__main__" :

    numbers = getTen()
    for num in numbers:
        print(num)