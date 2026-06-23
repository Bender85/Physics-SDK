# ADR-0002: Vector3 mutability decision

## Status
Accepted

## Context
Vector3 is a core data structure used heavily in physics simulation. We need to decide whether Vector3 should be mutable or immutable.

Immutable vectors are safer but generate more memory allocations. Mutable vectors are faster but require careful usage to avoid side effects.

## Decision
We choose a MUTABLE Vector3 implementation.

## Reasoning
- Physics simulation requires high performance
- Millions of vector operations per second are expected
- Reducing memory allocations is important
- We accept controlled risk of side effects

## Consequences
Positive:
- Better performance
- Less memory allocation
- Faster simulation loops

Negative:
- Possible side effects if objects are shared incorrectly
- Requires discipline in API usage
- Harder debugging if references are reused unintentionally