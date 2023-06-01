from math import pi, cos, tan
def calculate_projectile_height(y0, x, theta, v0):
    g = 9.81  # acceleration due to gravity (m/s^2)
    # Convert theta from degrees to radians
    theta = theta * (pi / 180)
    # Calculate the height of the projectile
    numerator = g * x**2
    denominator = 2 * (v0 * cos(theta))**2
    height = y0 + x * tan(theta) - numerator / denominator
    return height
# Example usage
barrel_height = 1  # y0 (m)
horizontal_distance = 0.5  # x (m)
elevation_angle = 80  # theta (degrees)
initial_velocity = 44  # v0 (m/s)
projectile_height = calculate_projectile_height(barrel_height, horizontal_distance, elevation_angle, initial_velocity)
print("The height of the projectile is:", round(projectile_height,2), "m")