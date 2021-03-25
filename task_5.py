class Stationery:
    def __init__(self, title="Pen, Pencil, Marker"):
        self.title = title

    def default_draw(self):
        print(f"Draw with {self.title}")


class Pen(Stationery):
    def default_draw(self):
        print(f"Draw with {self.title}")


class Pencil(Stationery):
    def default_draw(self):
        print(f"Draw with {self.title}")


class Marker(Stationery):
    def default_draw(self):
        print(f"Draw with {self.title}")


pen_draw = Pen("Pierre Cardin")
pen_draw.default_draw()

pencil_draw = Pencil("Kooh-i-Noor")
pencil_draw.default_draw()

mark_draw = Marker("TOUCH")
mark_draw.default_draw()