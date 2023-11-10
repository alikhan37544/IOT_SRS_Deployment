import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Smart Lighting System")

# Initial light status (off)
light_status = False

# Function to toggle light status
def toggle_light():
    global light_status
    light_status = not light_status
    update_light_label()

# Function to update light label text
def update_light_label():
    if light_status:
        light_label.config(text="Lights: ON", fg="green")
    else:
        light_label.config(text="Lights: OFF", fg="red")

# Create light control button
light_button = tk.Button(root, text="Toggle Lights", command=toggle_light, height=2, width=20)
light_button.pack(pady=20)

# Create label to display light status
light_label = tk.Label(root, text="Lights: OFF", font=("Arial", 18))
light_label.pack()

# Run the tkinter main loop
root.mainloop()
