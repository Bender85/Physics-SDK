# ADR-0003: Vector3 factory methods (zero, one, axis helpers)

## Status
Proposed

## Context
We often need common vector constants such as:
- zero vector (0,0,0)
- unit vectors (1,0,0), (0,1,0), (0,0,1)

These are frequently used in physics and simulation code.

## Decision
We introduce class-level factory methods:

- Vector3.zero()
- Vector3.one()
- Vector3.up()
- Vector3.right()
- Vector3.forward()

Implemented as @classmethod methods.

## Consequences
Positive:
- Improves code readability
- Avoids magic numbers
- Standardizes common vectors
- Common pattern in game engines (Unity, Unreal-like design)

Negative:
- Slight increase in API surface
- Might be unnecessary in very minimal math-only usage