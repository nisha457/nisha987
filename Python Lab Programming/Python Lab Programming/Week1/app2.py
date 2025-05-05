import math

def calculate_distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points (x1, y1) and (x2, y2).

    :param x1: x-coordinate of the first point (float or int).
    :param y1: y-coordinate of the first point (float or int).
    :param x2: x-coordinate of the second point (float or int).
    :param y2: y-coordinate of the second point (float or int).
    :return: The distance between the two points (float).
    """
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Input coordinates
x1 = float(input("Enter x-coordinate of the first point: "))
y1 = float(input("Enter y-coordinate of the first point: "))
x2 = float(input("Enter x-coordinate of the second point: "))
y2 = float(input("Enter y-coordinate of the second point: "))

# Calculate distance
distance = calculate_distance(x1, y1, x2, y2)

# Output the result
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
