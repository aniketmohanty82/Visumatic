import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

def projectile_motion_visualizer():
    """Run the projectile motion visualizer."""

    # Function to compute projectile motion
    def projectile_motion(v0, angle, v_z, y0, g=9.81, steps=500):
        theta = np.radians(angle)
        t_flight = (v0 * np.sin(theta) + np.sqrt((v0 * np.sin(theta))**2 + 2 * g * y0)) / g
        t = np.linspace(0, t_flight, steps)
        x = v0 * np.cos(theta) * t
        y = y0 + v0 * np.sin(theta) * t - 0.5 * g * t**2
        z = v_z * t
        return x, y, z, t

    # Create figure and define the layout
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 2, 1, projection='3d')  # 3D plot on the left
    ax.set_xlabel('X Distance (m)')
    ax.set_ylabel('Z (Lateral Distance)')
    ax.set_zlabel('Y Height (m)')
    ax.set_title('Projectile Motion')

    sliders_ax = plt.subplot(1, 2, 2)  # Sliders on the right
    sliders_ax.axis('off')

    # Initial plot parameters
    v0_init = 20
    angle_init = 45
    v_z_init = 5
    y0_init = 0

    # Create sliders
    slider_ax_v0 = plt.axes([0.65, 0.6, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_angle = plt.axes([0.65, 0.5, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_vz = plt.axes([0.65, 0.4, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_y0 = plt.axes([0.65, 0.3, 0.3, 0.03], facecolor='lightgoldenrodyellow')

    v0_slider = Slider(slider_ax_v0, 'Initial Velocity', 5, 50, valinit=v0_init, valstep=1)
    angle_slider = Slider(slider_ax_angle, 'Launch Angle', 0, 90, valinit=angle_init, valstep=1)
    v_z_slider = Slider(slider_ax_vz, 'Lateral Velocity', 0, 20, valinit=v_z_init, valstep=1)
    y0_slider = Slider(slider_ax_y0, 'Initial Height', 0, 50, valinit=y0_init, valstep=1)

    # Compute initial projectile motion
    x, y, z, t = projectile_motion(v0_init, angle_init, v_z_init, y0_init)

    line, = ax.plot(x, z, y, lw=2)  # Set initial trajectory
    point, = ax.plot([x[0]], [z[0]], [y[0]], 'ro')  # Set initial point

    def update(frame):
        """Update function for the animation."""
        line.set_data(x[:frame], z[:frame])
        line.set_3d_properties(y[:frame])
        point.set_data([x[frame]], [z[frame]])
        point.set_3d_properties([y[frame]])
        return line, point

    ani = FuncAnimation(fig, update, frames=len(x), interval=30, blit=False)

    def slider_update(val):
        """Update the animation and axis limits based on slider values."""
        nonlocal x, y, z, t
        v0 = v0_slider.val
        angle = angle_slider.val
        v_z = v_z_slider.val
        y0 = y0_slider.val

        # Recompute projectile motion
        x, y, z, t = projectile_motion(v0, angle, v_z, y0)

        # Update axis limits dynamically
        ax.set_xlim(0, max(x) + 5)
        ax.set_ylim(0, max(z) + 5)
        ax.set_zlim(0, max(y) + 5)

        # Update line and point data
        line.set_data(x, z)
        line.set_3d_properties(y)
        point.set_data([x[0]], [z[0]])
        point.set_3d_properties([y[0]])

    # Connect sliders to the update function
    v0_slider.on_changed(slider_update)
    angle_slider.on_changed(slider_update)
    v_z_slider.on_changed(slider_update)
    y0_slider.on_changed(slider_update)

    # def on_close(event):
    #     """Handle the figure close event."""
    #     plt.close(fig)  # Close only this figure, not the entire app.

    # fig.canvas.mpl_connect("close_event", on_close)

    plt.subplots_adjust(left=0.05, right=0.95, wspace=0.3)
    plt.show()

if __name__ == "__main__":
    projectile_motion_visualizer()
