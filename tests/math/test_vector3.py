from physics_sdk.math.vector3 import Vector3
import pytest


def test_zero_vector_has_all_zero_components():
    v = Vector3.zero()
    assert v.x == 0.0
    assert v.y == 0.0
    assert v.z == 0.0

def test_zero_returns_new_instance():
    v1 = Vector3.zero()
    v2 = Vector3.zero()
    assert v1 is not v2

def test_one_vector_has_all_one_components():
    v = Vector3.one()
    assert v.x == 1.0
    assert v.y == 1.0
    assert v.z == 1.0

def test_copy_creates_new_object():
    original = Vector3(1,2,3)
    copied = original.copy()
    assert copied is not original

def test_copy_preserves_values():
    original = Vector3(1,2,3)
    copied = original.copy()
    assert copied.x == original.x
    assert copied.y == original.y
    assert copied.z == original.z

def test_copy_is_independent():
    original = Vector3(1,2,3)
    copied = original.copy()
    copied.x = 100
    assert original.x == 1

def test_dot_parallel_vectors():
    a = Vector3(1, 0, 0)
    b = Vector3(2, 0, 0)

    assert a.dot(b) == 2

def test_dot_perpendicular_vectors():
    a = Vector3(1, 0, 0)
    b = Vector3(0, 1, 0)

    assert a.dot(b) == 0

def test_dot_opposite_vectors():
    a = Vector3(1, 0, 0)
    b = Vector3(-1, 0, 0)

    assert a.dot(b) == -1

def test_dot_with_zero_vector():
    a = Vector3(1, 2, 3)
    b = Vector3(0, 0, 0)

    assert a.dot(b) == 0

def test_dot_is_commutative():
    a = Vector3(1, 2, 3)
    b = Vector3(4, 5, 6)

    assert a.dot(b) == b.dot(a)

def test_dot_with_large_values():
    a = Vector3(1e6, 2e6, 3e6)
    b = Vector3(4, 5, 6)

    result = a.dot(b)

    assert isinstance(result, float)

def test_cross_xy_is_z():
    a = Vector3(1, 0, 0)
    b = Vector3(0, 1, 0)
    r = a.cross(b)
    assert r == Vector3(0, 0, 1)

def test_cross_is_anti_commutative():
    a = Vector3(1, 2, 3)
    b = Vector3(4, 5, 6)

    assert a.cross(b) == -b.cross(a)

def test_cross_parallel_vectors_is_zero():
    a = Vector3(2, 2, 2)
    b = Vector3(4, 4, 4)

    r = a.cross(b)

    assert r.is_zero()

def test_cross_result_is_orthogonal():
    a = Vector3(1, 0, 0)
    b = Vector3(0, 1, 0)

    r = a.cross(b)

    assert r.dot(a) == 0
    assert r.dot(b) == 0

def test_normalize_zero_vector_raises():
    v = Vector3.zero()
    with pytest.raises(ValueError):
        v.normalize()

def test_normalize_has_unit_length():

    v = Vector3(3, 4, 0)

    n = v.normalize()

    assert pytest.approx(n.length()) == 1.0

def test_normalize_preserves_direction():

    v = Vector3(10, 0, 0)

    n = v.normalize()

    assert n == Vector3(1, 0, 0)