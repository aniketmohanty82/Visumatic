import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def vector_addition_visualizer():
    """Run the vector addition visualizer."""
    # Function to add and display the resultant vector
    def add_vectors():
        try:
            # Get input values for vectors
            v1_i = float(vector1_i_entry.get())
            v1_j = float(vector1_j_entry.get())
            v1_k = float(vector1_k_entry.get())
            v2_i = float(vector2_i_entry.get())
            v2_j = float(vector2_j_entry.get())
            v2_k = float(vector2_k_entry.get())

            # Compute the resultant vector
            resultant_i = v1_i + v2_i
            resultant_j = v1_j + v2_j
            resultant_k = v1_k + v2_k

            # Compute the magnitude of the resultant vector
            magnitude = np.sqrt(resultant_i**2 + resultant_j**2 + resultant_k**2)

            # Update the result label
            result_label.config(
                text=f"Resultant Vector: {resultant_i:.2f}i, {resultant_j:.2f}j, {resultant_k:.2f}k\nMagnitude: {magnitude:.2f}"
            )

            # Plot the vectors in 3D
            plot_vectors(
                [v1_i, v1_j, v1_k],
                [v2_i, v2_j, v2_k],
                [resultant_i, resultant_j, resultant_k]
            )

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for the vector components.")
            
            
    # Function to subtract and display the resultant vector
    def subtract_vectors():
        try:
            # Get input values for vectors
            v1_i = float(vector1_i_entry.get())
            v1_j = float(vector1_j_entry.get())
            v1_k = float(vector1_k_entry.get())
            v2_i = float(vector2_i_entry.get())
            v2_j = float(vector2_j_entry.get())
            v2_k = float(vector2_k_entry.get())

            # Compute the resultant vector
            resultant_i = v1_i - v2_i
            resultant_j = v1_j - v2_j
            resultant_k = v1_k - v2_k

            # Compute the magnitude of the resultant vector
            magnitude = np.sqrt(resultant_i**2 + resultant_j**2 + resultant_k**2)

            # Update the result label
            result_label.config(
                text=f"Resultant Vector: {resultant_i:.2f}i, {resultant_j:.2f}j, {resultant_k:.2f}k\nMagnitude: {magnitude:.2f}"
            )

            # Plot the vectors in 3D
            plot_vectors(
                [v1_i, v1_j, v1_k],
                [v2_i, v2_j, v2_k],
                [resultant_i, resultant_j, resultant_k]
            )

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for the vector components.")

    # Function to plot vectors in 3D
    def plot_vectors(v1, v2, resultant):
        ax.clear()
        ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color="blue", label="Vector 1", arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color="green", label="Vector 2", arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, resultant[0], resultant[1], resultant[2], color="red", label="Resultant", arrow_length_ratio=0.1)

        # Set plot limits
        max_limit = max(
            abs(v1[0] + v2[0]), abs(v1[1] + v2[1]), abs(v1[2] + v2[2]), 1
        )
        ax.set_xlim([-max_limit, max_limit])
        ax.set_ylim([-max_limit, max_limit])
        ax.set_zlim([-max_limit, max_limit])
        
        ax.plot([-max_limit, max_limit], [0, 0], [0, 0], color="black", linestyle="--")  # X-axis
        ax.plot([0, 0], [-max_limit, max_limit], [0, 0], color="black", linestyle="--")  # Y-axis
        ax.plot([0, 0], [0, 0], [-max_limit, max_limit], color="black", linestyle="--")  # Z-axis

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.legend()
        canvas.draw()

    # Create the Tkinter window
    root = tk.Tk()
    root.title("3D Vector Addition")
    root.geometry("900x600")

    # Create a frame for the 3D graph
    graph_frame = tk.Frame(root, bg="#ffffff")
    graph_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a matplotlib figure for 3D plotting
    fig = Figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111, projection="3d")

    # Add the figure to the Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Input frame for vector components and results
    input_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
    input_frame.pack(side=tk.RIGHT, fill=tk.Y)

    tk.Label(input_frame, text="Vector 1 (i, j, k):", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg = "black").pack(pady=10)
    vector1_i_entry = tk.Entry(input_frame, width=10, bg="#f0f0f0", fg="black")
    vector1_i_entry.pack(pady=5)
    vector1_j_entry = tk.Entry(input_frame, width=10, bg="#f0f0f0", fg="black")
    vector1_j_entry.pack(pady=5)
    vector1_k_entry = tk.Entry(input_frame, width=10, bg="#f0f0f0", fg="black")
    vector1_k_entry.pack(pady=5)

    tk.Label(input_frame, text="Vector 2 (i, j, k):", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="black").pack(pady=10)
    vector2_i_entry = tk.Entry(input_frame, width=10, bg="#f0f0f0", fg="black")
    vector2_i_entry.pack(pady=5)
    vector2_j_entry = tk.Entry(input_frame, width=10, bg="#f0f0f0", fg="black")
    vector2_j_entry.pack(pady=5)
    vector2_k_entry = tk.Entry(input_frame, width=10, bg="#f0f0f0", fg="black")
    vector2_k_entry.pack(pady=5)

    add_button = tk.Button(input_frame, text="Add", command=add_vectors, bg="white", fg="black", font=("Helvetica", 12, "bold"))
    add_button.pack(pady=20)

    subtract_button = tk.Button(input_frame, text="Subtract", command=subtract_vectors, bg="white", fg="black", font=("Helvetica", 12, "bold"))
    subtract_button.pack(pady=20)
    
    result_label = tk.Label(input_frame, text="Resultant Vector: \nMagnitude: ", font=("Helvetica", 12), fg="black", bg="#f0f0f0")
    result_label.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    vector_addition_visualizer()
