import tkinter as tk
from PIL import Image, ImageTk  # For resizing the logo
import subprocess
import os
import sys

def open_projectile_visualizer():
    """Open the projectile motion visualizer and exit the homepage."""
    root.destroy()  # Close the homepage window
    try:
        # Run the projectile motion visualizer
        subprocess.run([sys.executable, os.path.join("src", "projectiles.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running projectile visualizer: {e}")
    finally:
        # Exit the entire application after the visualizer is closed
        sys.exit()

# Create the homepage window
root = tk.Tk()
root.title("Visumatic")
root.geometry("600x400")
root.configure(bg="#040444")  # Dark background color

# Load and resize the logo
try:
    logo_path = os.path.join("src", "logo.png")  # Ensure the logo is placed in the src/ folder
    original_logo = Image.open(logo_path)
    resized_logo = original_logo.resize((325, 244), Image.Resampling.LANCZOS)  # High-quality resize
    logo = ImageTk.PhotoImage(resized_logo)
    logo_label = tk.Label(root, image=logo, bg="#282c34")
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

# Add a button to navigate to the projectile visualizer
button = tk.Button(
    root, 
    text="Projectile Motion", 
    font=("Helvetica", 16), 
    fg="black", 
    bg="#61afef", 
    activebackground="#528aa5", 
    activeforeground="white", 
    command=open_projectile_visualizer
)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
