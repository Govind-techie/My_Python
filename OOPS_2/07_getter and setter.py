# Getter and Setter : Getter is used to get the value of a private variable and setter is used to set the value of a private variable.

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private variable

    @property # It is used to get the value of the radius property.
    def radius(self): # Getter for the radius property.
        return self._radius

    @radius.setter # It is used to set the value of the radius property.
    def radius(self, value): # Setter for the radius property.
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

# Example usage
circle = Circle(5)
print(circle.radius)  # Accessing the radius using the getter

circle.radius = 10  # Modifying the radius using the setter
print(circle.radius)

try:
    circle.radius = -3  # Attempting to set a negative radius
except ValueError as e:
    print(e)  # Output: Radius cannot be negative
