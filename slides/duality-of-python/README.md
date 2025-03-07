# The Duality of Python

## Summary

## Description
You may have learned that in Python, everything is an object. This is true; even primitive data like integers or stack frames are objects. You may also have learned that the base type of every object is type. This is also true. But these two truths seem to be in conflict with one another. Join me as I explore some of Python's most fundamental built-ins and try to reconcile the question: how can `object`'s type be `type` while at the same time `type` inherits from `object`?

## Outline

- Intro (1 minute)
- What is `object`? (3 minute)
- What is `type`? (3 minutes)
- A class vs an instance (5 minutes)
  - how does one turn into the other?
- Inheritance and MRO (5 minutes)
  - what does isinstance tell us
  - what does issubclass tell us
- breaking down class creation (4 minutes)
  - using `class`
  - using `type()`
  - using `new_class()`
- Answer: which comes first when Python initialized (2 minutes)
- Conclusion: how can both come first (2 minutes)
