import tkinter as tk
from PIL import Image, ImageTk  # For resizing the logo
import subprocess
import os
import sys

def open_projectile_visualizer():
    """Open the projectile motion visualizer and return to the homepage after it closes."""
    root.withdraw()  # Hide the homepage window
    try:
        # Run the projectile motion visualizer
        subprocess.run([sys.executable, os.path.join("src", "projectiles.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running projectile visualizer: {e}")
    finally:
        # Show the homepage window again after the visualizer closes
        root.deiconify()

def open_double_pendulum_visualizer():
    """Open the double pendulum visualizer and return to the homepage after it closes."""
    root.withdraw()  # Hide the homepage window
    try:
        # Run the double pendulum visualizer
        subprocess.run([sys.executable, os.path.join("src", "double_pendulum.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running double pendulum visualizer: {e}")
    finally:
        # Show the homepage window again after the visualizer closes
        root.deiconify()

def open_vectors_visualizer():
    """Open the vectors visualizer and return to the homepage after it closes."""
    root.withdraw()  # Hide the homepage window
    try:
        # Run the vectors visualizer
        subprocess.run([sys.executable, os.path.join("src", "vectors.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running vectors visualizer: {e}")
    finally:
        # Show the homepage window again after the visualizer closes
        root.deiconify()

# Create the homepage window
root = tk.Tk()
root.title("Visumatic")
root.geometry("700x500")
root.configure(bg="#040444")  # Dark background color

# Load and resize the logo
try:
    logo_path = os.path.join("src", "logo.png")  # Ensure the logo is placed in the src/ folder
    original_logo = Image.open(logo_path)
    resized_logo = original_logo.resize((325, 244), Image.Resampling.LANCZOS)  # High-quality resize
    logo = ImageTk.PhotoImage(resized_logo)
    logo_label = tk.Label(root, image=logo, bg="#040444")
    logo_label.pack(pady=20)
except Exception as e:
    print(f"Error loading or resizing logo: {e}")

# Add a label
label = tk.Label(
    root, 
    text="Welcome to Visumatic!", 
    font=("Helvetica", 20, "bold"), 
    fg="white", 
    bg="#040444"
)
label.pack(pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#040444")
button_frame.pack(pady=20)

# Add a button for the projectile motion visualizer
button = tk.Button(
    button_frame, 
    text="Projectile Motion", 
    font=("Helvetica", 16), 
    fg="black", 
    bg="white", 
    activebackground="black", 
    activeforeground="white", 
    command=open_projectile_visualizer
)
button.grid(row=0, column=0, padx=20, pady=10)

# Add a button for the double pendulum visualizer
double_pendulum_button = tk.Button(
    button_frame, 
    text="Double Pendulum", 
    font=("Helvetica", 16), 
    fg="black", 
    bg="white", 
    activebackground="black", 
    activeforeground="white", 
    command=open_double_pendulum_visualizer
)
double_pendulum_button.grid(row=0, column=1, padx=20, pady=10)

# Add a button for the vectors visualizer
vectors_button = tk.Button(
    button_frame, 
    text="Vectors", 
    font=("Helvetica", 16), 
    fg="black", 
    bg="white", 
    activebackground="black", 
    activeforeground="white", 
    command=open_vectors_visualizer
)
vectors_button.grid(row=0, column=2, padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()
