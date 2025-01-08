import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from scipy.integrate import solve_ivp

def double_pendulum_visualizer():
    """Run the double pendulum visualizer with adjustable sliders."""
    # Constants and parameters
    g = 9.81  # Acceleration due to gravity (m/s^2)
    
    # Initial parameters for the pendulum
    l1_init, l2_init = 1.0, 1.0  # Lengths of the pendulum arms (m)
    m1_init, m2_init = 1.0, 1.0  # Masses of the pendulum bobs (kg)
    theta1_init, theta2_init = np.pi / 2, np.pi / 2  # Initial angles (radians)

    # Time settings
    t_span = (0, 20)  # Time range for the simulation (seconds)
    t_eval = np.linspace(*t_span, 1000)  # Time points for evaluation

    # Function to compute the motion of the double pendulum
    def compute_pendulum(l1, l2, m1, m2, theta1, theta2):
        def equations(t, y):
            theta1, omega1, theta2, omega2 = y
            delta_theta = theta2 - theta1
            
            denom1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta_theta) ** 2
            denom2 = (l2 / l1) * denom1
            
            domega1 = ((m2 * l1 * omega1 ** 2 * np.sin(delta_theta) * np.cos(delta_theta) +
                        m2 * g * np.sin(theta2) * np.cos(delta_theta) +
                        m2 * l2 * omega2 ** 2 * np.sin(delta_theta) -
                        (m1 + m2) * g * np.sin(theta1)) / denom1)
            
            domega2 = ((-m2 * l2 * omega2 ** 2 * np.sin(delta_theta) * np.cos(delta_theta) +
                        (m1 + m2) * g * np.sin(theta1) * np.cos(delta_theta) -
                        (m1 + m2) * l1 * omega1 ** 2 * np.sin(delta_theta) -
                        (m1 + m2) * g * np.sin(theta2)) / denom2)
            
            return [omega1, domega1, omega2, domega2]

        # Initial state
        y0 = [theta1, 0.0, theta2, 0.0]

        # Solve the equations of motion
        sol = solve_ivp(equations, t_span, y0, t_eval=t_eval, method="RK45")
        theta1, theta2 = sol.y[0], sol.y[2]
        
        # Convert polar to Cartesian coordinates
        x1 = l1 * np.sin(theta1)
        y1 = -l1 * np.cos(theta1)
        x2 = x1 + l2 * np.sin(theta2)
        y2 = y1 - l2 * np.cos(theta2)
        
        return x1, y1, x2, y2

    # Initialize coordinates
    x1, y1, x2, y2 = compute_pendulum(l1_init, l2_init, m1_init, m2_init, theta1_init, theta2_init)

    # Create figure
    fig = plt.figure(figsize=(12, 6))

    # Animation plot (left)
    ax = fig.add_subplot(1, 2, 1)
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal', adjustable='datalim')
    ax.grid()
    line, = ax.plot([], [], 'o-', lw=2)

    def update(frame):
        """Update function for the animation."""
        line.set_data([0, x1[frame], x2[frame]], [0, y1[frame], y2[frame]])
        return line,

    ani = FuncAnimation(fig, update, frames=len(t_eval), interval=30, blit=True)

    # Sliders (right)
    slider_ax_l1 = plt.axes([0.65, 0.7, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_l2 = plt.axes([0.65, 0.6, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_m1 = plt.axes([0.65, 0.5, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_m2 = plt.axes([0.65, 0.4, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_theta1 = plt.axes([0.65, 0.3, 0.3, 0.03], facecolor='lightgoldenrodyellow')
    slider_ax_theta2 = plt.axes([0.65, 0.2, 0.3, 0.03], facecolor='lightgoldenrodyellow')

    l1_slider = Slider(slider_ax_l1, 'Length 1', 0.5, 2.0, valinit=l1_init)
    l2_slider = Slider(slider_ax_l2, 'Length 2', 0.5, 2.0, valinit=l2_init)
    m1_slider = Slider(slider_ax_m1, 'Mass 1', 0.5, 2.0, valinit=m1_init)
    m2_slider = Slider(slider_ax_m2, 'Mass 2', 0.5, 2.0, valinit=m2_init)
    theta1_slider = Slider(slider_ax_theta1, 'Angle 1', 0, np.pi, valinit=theta1_init)
    theta2_slider = Slider(slider_ax_theta2, 'Angle 2', 0, np.pi, valinit=theta2_init)

    def slider_update(val):
        """Update the pendulum motion based on slider values."""
        nonlocal x1, y1, x2, y2
        l1 = l1_slider.val
        l2 = l2_slider.val
        m1 = m1_slider.val
        m2 = m2_slider.val
        theta1 = theta1_slider.val
        theta2 = theta2_slider.val

        # Recompute pendulum motion
        x1, y1, x2, y2 = compute_pendulum(l1, l2, m1, m2, theta1, theta2)

    # Connect sliders to the update function
    l1_slider.on_changed(slider_update)
    l2_slider.on_changed(slider_update)
    m1_slider.on_changed(slider_update)
    m2_slider.on_changed(slider_update)
    theta1_slider.on_changed(slider_update)
    theta2_slider.on_changed(slider_update)

    # Adjust layout and show the plot
    plt.subplots_adjust(left=0.05, right=0.95, wspace=0.3)
    plt.show()

if __name__ == "__main__":
    double_pendulum_visualizer()
