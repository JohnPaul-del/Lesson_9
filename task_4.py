import random

class Car:
    def __init__(self):
        color_list = ("red", "green", "blue", "white", "black")
        self.speed = random.randint(1, 120)
        self.color = random.choice(color_list)
        self.name = input("Enter car model: ")
        self.ispolice = True

    def car_motion_go(self):
        print(f"{self.name} {self.color} is drive with {self.speed} m/h")

    def car_motion_left(self):
        print(f"{self.name} {self.color} turn to the left")

    def car_motion_right(self):
        print(f"{self.name} {self.color} turn to the right")

    def car_motion_stop(self):
        print(f"{self.name} {self.color} car has been stopping")


class TownCar(Car):
    def car_motion_go(self):
        if self.speed > 60:
            print(f"{self.name} {self.color} is moving at an overspeed. This is Town Car")


class WorkCar(Car):
    super().car_motion_left()

    def car_motion_go(self):
        if self.speed > 20:
            print(f"{self.name} {self.color} is moving at an overspeed. This is Work Car")


class PoliceCar(Car):
   if super(Car).ispolice() is True:
       super(Car).name = f" {super(Car).name} (police car)"


car1 = PoliceCar()
car1.car_motion_go()
car1.car_motion_left()
car1.car_motion_right()
car1.car_motion_stop()
car1.police_car_color()
