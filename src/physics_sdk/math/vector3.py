from __future__ import annotations
from dataclasses import dataclass
import math

EPSILON = 1e-9

@dataclass(slots=True)
class Vector3:
    """
    Represents a 3D vector with x, y, and z components.
    """
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def length(self) -> float:
        """
        Calculate the length (magnitude) of the vector.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def squared_length(self) -> float:
        """
        Calculate the squared length of the vector.
        """
        return (self.x * self.x + self.y * self.y + self.z * self.z)
    
    def copy(self) -> "Vector3":
        """
        Return a copy of the vector.
        """
        return Vector3(self.x, self.y, self.z)
    
    def to_tuple(self) -> tuple[float, float, float]:
        """
        Convert vector to tuple.
        """
        return (self.x, self.y, self.z)
    
    def is_zero(self, epsilon: float = 1e-9) -> bool:
        """
        Check whether vector is effectively zero.
        """
        return (
            math.isclose(self.x, 0.0, abs_tol=epsilon)
            and math.isclose(self.y, 0.0, abs_tol=epsilon)
            and math.isclose(self.z, 0.0, abs_tol=epsilon)
        )
    
    def distance_to(self, other: "Vector3") -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z

        return math.sqrt(
            dx * dx +
            dy * dy +
            dz * dz
        )
    

def __add__(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            return NotImplemented
        
        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z    
        )
    
def __sub__(self, other: "Vector3") -> "Vector3":
    if not isinstance(other, Vector3):
        return NotImplemented
    
    return Vector3(
        self.x - other.x,
        self.y - other.y,
        self.z - other.z    
    )
    
def __neg__(self) -> "Vector3":
    return Vector3(-self.x, -self.y, -self.z)
    
def __mul__(self, scalar: float) -> "Vector3":
    if not isinstance(scalar, (int, float)):
        return NotImplemented
    
    return Vector3(
        self.x * scalar,
        self.y * scalar,
        self.z * scalar    
    )
    
def __rmul__(self, scalar: float) -> "Vector3":
    return self * scalar
    
def __truediv__(self, scalar: float) -> "Vector3":
    if not isinstance(scalar, (int, float)):
        return NotImplemented
    
    if scalar == 0:
        raise ValueError("Cannot divide by zero.")
    
    return Vector3(
        self.x / scalar,
        self.y / scalar,
        self.z / scalar    
    )
    
def __iter__(self):
    yield self.x
    yield self.y
    yield self.z

# star task: Implement the __abs__ method which can invoke like abs(v) to get the length of the vector.
def __abs__(self) -> float:
    """
    Return the length (magnitude) of the vector.
    """
    return self.length()

# star task2: Implement the __eq__ method to compare two Vector3 instances for equality.
def __eq__(self, other: object) -> bool:
    if not isinstance(other, Vector3):
        return NotImplemented
    
    return (
        math.isclose(self.x, other.x, abs_tol=EPSILON) and
        math.isclose(self.y, other.y, abs_tol=EPSILON) and
        math.isclose(self.z, other.z, abs_tol=EPSILON)
    )
    

v = Vector3(4, 2, 1)
print(v.length())  # Output: 5.0
print(v.squared_length())  # Output: 21.0