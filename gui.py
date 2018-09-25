import random
import tkinter as tk

from boarding import Boarding
from boarding_process import RandomBoarding
from passenger import Passenger
from shapes import Rectangle


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.canvas_width = 2000
        self.canvas_height = 2000

        self.gui_varience = 200

        self.passenger_proxy = {}

        self.create_boarding()
        self.create_widgets()
        self.animation(20, 20)  # run animation
        print('infinite loop?')

    def animation(self, x_move, y_move):

        for p1 in self.b.passenger_list:
            p1_proxy, p1_luggage_proxy = self.passenger_proxy[p1]
            p1_coords = self.canvas.coords(p1_proxy)
            r1 = Rectangle(p1_coords)

            for p2 in self.b.passenger_list:
                p2_proxy, p2_luggage_proxy = self.passenger_proxy[p2]
                p2_coords = self.canvas.coords(p2_proxy)
                r2 = Rectangle(p2_coords)

                if p1_proxy != p2_proxy:
                    if r1 & r2:
                        # print(p1_proxy, p1_coords, 'intersects', p2_proxy, p2_coords)
                        x_move, y_move = self.move_directions(p2_coords)
                        self.canvas.move(p2_proxy, x_move, y_move)  # movement
                        self.canvas.move(p2_luggage_proxy, x_move, y_move)  # movement
                        self.canvas.update()

        # self.canvas.after(20)  # milliseconds in wait time, this is 50 fps
        self.master.after(20, self.animation, x_move, y_move)

    def create_widgets(self):
        root.option_add("*Font", "courier 20")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.canvas = tk.Canvas(root,
                                width=self.canvas_width,
                                height=self.canvas_height,
                                bg='yellow')

        # self.canvas.create_line(0, 0, 200, 100)
        # self.canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        # self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")

        for p in self.b.passenger_list:
            assert isinstance(p, Passenger)
            x_offset = random.randint(0, self.gui_varience)
            y_offset = random.randint(0, self.gui_varience)
            tk_rgb = "#%02x%02x%02x" % (
                random.randint(0, 254),
                random.randint(0, 254),
                random.randint(0, 254))

            passenger_rect = self.canvas.create_rectangle(
                250 + x_offset,
                500 + y_offset,
                250 + x_offset + 50,
                500 + y_offset + 50,
                fill=tk_rgb)

            luggage_list_rects = []
            if len(p.lugagge_list):
                passenger_luggage_rect = self.canvas.create_rectangle(
                    275 + x_offset,
                    525 + y_offset,
                    275 + x_offset + 50,
                    525 + y_offset + 25,
                    fill='blue')
                luggage_list_rects.append(passenger_luggage_rect)

            self.passenger_proxy[p] = passenger_rect, luggage_list_rects

        self.img = tk.PhotoImage(file="media/plane.ppm")
        self.img_id = self.canvas.create_image(1000, 100, image=self.img)
        self.canvas.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def create_boarding(self):
        self.b = Boarding()
        self.b.generate_passengers(100)
        self.b.print_description()

        self.b.boarding_process = RandomBoarding(self.b.plane, self.b.passenger_list)
        self.b.boarding_process.assign_seats()

        self.b.board()

    def move_directions(self, coords):
        x = random.randint(0, 40) - 20
        y = random.randint(0, 40) - 20

        if coords[3] + y > self.canvas_height:
            y *= -1
        if coords[2] + y < 0:
            y = 0

        if coords[2] + x > self.canvas_width:
            x *= -1
        if coords[1] + x < 0:
            x = 0

        return x, y


root = tk.Tk()
app = Application(master=root)
app.mainloop()