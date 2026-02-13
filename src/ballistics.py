import numpy as np
import matplotlib.pyplot as plt


def calculate_projectile():
    print("\n[INPUT] Provide firearm parameters")

    try:
        velocity = float(input("Muzzle Velocity (m/s): "))
        theta = float(input("Firing Angle (degrees): "))
    except ValueError:
        print("[ERROR] Invalid values, defaulting to preset parameters.")
        velocity, theta = 700, 40

    gravity = 9.81
    t_max = (2 * velocity * np.sin(np.radians(theta))) / gravity
    t_points = np.linspace(0, t_max, 500)

    x_coords = velocity * np.cos(np.radians(theta)) * t_points
    y_coords = velocity * np.sin(np.radians(theta)) * t_points - 0.5 * gravity * t_points**2

    plt.plot(x_coords, y_coords)
    plt.title("Projectile Path Simulation")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.show()
