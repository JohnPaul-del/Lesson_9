from tkinter import *


class TrafficLight:
    def __init__(self):
        self.__color = ["#FF0000", "#FFFF00", "#00FF00"]
        self.status = 0
        window = Tk()
        window.title = "Traffic Light"
        self.canvas = Canvas(window, width=200, height=600, bg="black")
        self.red_circle = self.canvas.create_oval([0, 0], [200, 200], fill="#580000")
        self.yellow_circle = self.canvas.create_oval([0, 200], [200, 400], fill="#6E6E00")
        self.green_circle = self.canvas.create_oval([0, 400], [200, 600], fill="#075800")
        self.canvas.pack()
        self.canvas.update()
        self.canvas.after(30, self.start_traffic_light)

    def start_traffic_light(self):
        if self.status == 0:
            self.status = 1
            self.canvas.itemconfigure(self.red_circle, fill=self.__color[0])
            self.canvas.itemconfigure(self.yellow_circle, fill="#6E6E00")
            self.canvas.itemconfigure(self.green_circle, fill="#075800")
            self.canvas.after(7000, self.start_traffic_light)
        elif self.status == 1:
            self.status = 2
            self.canvas.itemconfigure(self.red_circle, fill="#580000")
            self.canvas.itemconfigure(self.yellow_circle, fill=self.__color[1])
            self.canvas.after(2000, self.start_traffic_light)
        elif self.status == 2:
            self.status = 3
            self.canvas.itemconfigure(self.yellow_circle, fill="#6E6E00")
            self.canvas.itemconfigure(self.green_circle, fill=self.__color[2])
            self.canvas.after(3000, self.start_traffic_light)
        else:
            self.status = 0
            self.canvas.itemconfigure(self.red_circle, fill="#580000")
            self.canvas.itemconfigure(self.yellow_circle, fill=self.__color[1])
            self.canvas.itemconfigure(self.green_circle, fill="#075800")
            self.canvas.after(2000, self.start_traffic_light)


traf_l = TrafficLight()
traf_l.canvas.mainloop()
