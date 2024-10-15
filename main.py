import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pendulum import solve_pendulum
import tkinter as tk
from tkinter import simpledialog

def init_plot(ax, s):
    """ Initialize the plot with limits and remove ticks and borders """
    ax.set_xlim(-s*3, s*3)
    ax.set_ylim(-s*3, s*3)
    ax.set_aspect('equal')
    ax.set_xticks([])  # Remove x-axis ticks
    ax.set_yticks([])  # Remove y-axis ticks

    # Remove the borders (spines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

def get_user_input():
    """ Create a tkinter GUI to get user input for gravity and pendulum length with default values """
    # Initialize tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Default values
    default_g = 9.81  # Default gravitational constant (m/s²)
    default_L = 1.0   # Default pendulum length (meters)
    
    # Prompt for gravitational constant
    g = simpledialog.askfloat("Input", f"Enter the gravitational constant (g in m/s², default {default_g}):", initialvalue=default_g)
    
    # Prompt for pendulum length
    L = simpledialog.askfloat("Input", f"Enter the length of the pendulum (L in meters, default {default_L}):", initialvalue=default_L)

    # Check if user clicked "OK" without input and assign default if necessary
    if g is None:
        g = default_g
    if L is None:
        L = default_L

    # Close tkinter root window after inputs are taken
    root.quit()

    return g, L


def main():
    # Get user input for gravitational constant and pendulum length
    g, L = get_user_input()

    # Time span for simulation
    simulation_time = 100
    frame_per_sec = simulation_time * 50
    t_eval = np.linspace(0, simulation_time, frame_per_sec)  # time points to evaluate (start, stop, num)

    # Initial conditions (initial angle, velocity)
    theta0 = np.pi * 2 / 5  # 45 degrees
    omega0 = 0.0  # Resting pendulum

    # Set up the figure and axis
    fig, ax = plt.subplots()
    s = 1.5  # Size factor for visual padding
    init_plot(ax, s)

    # Set background colours
    fig.patch.set_facecolor('#E8E8E8')
    ax.set_facecolor('#E8E8E8')

    # Solve the pendulum equation with initial parameters
    x, y = solve_pendulum(L, theta0, g, t_start=0, t_end=simulation_time, t_eval=t_eval)

    # Pendulum line
    line, = ax.plot([], [], 'o-', lw=2, color='crimson')

    # Initialization function: plot the empty pendulum at t=0
    def init():
        line.set_data([], [])
        return line,

    # Animation function: update the pendulum position at each frame
    def update(frame):
        y_offset = 1.0  # set constant distance
        idx = frame % len(t_eval)  # Modulo operator to cycle through frames smoothly
        line.set_data([0, x[idx]], [y_offset, y[idx] + y_offset])  # Update x and y values
        return line,

    # Create the animation
    interval_c = (simulation_time / frame_per_sec) * 1000  # interval constant | convert to milliseconds
    ani = FuncAnimation(fig, update, frames=len(t_eval), init_func=init, blit=True, interval=interval_c)

    # Variable to track the animation state (paused or not)
    is_paused = [False]  # Using a list to make it mutable inside the nested function

    # Key press event handler to toggle pause on spacebar press
    def on_key_press(event):
        if event.key == ' ':  # Spacebar key
            if is_paused[0]:
                ani.event_source.start()  # Resume animation
            else:
                ani.event_source.stop()  # Pause animation
            is_paused[0] = not is_paused[0]  # Toggle the pause state

    # Connect the key press event to the figure
    fig.canvas.mpl_connect('key_press_event', on_key_press)

    # Display the animation
    plt.show()

# Ensures the script runs only when executed directly, not imported
if __name__ == "__main__":
    main()
