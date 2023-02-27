import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Tire Services")

# Set the window size
root.geometry("300x150")

# Create a label widget to display some text
title_label = tk.Label(root, text="Select a tire service:")

# Create three button widgets
tire_replacement_button = tk.Button(root, text="Tire Replacement")
tire_rotation_button = tk.Button(root, text="Tire Rotation")
estimate_calculator_button = tk.Button(root, text="Estimate Calculator")

# Pack the label and buttons into the window
title_label.pack(pady=10)
tire_replacement_button.pack(pady=5)
tire_rotation_button.pack(pady=5)
estimate_calculator_button.pack(pady=5)
# Start the main event loop
root.mainloop()

