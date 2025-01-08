import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

def projectile_motion_visualizer():
    # Function to compute projectile motion
    def projectile_motion(v0, angle, v_z, y0, g=9.81, steps=500):
        theta = np.radians(angle)
        t_flight = (v0 * np.sin(theta) + np.sqrt((v0 * np.sin(theta))**2 + 2 * g * y0)) / g
        t = np.linspace(0, t_flight, steps)
        x = v0 * np.cos(theta) * t
        y = y0 + v0 * np.sin(theta) * t - 0.5 * g * t**2
        z = v_z * t
        return x, y, z, t

    # Function to create and update the animation
    def create_animation(v0, angle, v_z, y0, ax):
        x, y, z, t = projectile_motion(v0, angle, v_z, y0)

        # Recreate the 3D plot boundaries and labels
        ax.set_xlim(0, np.max(x) + 1)
        ax.set_ylim(0, np.max(z) + 1)
        ax.set_zlim(0, np.max(y) + 1)
        ax.set_xlabel('X Distance (m)')
        ax.set_ylabel('Z (Lateral Distance)')
        ax.set_zlabel('Y Height (m)')
        ax.set_title('Projectile Motion')

        # Initialize the line and point
        line, = ax.plot([], [], [], lw=2)
        point, = ax.plot([], [], [], 'ro')

        # Update function for the animation
        def update(frame):
            line.set_data(x[:frame], z[:frame])
            line.set_3d_properties(y[:frame])
            point.set_data([x[frame]], [z[frame]])
            point.set_3d_properties([y[frame]])
            return line, point

        ani = FuncAnimation(fig, update, frames=len(x), interval=30, blit=False)
        return ani, line, point

    # Create figure and define the layout
    fig = plt.figure(figsize=(12, 6))

    # Add a subplot for the 3D animation on the left
    ax = fig.add_subplot(1, 2, 1, projection='3d')  # 1 row, 2 columns, 1st plot

    # Add a subplot for the sliders on the right
    sliders_ax = plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
    sliders_ax.axis('off')  # Hide the plot axes for the sliders section

    # Initial plot parameters
    v0_init = 20
    angle_init = 45
    v_z_init = 5  # Initial lateral velocity
    y0_init = 0   # Initial height

    # Create slider axes within the sliders subplot
    slider_ax_v0 = plt.axes([0.65, 0.6, 0.3, 0.03], facecolor='lightgoldenrodyellow')  # Positioned inside right subplot
    slider_ax_angle = plt.axes([0.65, 0.5, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_vz = plt.axes([0.65, 0.4, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_y0 = plt.axes([0.65, 0.3, 0.3, 0.03], facecolor='lightgoldenrodyellow')

    v0_slider = Slider(slider_ax_v0, 'Initial Velocity', 5, 50, valinit=v0_init, valstep=1, handle_style={'facecolor': 'red'})
    angle_slider = Slider(slider_ax_angle, 'Launch Angle', 0, 90, valinit=angle_init, valstep=1, handle_style={'facecolor': 'red'})
    v_z_slider = Slider(slider_ax_vz, 'Lateral Velocity', 0, 20, valinit=v_z_init, valstep=1, handle_style={'facecolor': 'red'})
    y0_slider = Slider(slider_ax_y0, 'Initial Height', 0, 50, valinit=y0_init, valstep=1, handle_style={'facecolor': 'red'})

    v0_slider.vline.set_color('black')
    angle_slider.vline.set_color('black')
    v_z_slider.vline.set_color('black')
    y0_slider.vline.set_color('black')

    # Persistent animation and plot elements
    ani = None
    line = None
    point = None

    # Update function for sliders
    def update_sliders(val):
        global ani, line, point  # Keep the animation and plot elements persistent
        v0 = v0_slider.val
        angle = angle_slider.val
        v_z = v_z_slider.val
        y0 = y0_slider.val
        ax.cla()  # Clear the axis
        ani, line, point = create_animation(v0, angle, v_z, y0, ax)

    # Connect sliders to the update function
    v0_slider.on_changed(update_sliders)
    angle_slider.on_changed(update_sliders)
    v_z_slider.on_changed(update_sliders)
    y0_slider.on_changed(update_sliders)

    # Initial animation
    ani, line, point = create_animation(v0_init, angle_init, v_z_init, y0_init, ax)

    # Show plot
    plt.subplots_adjust(left=0.05, right=0.95, wspace=0.3)  # Adjust layout
    
    def on_close(event):
        plt.close(fig)
        exit(0)
    
    fig.canvas.mpl_connect("close_event", on_close)
    
    plt.show()
    
if __name__ == "__main__":
    projectile_motion_visualizer()
