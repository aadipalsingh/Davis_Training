#calaculate the area and perimeter of circle Using exception handling
import math
try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    print(f"Area of the circle: {area:.2f}")
    print(f"Perimeter of the circle: {perimeter:.2f}")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")