# ADR-0001: Separation of Math and Physics modules

## Status
Accepted

## Context
We are building a physics simulation engine. Initially, there is a risk of mixing mathematical constructs (vectors, matrices) with physical behavior (rigid bodies, forces, simulation rules).

If math and physics are mixed, the system becomes hard to maintain and reuse in other contexts (e.g. rendering, robotics, AI).

## Decision
We separate the codebase into two independent layers:

- `math/` — pure mathematical structures (Vector3, Matrix3, Quaternion)
- `physics/` — physical simulation logic (RigidBody, Forces, Gravity, World)

Math objects must NOT contain physics logic.

## Consequences
Positive:
- Clean architecture
- Reusable math module
- Easier testing
- Better scalability

Negative:
- Slightly more abstraction at the beginning
- Requires discipline to keep boundaries clean