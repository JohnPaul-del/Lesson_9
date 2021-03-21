class Worker:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.position = ""
        self.__income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def data_of_worker(self):
        self.name = input("Enter the name: ")
        self.surname = input("Enter the surname: ")
        self.position = input("Enter the position: ")
        wage = input("Enter the wage: ")
        bonus = input("Enter the bonus: ")
        income = super().__income()
        income.update({"wage": wage, "bonus": bonus})
        for i in income.values():
            result += i
        print(f"{self.name} {self.surname} has a {result}")


worker1 = Position()
worker1.data_of_worker()