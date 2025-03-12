---
lineNumbers: false
colorSchema: light
drawings:
  persist: false
transition: slide-left
title: The Duality of Python
layout: intro
class: text-center
---

<!--
## The
# Dyadic Foundation
## of Python
-->

<h1 style="position: relative; right: 19%; color: #376496; text-shadow: black -1.5px -1.5px; margin: 0;">
  The Duality
</h1>
<img src="/images/python-logo.png" style="height: 100px; margin-left: auto; margin-right: auto;">
<h1 style="position: relative; left: 16%; color: #fce664; text-shadow: black 1.5px 1.5px; margin: 0; line-height: 0.15em;">
  of Python
</h1>

<!--
Take you with me as I wrestle to answer a question of how Python deeply works
-->

---
layout: center
---

# Everything in Python is an object

> Objects are Python’s abstraction for data. All data in a Python program is
> represented by objects or by relations between objects.
>
> <p style="text-align: right;">- <a href="https://docs.python.org/3/reference/datamodel.html">Python data model</a></p>

<!--
Python is inclusive of other programing styles: imperitive, functional

In the end, it is formost and Object-Oriented language

Everything you can touch/reach in Python is an object

Not much in this dynamic language that can be depended upon 100%
-->

---
layout: two-cols-header
---

# object

````md magic-move
```python
assert isinstance(ArgumentParser, object)
```
```python
assert isinstance(ArgumentParser(), object)
```
```python
assert isinstance(max, object)
```
```python
assert isinstance((), object)
```
```python
assert isinstance(b"Python", object)
```
```python
assert isinstance(None, object)
```
```python
assert isinstance(__builtins__, object)
```
```python
thing = compile("import this", "<example>", "exec")
# <code object <module> at 0x1032fe090, file "<example>", line 1>
assert isinstance(thing, object)
```
```python
thing = ctypes.pointer(ctypes.c_int(42))
<__main__.LP_c_int object at 0x105c7db50>
assert isinstance(thing, object)
```
````

::left::

- classes

<v-clicks at="1">

- instances
- functions
- data structures
- base data types

</v-clicks>

::right::

<v-clicks at="5">

- constants
- namespaces
- code
- pointers

</v-clicks>

---
layout: quote
---

# Everything in Python has a type

> Every object has an identity, a type and a value.
>
> <p style="text-align: right;">- <a href="https://docs.python.org/3/reference/datamodel.html">Python data model</a></p>

<!--
everything's type is (eventually) type

only information a thing must have: type and id

Not much in this dynamic language that can be depended upon 100%
-->

---
layout: two-cols-header
---

# type

````md magic-move
```python
type(ArgumentParser) # <class 'type'>
```
```python
type(ArgumentParser) # <class 'type'>
type(max) # <class 'builtin_function_or_method'>
```
```python
type(ArgumentParser) # <class 'type'>
type(max) # <class 'builtin_function_or_method'>
type(b"Python") # <class 'bytes'>
```
```python
type(ArgumentParser) # <class 'type'>
type(max) # <class 'builtin_function_or_method'>
type(b"Python") # <class 'bytes'>
type(None) # <class 'NoneType'>
```
```python
type(type(ArgumentParser)) # <class 'type'>
type(type(max)) # <class 'type'>
type(type(b"Python")) # <class 'type'>
type(type(None)) # <class 'type'>
```
```python
type(type)
# <class 'type'>
```
```python
type(type(type(type)))
# <class 'type'>
```
```python
type(object)
# <class 'type'>
```
```python
assert isinstance(type, object)
```
````

::left::

- classes

<v-clicks at="1">

- functions
- base data types
- constant types

</v-clicks>

::right::

<v-click at="5">

- `type` itself (recursively)

</v-click>

<v-clicks at="7">

- `object`
- `type` is an object

</v-clicks>

<!--
- and instnaces
- even C-functions

`type` is the self-referential type that ends the type hierarchy

here we have the only 2 constant facts in a dynamic language, seemingly contradicting each other
-->

---
layout: intro
class: text-center
---

# What came first, `object` or `type`?

---
layout: default
---

# What is the role of object
- root of every class' inheritance tree
- provides most default behaviours

<!--
All behaviour we expect from Python comes from object - not interpreter
Things we think we can rely on, but are not 100%

anything can be string-ified? object

new classes/instances are boolean-true by default? object

object equality falls back on `id`? object

__dir__ powers dir() and TAB? object
-->

---

# object
````md magic-move
```python
class ArgumentDict(ArgumentParser, UserDict):
    def __init__(): ...
```
```python
class ArgumentDict(ArgumentParser, UserDict):
    def __init__(): ...
ArgumentDict.__bases__
# (<class 'argparse.ArgumentParser'>,
#  <class 'collections.UserDict'>)
```
```python
class ArgumentDict(ArgumentParser, UserDict):
    def __init__(): ...
ArgumentDict.__bases__
# (<class 'argparse.ArgumentParser'>,
#  <class 'collections.UserDict'>)
ArgumentParser.__bases__
# (<class 'argparse._AttributeHolder'>,
#  <class 'argparse._ActionsContainer'>)
```
```python
class ArgumentDict(ArgumentParser, UserDict):
    def __init__(): ...
ArgumentDict.__bases__
# (<class 'argparse.ArgumentParser'>,
#  <class 'collections.UserDict'>)
ArgumentParser.__bases__
# (<class 'argparse._AttributeHolder'>,
#  <class 'argparse._ActionsContainer'>)
UserDict.__bases__
# (<class 'collections.abc.MutableMapping'>,)
```
```python
class ArgumentDict(ArgumentParser, UserDict):
    def __init__(): ...
ArgumentDict.__mro__
# (<class '__main__.ArgumentDict'>,
#  <class 'argparse.ArgumentParser'>,
#  <class 'argparse._AttributeHolder'>,
#  <class 'argparse._ActionsContainer'>,
#  <class 'collections.UserDict'>,
#  <class 'collections.abc.MutableMapping'>,
#  <class 'collections.abc.Mapping'>,
#  <class 'collections.abc.Collection'>,
#  <class 'collections.abc.Sized'>,
#  <class 'collections.abc.Iterable'>,
#  <class 'collections.abc.Container'>,
#  <class 'object'>)
```
```python
class ArgumentDict(ArgumentParser, UserDict):
    def __init__(): ...
ArgumentDict.__init__
# <function ArgumentDict.__init__ at 0x105ca9120>
```
```python
class ArgumentDict(ArgumentParser, UserDict):
    def __init__(): ...
ArgumentDict.__init__
# <function ArgumentDict.__init__ at 0x105ca9120>
ArgumentDict.__repr__
# <function _AttributeHolder.__repr__ at 0x1034d5ee0>
```
```python
class ArgumentDict(ArgumentParser, UserDict):
    def __init__(): ...
ArgumentDict.__init__
# <function ArgumentDict.__init__ at 0x105ca9120>
ArgumentDict.__repr__
# <function _AttributeHolder.__repr__ at 0x1034d5ee0>
ArgumentDict.__str__
# <slot wrapper '__str__' of 'object' objects>
```
```python
class ArgumentDict(ArgumentParser, UserDict):
    def __init__(): ...
ArgumentDict.__init__
# <function ArgumentDict.__init__ at 0x105ca9120>
ArgumentDict.__repr__
# <function _AttributeHolder.__repr__ at 0x1034d5ee0>
ArgumentDict.__str__
# <slot wrapper '__str__' of 'object' objects>
ArgumentDict.json
# Traceback (most recent call last):
#   File "<python-input-122>", line 1, in <module>
#     ArgumentDict.json
# AttributeError: type object 'ArgumentDict' has no attribute 'json'
```
````

<!--
We could continue to ask for __bases__ until we ran out of parents

BUT! This is a terrible way to ascemble all parentage

__mro__ linerized the inheritance graph. Lose some relationships, but NO duplcation

This is exactly the order that attributed/methods are looked up

object is ALWAYS last
-->

---

# object

````md magic-move
```python
class Nil:
    pass
```
```python
class Nil:
    pass
Nil.__bases__
# (<class 'object'>,)
```
```python
class Nil:
    pass
Nil.__bases__
# (<class 'object'>,)
Nil.__mro__
# (<class '__main__.Nil'>, <class 'object'>)
```
```python
object
```
```python
object.__bases__
# ()
```
```python
object.__bases__
# ()
object.__mro__
# (<class 'object'>,)
```
```python
type
```
```python
type.__bases__
# (<class 'object'>,)
```
```python
type.__bases__
# (<class 'object'>,)
type.__mro__
# (<class 'type'>, <class 'object'>)
```
````

---
layout: default
---

# What is the role of type
- creates new classes
- retrieves what class created some object

---

# type

````md magic-move
```python
argd = ArgumentDict()
```
```python
argd = ArgumentDict()
type(argd)
# <class '__main__.ArgumentDict'>
```
```python
ArgumentDict
```
```python
type(ArgumentDict)
# <class 'abc.ABCMeta'>
```
```python
type(ABCMeta)
# <class 'type'>
```
```python
type
```
```python
type(type)
# <class 'type'>
```
```python
object
```
```python
type(object)
# <class 'type'>
```
````

<!--
What question is this answering?

What does it mean for ArgumentParser to be of type 'type'?

It means that ArgumentParser was created from a thing named 'type'

So 'type-of' question can be rephrased as what is this thing's creator class
-->

---

# type

````md magic-move
```python
NewNil = type('NewNil', (), {})
```
```python
NewNil = type('NewNil', (), {})
# <class '__main__.NewNil'>
```
```python
NewNil = type('NewNil', (), {})
# <class '__main__.NewNil'>
NewNil()
# <__main__.NewNil object at 0x105b33a10>
```
```python
type(NewNil) is type
```
```python
type(NewNil) is NewNil.__class__
```
````

<!--
Cannot tell post-creation if `class` or `type()` was used
-->

---

# What is the role of class

- collection of other objects contained in a series of hierarchical namespace
- type craetes new classes
- object that creates instances

<!--
- or created by class created by type
- all classes are also instances

> These objects normally act as factories for new instances of themselves [Data Model]
-->

---

# What is the role of instance

- collection of other objects contained in a series of hierarchical namespace
- object's class is its type
- object created by a class

<!--
specialized, in-line, for of sub-classing

object == instance, type == class

> A class instance is created by calling a class object [Data model]
-->

---

# What is the role of instance

- some crate classes
- some create instances
- most create neither classes nor instances

<!--
- these are typcially called metaclasses

- classes, as they are simultaniously instances

- this set of thing are what Python programmers typcially mean by an "instance"
  - doesn't allow for further specialization

- some other's are callable but not factories

so, by the definitions at the start, everything in Python is an instance
everything has a class (but only some are a class)
-->

---
layout: quote
transition: view-transition
---

# Everything in Python is an object
# Everything in Python has a type

---
layout: quote
---

# Everything in Python is an instance
# Everything in Python has a class

---
layout: intro
class: text-center
transition: view-transition
---

# What came first, the object or the type?

---
layout: intro
class: text-center
---

# What came first, the class or the instance?

<!--
I do realize I have yet to answer my first question.

But I am here to talk about Duality

Pythonistas typically think of classes coming first, and instances following, coming from classes

Actually, the opposite is true
-->

---
layout: two-cols
---

# object

<br/><br/>

- top of all inheritance
- is a class
- is an instance of type
- MRO is (object)

::right::

# type

<br/><br/>

- first class creator
- is a class
- is an instance of type
- MRO is (type, object)

<!--
type of, made-by `type`

type is a metaclass

object is a class class
-->

---
layout: default
class:
---

<h1>An An<img src="/images/c-logo.svg" style="display:inline; vertical-align: bottom; height: 1.1em;">wer</h1>

<v-click>

````md magic-move
```c
struct PyObject {
    Py_ssize_t ob_refcnt;
    PyTypeObject *ob_type;
};
```
```c
struct PyObject {
    Py_ssize_t ob_refcnt;
    PyTypeObject *ob_type;
};
struct PyVarObject {
    PyObject ob_base;
    Py_ssize_t ob_size;
};
```
```c
struct PyObject {
    Py_ssize_t ob_refcnt;
    PyTypeObject *ob_type;
};
struct PyVarObject {
    PyObject ob_base;
    Py_ssize_t ob_size;
};
```
```c
struct PyObject {
    Py_ssize_t ob_refcnt;
    PyTypeObject *ob_type;
};
struct PyVarObject {
    PyObject ob_base;
    Py_ssize_t ob_size;
};
struct PyTypeObject {
    PyVarObject ob_base;
    const char *tp_name;
    Py_ssize_t tp_basicsize, tp_itemsize;

    /* type specific implementation */
};
```
````

</v-click>

<div v-click="[3, '+1']" style="transition: all 500ms ease;">

> Nothing is actually declared to be a PyObject, but every pointer to
> a Python object can be cast to a PyObject*.  This is inheritance built
> by hand.  Similarly every pointer to a variable-size Python object can,
> in addition, be cast to PyVarObject*.
> <p style="text-align: right;">- <a href="https://github.com/python/cpython/blob/main/Include/object.h">Include/object.h</a></p>

</div>

<!--
The technical answer

comment by Tim Peters, July 7 2002 (Python 2.3.0)</p>

Can't have PyObject without PyTypeObject, vice versa

Truth of "everything is an object" remains even in C

All object types are extensions of this type.
https://docs.python.org/3/c-api/structures.html#c.PyObject

PyTypeObject: The C structure of the objects used to describe built-in types.
https://docs.python.org/3/c-api/type.html#c.PyTypeObject

c`PyType_Type` == py`type`

https://docs.python.org/3/c-api/typeobj.html

This is the very definition of an implementation detail
-->

---
layout: quote
---

<h1 style="position: relative; right: -3%; color: #376496; text-shadow: black -1.5px -1.5px; margin: 0; line-height: 0.8em;">
  Programming is
</h1>
<img src="/images/python-logo.png" style="height: 100px; margin-left: auto; margin-right: auto;">
<h1 style="position: relative; left: 53%; color: #fce664; text-shadow: black 1.5px 1.5px; margin: 0; line-height: 0.1em;">
  full of dualities
</h1>

<!--
I think I was asking the wrong question.

Mental flexibility; Paradoxes; bootstrap;

Python is interpreted and compiled

programs are data and instrutions

classes and instances aren't either or

Python3 or Python2 code?
-->

---
layout: intro
class: text-center
---

# Thanks

<!--
Bonus: bottom type

object() instance
-->