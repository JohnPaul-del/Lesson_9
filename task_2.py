class Road:
    def __init__(self):
        self._r_width = 0
        self._r_length = 0

    def calc_square(self):
        self._r_width = int(input("Enter the width in meter: "))
        self._r_length = int(input("Enter the length in meter: "))
        quantity = int(input("Enter the quantity in kilo: "))
        thickness = int(input("Enter the thickness in santimeter: "))
        res_square = self._r_width * self._r_length * quantity * thickness
        print(f"You need: {res_square / 1000} t")


calc_1 = Road()
calc_1.calc_square()
# calc_2 = Road()
# calc_2.calc_square()
