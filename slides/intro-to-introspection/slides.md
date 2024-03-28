---
theme: purplin
highlighter: shiki
lineNumbers: false
colorSchema: 'light'
drawings:
  persist: false
transition: slide-left
title: Intro to Introspection
layout: image
class: text-center
image: https://images.unsplash.com/photo-1600201319330-e99245e614c5
---
<!-- https://unsplash.com/photos/person-in-blue-jacket-standing-on-brown-rock-formation-during-daytime-6i3O_w7wOyE -->

<p style="position: relative; bottom: 30%">
  <h1 style="color: #F8F8F0;font-size: 5.5rem; font-weight: 700">
    Intro to Introspection
  </h1>
</p>

<style>
div {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

---
layout: image
image: https://images.unsplash.com/photo-1600201319330-e99245e614c5
---

# Introspection
## Exploring your code at runtime

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1600201319330-e99245e614c5
---

# Essential Questions
## What's available
## What is it
## What does it have

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- identify; inheritance; composition -->

---
layout: image
image: https://images.unsplash.com/photo-1517239320384-e08ad2c24a3e
---

# In a Strange Environment

<br/>
<v-click>
```python
>>> 
```
</v-click>

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- how do you explore this new space? -->

---
layout: image
image: https://images.unsplash.com/photo-1517239320384-e08ad2c24a3e
---

````md magic-move
```python
>>> locals()
```
```python {*|7|10}
>>> locals()
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <_frozen_importlib_external.SourceFileLoader
                object at 0x101c99ca0>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'shy': ⣀⡠⠔⠊⠉⠑⠢⢄⣀⡠⠔⠊⠉⠑⠢}
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- look around: what's there? not much. dir() vars() locals() globals() -->

---
layout: image
image: https://images.unsplash.com/photo-1517239320384-e08ad2c24a3e
---

````md magic-move
```python
>>> type(shy)
```
```python
>>> type(shy)
<class '__main__.Unknown'>
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- Identify objects of interest. So it is an instance of a class -->

---
layout: image
image: https://images.unsplash.com/photo-1517239320384-e08ad2c24a3e
---

````md magic-move
```python
>>> dir(shy)
```
```python
>>> dir(shy)
['hint']
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
"Call me but I won't respond to those that don't know me"
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
"Call me but I won't respond to those that don't know me"
>>> callable(shy)
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
"Call me but I won't respond to those that don't know me"
>>> callable(shy)
True
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
"Call me but I won't respond to those that don't know me"
>>> callable(shy)
True
>>> shy()
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
"Call me but I won't respond to those that don't know me"
>>> callable(shy)
True
>>> shy()
>>>
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- investigate -->

---
layout: image
image: https://images.unsplash.com/photo-1631641551473-fbe46919289d
---
<!-- https://images.unsplash.com/photo-1510256506868-484d0db06ee2 -->

# Exploring Deeper

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- Using the inspect module -->

---
layout: image
image: https://images.unsplash.com/photo-1631641551473-fbe46919289d
---

````md magic-move
```python
>>> import inspect
```
```python
>>> import inspect
>>> inspect.getmembers(shy)
```
```python
>>> import inspect
>>> inspect.getmembers(shy)
[('hint', "Call me but I won't respond to those that don't know me")]
```
```python
>>> import inspect
>>> inspect.getmembers(shy)
[('hint', "Call me but I won't respond to those that don't know me")]
>>> inspect.getdoc(shy)
```
```python
>>> import inspect
>>> inspect.getmembers(shy)
[('hint', "Call me but I won't respond to those that don't know me")]
>>> inspect.getdoc(shy)
'Some class of unknown purpose.'
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
maybe not surprising batteries-included includes an introspection module
investigate again. Same and more info
-->

---
layout: image
image: https://images.unsplash.com/photo-1631641551473-fbe46919289d
---

````md magic-move
```python
>>> inspect.getmro(type(shy))
```
```python
>>> inspect.getmro(type(shy))
(<class '__main__.Unknown'>,
 <class '__main__.Enigma'>,
 <class '__main__.Mystery'>,
 <class '__main__.Riddle'>,
 <class 'object'>)
```
```python
>>> dir(type(shy))
```
```python
>>> dir(type(shy))
['__call__', '__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', 'key', 'machine', 'message', 'solve']
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
Identify beyond the immediate type
-->

---
layout: image
image: https://images.unsplash.com/photo-1631641551473-fbe46919289d
---

````md magic-move
```python
>>> inspect.signature(shy)
```
```python
>>> inspect.signature(shy)
<Signature (
  unlock: bool = False,
  message: str = '',
  key: ~Key = None,
  machine: Callabl[str, ~Key], Optional[str]] =
    <function <lambda> at 0x102f7ef70>
 ) -> Optional[str]>
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1631641551473-fbe46919289d
---

````md magic-move
```python
>>> shy()
```
```python
>>> shy()
>>> shy(False)
```
```python
>>> shy()
>>> shy(False)
''
```
```python
>>> shy()
>>> shy(False)
''
>>> shy(False, "hello")
```
```python
>>> shy()
>>> shy(False)
''
>>> shy(False, "hello")
''
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1631641551473-fbe46919289d
---


````md magic-move
```python
>>> shy(False, shy.message, shy.key, shy.machine)
```
```python
>>> shy(False, shy.message, shy.key, shy.machine)
'greetings from the unknown'
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

# Striking Out on Your Own

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- inspect?.. just some python code -->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

# Introspection Axioms
## Names Resolve from Inner- to Outer-Most Scope
## Everything is an Object
## Attribute Lookup is Based on Inheritance

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

# Scope Resolution
## Names are Resolved in LEGB Order
- <u><b>L</b></u>ocal
- <u><b>E</b></u>nclosing
- <u><b>G</b></u>lobal
- <u><b>B</b></u>uiltin

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

````md magic-move
```python
>>> locals()
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <_frozen_importlib_external.SourceFileLoader
                object at 0x101c99ca0>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'shy': ⣀⡠⠔⠊⠉⠑⠢⢄⣀⡠⠔⠊⠉⠑⠢}
```
```python
>>> 'locals' in locals()
```
```python
>>> 'locals' in locals()
False
```
```python
>>> 'locals' in globals()
False
```
```python
>>> hasattr(__builtins__, 'locals')
True
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- if you want to inspect something you have to be able to identify it -->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

# Everything is an Object
## Objects Contain Attributes
## Attribute retrieval is really a dict lookup
## Special Info Kept in Special Attributes
- [docs.python.org/reference/datamodel](https://docs.python.org/3/reference/datamodel.html)

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
putting a '.' after a thing is always valid - the lookup might not exist
namespaces are a dicts wearing a mask. syntactic sugar
Data Model is your map when introspecting. You may know 'magic' or 'dunder'
-->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

````md magic-move
```python
>>> __builtins__.locals
<built-in function locals>
```
```python
>>> __builtins__.__dict__['locals']
<built-in function locals>
```
```python
>>> __dict__
```
```python
>>> __dict__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '__dict__' is not defined. Did you mean: '__doc__'?
```
```python
>>> import sys
```
```python
>>> import sys
>>> sys.modules[__name__].__dict__
```
```python
>>> import sys
>>> sys.modules[__name__].__dict__
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <_frozen_importlib_external.SourceFileLoader
                object at 0x101c99ca0>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'shy': ⣀⡠⠔⠊⠉⠑⠢⢄⣀⡠⠔⠊⠉⠑⠢,
 'sys': <module 'sys' (built-in)>}
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- https://docs.python.org/3/reference/datamodel.html -->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

# Attribute Lookup
## Check Current Instance
## Check Current Class
## Check All Parent Classes in MRO
- <u><b>M</b></u>ethod
- <u><b>R</b></u>esolution
- <u><b>O</b></u>rder

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

````md magic-move
```python
>>> inspect.getmembers(shy)
[('hint', "Call me but I won't respond to those that don't know me")]
```
```python
>>> shy.__dict__
```
```python
>>> shy.__dict__
{'key': slice(None, None, -1),
 'message': 'nwonknu eht morf sgniteerg',
 'hint': "call me but I won't respond to those that don't know me",
 'machine': <built-in functon getitem>}
```
```python
>>> [n for n in shy.__dict__.keys()]
['key', 'message', 'hint', 'machine']
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

````md magic-move
```python
>>> dir(type(shy))
['__call__', '__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', 'key', 'machine', 'message', 'solve']
```
```python
>>> shy.__class__
```
```python
>>> shy.__class__
<class '__main__.Unknown'>
```
```python
>>> shy.__class__.__dict__
```
```python
>>> shy.__class__.__dict__
mappingproxy({'__module__': '__main__',
  '__doc__': 'Some class of unknown purpose.',
  '__init__': <function Unknown __init__ at 0x104c8dbc0>,
  '__dir__': <function Unknown.__dir__ at 0x104c8dc60>,
  '__call__': <function Unknown.__call__ at 0x104c8dd00>})
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

````md magic-move
```python
>>> dir(type(shy))
['__call__', '__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', 'key', 'machine', 'message', 'solve']
```
```python
>>> shy.__class__.__mro__
```
```python
>>> shy.__class__.__mro__
(<class '__main__.Unknown'>,
 <class '__main__.Enigma'>,
 <class '__main__.Mystery'>,
 <class '__main__.Riddle'>,
 <class 'object'>)
```
```python
>>> [
  n
  for cls in shy.__class__.__mro__
  for n in cls.__dict__.keys()
]
['__module__', '__doc__', '__init__', '__dir__', '__call__', '__bool__', '__getitem__',
 '__module__', 'machine', '__init__', '__doc__', '__module__', 'message', '__repr__', 
 '__dict__', '__weakref__', '__doc__', '__module__', 'key', '__init__', '__dict__',
 '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__',
 '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__',
 '__init__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__',
 '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', '__doc__']
```
```python
>>> sorted({
  n
  for cls in shy.__class__.__mro__
  for n in cls.__dict__.keys()
})
['__bool__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',  '__str__',
 '__subclasshook__', '__weakref__', 'key', 'machine', 'message']
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

```python
>>> inspect.signature(shy)
<Signature (
  unlock: bool = False,
  message: str = '',
  key: ~Key = None,
  machine: Callabl[str, ~Key], Optional[str]] =
    <function <lambda> at 0x102f7ef70>
 ) -> Optional[str]>
```
````md magic-move {at:1}
```python
>>>
```
```python
>>> shy.__class__.__call__
<function Unknown.__call__ at 0x109271da0>
```
```python
>>> shy.__class__.__call__.__code__
<code object __call__ at 0x108ff18b0, file "./unknown.py", line 45>
```
```python
>>> shy.__class__.__call__.__code__.co_varnames
('self', 'unlock', 'message', 'key', 'machine')
```
```python
>>> shy.__class__.__call__.__defaults__
(False, '', None, <function <lambda> at 0x1049c9f80>)
```
```python
>>> shy.__class__.__call__.__annotations__
{'unlock': <class 'bool'>,
 'message': <class 'str'>,
 'key': ~Key,
 'machine': typing.Callable[[str, ~Key], typing.Optional[str]],
 'return': typing.Optional[str]}
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1422452098470-722310d3ad74
---

# General Introspection

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- now we have seen how inspect can shine light on you code, you can take the same approach to answer questions about your code no one else has asked before -->

---
layout: image
image: https://images.unsplash.com/photo-1422452098470-722310d3ad74
---

````md magic-move {at:1}
```python
>>> def indexable(obj):
...     return (hasattr(obj, "__getitem__")
             or hasattr(obj, "__class_getitem__"))
... 
```
```python
>>> indexable(shy)
```
```python
>>> indexable(shy)
True
```
```python
>>> shy[shy.key]
>>>
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- not __index__. Important to keep the data-model guide close as you explore on your own -->

---
layout: image
image: https://images.unsplash.com/photo-1422452098470-722310d3ad74
---

# Review
## What's Available
- LEGB
## What is it
- <code style="color: var(--prism-function)">type<span style="color: var(--prism-punctuation)">()</span></code> is the object's <code style="color: var(--prism-property)">\_\_class\_\_</code>
## What does it have
- objects' attributes are a dict lookup in <code style="color: var(--prism-property)">\_\_dict\_\_</code>

<style>
  .slidev-layout h2 {
    margin-top: 0.25em;
  }
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- 3 core questions to ask of your code -->

---
layout: image
image: https://images.unsplash.com/photo-1422452098470-722310d3ad74
---

# Review
## built-in Namespace Contains Introspection Tools
- <code style="color: var(--prism-function)">help<span style="color: var(--prism-punctuation)">()</span></code> is a super powerful use of introspection
## Use the <code style="color: var(--prism-foreground)">inspect</code> Module for More Power
- Access to an Object's Magic Methods
- Takes Care of MRO and Edge Cases for You
## Extract Info from an Object with the Data Model

<style>
  .slidev-layout h2 {
    margin-top: 0.25em;
  }
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- 1/5 of builtins can be used for introspection -->

---
layout: image
class: text-center
image: https://images.unsplash.com/photo-1422452098470-722310d3ad74
---

<p style="position: relative; bottom: 30%">
  <h1 style="color: #F8F8F0;font-size: 5.5rem; font-weight: 700">
    Thanks!
  </h1>
</p>

<style>
div {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
class: text-center
image: https://images.unsplash.com/photo-1516825295207-81549bdd014c
---

<p style="position: relative; bottom: 30%">
  <h1 style="color: #F8F8F0;font-size: 5.5rem; font-weight: 700">
    Spoilers!
  </h1>
</p>

<style>
div {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1516825295207-81549bdd014c
---

````md magic-move
```python
>>> shy(shy, shy, shy, shy.machine)
42
```
```python
>>> shy.machine
<built-in function getitem>
```
```python
>>> shy.machine
<built-in function getitem>
>>> inspect.getdoc(shy.machine)
'Same as a[b].'
```
```python
>>> shy(shy, shy, shy, shy.machine)
42
```
```python
>>> shy[shy]
42
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- shy(...) can be 'factored out' to shy[shy] -->