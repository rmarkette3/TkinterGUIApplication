import tkinter as tk
from tkinter import messagebox

class TireShopPOS:
    def __init__(self, master):
        self.master = master
        master.title("Tire Shop POS")
        self.total = 0
        self.labor_counter = 0

        # Load logo image and resize
        self.logo_image = tk.PhotoImage(file="tire_shop_logo.png")
        self.logo_image = self.logo_image.subsample(2)
        self.logo = tk.Label(master, image=self.logo_image)
        self.logo.pack()

        # Tire Replacement button
        self.tire_replacement_button = tk.Button(master, text="Tire Replacement", command=self.tire_replacement)
        self.tire_replacement_button.pack()

        # Tire Rotation button
        self.tire_rotation_button = tk.Button(master, text="Tire Rotation", command=self.tire_rotation)
        self.tire_rotation_button.pack()

        # Estimate Calculator button
        self.estimate_calculator_button = tk.Button(master, text="Estimate Calculator", command=self.estimate_calculator)
        self.estimate_calculator_button.pack()

        # Time Clock button
        self.time_clock_button = tk.Button(master, text="Time Clock", command=self.time_clock)
        self.time_clock_button.pack()

    def tire_replacement(self):
        self.total += 150
        self.labor_counter += 2

    def tire_rotation(self):
        self.total += 50
        self.labor_counter += 1

    def estimate_calculator(self):
        self.total += self.labor_counter * 50
        estimate = f"Total: ${self.total:.2f}"
        self.total = 0
        self.labor_counter = 0
        messagebox.showinfo("Estimate", estimate)

    def time_clock(self):
        clock_window = tk.Toplevel(self.master)
        clock_window.title("Time Clock")

        # Load clock image and resize
        self.clock_image = tk.PhotoImage(file="clock.png")
        self.clock_image = self.clock_image.subsample(2)
        self.clock_label = tk.Label(clock_window, image=self.clock_image)
        self.clock_label.pack(side="right")

        for i in range(10):
            button = tk.Button(clock_window, text=i, command=lambda i=i: print(i))
            button.pack()

root = tk.Tk()
pos = TireShopPOS(root)
root.mainloop()
