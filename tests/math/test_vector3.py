from physics_sdk.math.vector3 import Vector3


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