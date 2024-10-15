# pendulum.py

import numpy as np
from scipy.integrate import solve_ivp

# Pendulum constants
g = 9.81  # Default gravitational acceleration (m/s²)
L = 1.0   # Default length of the pendulum (meters)
theta0 = np.pi * 2 / 5  # Default initial angle (45 degrees)
omega0 = 0.0        # Default initial angular velocity (rest)

# Pendulum differential equation
def pendulum_ode(t, y, g, L):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Function to solve the pendulum equation for given parameters
def solve_pendulum(L, theta0, g, t_start, t_end, t_eval):
    y0 = [theta0, omega0]
    solution = solve_ivp(pendulum_ode, [t_start, t_end], y0, t_eval=t_eval, args=(g, L))
    theta_sol = solution.y[0]
    x = L * np.sin(theta_sol)
    y = -L * np.cos(theta_sol)
    return x, y

# Initial conditions function
def get_initial_conditions():
    return theta0, omega0, g, L
