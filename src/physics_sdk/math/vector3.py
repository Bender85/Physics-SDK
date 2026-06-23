from __future__ import annotations
import math


class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # -------------------------
    # FACTORY METHODS
    # -------------------------
    @classmethod
    def zero(cls) -> "Vector3":
        return cls(0.0, 0.0, 0.0)

    @classmethod
    def one(cls) -> "Vector3":
        return cls(1.0, 1.0, 1.0)

    # -------------------------
    # CORE UTILITIES
    # -------------------------
    def copy(self) -> "Vector3":
        return Vector3(self.x, self.y, self.z)

    def to_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    def is_zero(self, eps: float = 1e-9) -> bool:
        return (
            abs(self.x) < eps and
            abs(self.y) < eps and
            abs(self.z) < eps
        )

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def squared_length(self) -> float:
        return self.x**2 + self.y**2 + self.z**2

    def distance_to(self, other: Vector3) -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )

    # -------------------------
    # DOT PRODUCT
    # -------------------------
    def dot(self, other: "Vector3") -> float:
        if not isinstance(other, Vector3):
            return NotImplemented

        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )
    
    # -------------------------
    # CROSS PRODUCT
    # -------------------------
    def cross(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            return NotImplemented

        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    # -------------------------
    # NORMALIZATION
    # -------------------------
    def normalize(self) -> "Vector3":
        length = self.length()

        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")

        inv_length = 1.0 / length

        return Vector3(
            self.x * inv_length,
            self.y * inv_length,
            self.z * inv_length
        )

    # -------------------------
    # PYTHON OPERATORS (NEW)
    # -------------------------
    def __add__(self, other: Vector3) -> Vector3:
        if not isinstance(other, Vector3):
            return NotImplemented

        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other: Vector3) -> Vector3:
        if not isinstance(other, Vector3):
            return NotImplemented

        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__(self, scalar: float) -> Vector3:
        if not isinstance(scalar, (int, float)):
            return NotImplemented

        return Vector3(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )

    def __rmul__(self, scalar: float) -> Vector3:
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> Vector3:
        if scalar == 0:
            raise ZeroDivisionError("Division by zero in Vector3")

        return Vector3(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar
        )

    def __neg__(self) -> Vector3:
        return Vector3(-self.x, -self.y, -self.z)

    def __abs__(self) -> float:
        return self.length()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector3):
            return NotImplemented

        return (
            math.isclose(self.x, other.x, abs_tol=1e-9) and
            math.isclose(self.y, other.y, abs_tol=1e-9) and
            math.isclose(self.z, other.z, abs_tol=1e-9)
        )

    def __repr__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"