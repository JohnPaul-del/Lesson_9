class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def data_of_worker(self):
        return f'{self.name} {self.surname}'

    def income_of_worker(self):
        return f'{sum(self._income.values())}'


w_name = input("Enter the name: ")
w_surname = input("Enter the surname: ")
w_position = input("Enter the position: ")
w_wage = int(input("Enter the wage: "))
w_bonus = int(input("Enter the bonus: "))
worker1 = Position(w_name, w_surname, w_position, w_wage, w_bonus)
print(f"{worker1.data_of_worker()} has a ${worker1.income_of_worker()} on {worker1.position} position")
