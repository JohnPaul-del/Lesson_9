import random


class Car:
    def __init__(self, ispolice=False):
        color_list = ("red", "green", "blue", "white", "black")
        model_list = ("Ford", "Dodge", "Plimouth", "Chevrolet", "GMC", "Shelby")
        self.speed = random.randint(1, 120)
        self.color = random.choice(color_list)
        self.name = random.choice(model_list)
        self.ispolice = ispolice

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
            print(f"{self.name} {self.color} is moving at an overspeed {self.speed}. This is Town Car")
        else:
            print(f"{self.name} {self.color} is drive with {self.speed} m/h")


class WorkCar(Car):
    def car_motion_go(self):
        if self.speed > 20:
            print(f"{self.name} {self.color} is moving at an overspeed {self.speed}. This is Work Car")
        else:
            print(f"{self.name} {self.color} is drive with {self.speed} m/h")


class PoliceCar(Car):
    def __init__(self, ispolice=True):
        super().__init__(ispolice)
        self.name = f" {self.name} *047* NYPD"


class SportCar(Car):
    pass


pd_car = PoliceCar()
pd_car.car_motion_go()
pd_car.car_motion_left()
pd_car.car_motion_right()
pd_car.car_motion_stop()
print("*"*50)
tw_car = TownCar()
tw_car.car_motion_go()
tw_car.car_motion_left()
tw_car.car_motion_right()
tw_car.car_motion_stop()
print("*"*50)
w_car = WorkCar()
w_car.car_motion_go()
w_car.car_motion_left()
w_car.car_motion_right()
w_car.car_motion_stop()
print("*"*50)
s_car = SportCar()
s_car.car_motion_go()
s_car.car_motion_left()
s_car.car_motion_right()
s_car.car_motion_stop()
