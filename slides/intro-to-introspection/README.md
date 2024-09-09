# Intro to Introspection

### Summary
Python holds no secrets about your code; except perhaps how to access that information. In this talk, you'll find out how to discover almost any information about running Python code.

### Description
* Introduction (2 minutes)
    * techniques work equally in normal execution, interactive mode, or when debugging.
    * start with the obvious tools like print() before going deeper
* Name discovery (5 minutes)
    * discover names that will resolve in the current scope
    * discover attributes on a random object
* Description discovery (5 minutes)
    * how does this object choose to represent itself
    * get back author notes at runtime
* Type discovery (5 minutes)
    * what _is_ this thing
    * how does this thing relate to other objects
* Code discovery (5 minutes)
    * start using the inspect module
    * lookup signature of callables
    * find the exact location in py file where the object was defined
* Conclusion (2 minutes)
    * typically, all information available while reading code i also available when running the code
    * don't be afraid to peek inside python

### Slides
https://slides.ucodery.com/intro-to-introspection/

## Extra Info

To reproduce any of the code examples, or to play around with
introspection on your own, run the following command from this
directory (python >= 3.7):

```bash
$ python -i ./unknown.py
```
