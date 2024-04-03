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

<!--
asked "what is introspection?"

exploring code at runtime

simply: asking questions and getting answers about running code without source
-->

---
layout: image
image: https://images.unsplash.com/photo-1600201319330-e99245e614c5
---

<div class="grid grid-cols-2 w-full h-full auto-rows-fr">
  <div class="slidev-layout repadh1">
    <h1>Essential Questions</h1>
  </div>
  <div class="slidev-layout ii-content repadh2 default slidev-page" style="background-color: rgb(24 20 18 / 92%)">
    <h2>What's Available</h2>
    <h2>What Is It</h2>
    <h2>What Does It Have</h2>
  </div>
</div>

<style>
  .slidev-layout {
    padding: 0;
  }
  .slidev-layout .repadh1 {
    padding: 3rem;
  }
  .slidev-layout .repadh2 {
    padding: 2.5rem;
  }
</style>

<BarBottom  color="#F8F8F0" bg="#131218" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
identify
fundamental q inheritance
fundamental = composition
-->

---
layout: image
image: https://images.unsplash.com/photo-1517239320384-e08ad2c24a3e
---

# In a Strange Environment

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
how do you explore this new space?

what's the purpose of the program under execution?
-->

---
layout: image
image: https://images.unsplash.com/photo-1517239320384-e08ad2c24a3e
---

````md magic-move
```python
>>> 
```
```python
>>> locals()
```
```python
>>> locals()
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <_frozen_importlib_external.SourceFileLoader
                object at 0x101876390>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'shy': ⣀⡠⠔⠊⠉⠑⠢⢄⣀⡠⠔⠊⠉⠑⠢⢄}
>>> 
```
```python {*|7|10}
>>> globals()
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <_frozen_importlib_external.SourceFileLoader
                object at 0x101876390>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'shy': ⣀⡠⠔⠊⠉⠑⠢⢄⣀⡠⠔⠊⠉⠑⠢⢄}
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
look around: what's there? not much.

if \_\_name\_\_ == '\_\_main\_\_':
-->

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
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
Identify objects of interest.

So it is an instance of a class
-->

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
>>> 
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
'Call me maybe'
>>> 
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
'Call me maybe'
>>> callable(shy)
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
'Call me maybe'
>>> callable(shy)
True
>>> 
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
'Call me maybe'
>>> callable(shy)
True
>>> shy()
```
```python
>>> dir(shy)
['hint']
>>> shy.hint
'Call me maybe'
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

<!--
investigate

TypeError: 'int' object is not callable
-->

---
layout: image
image: https://images.unsplash.com/photo-1631641551473-fbe46919289d
---

# Exploring Deeper

<BarBottom  color="#F8F8F0" bg="#271307" title="slides.ucodery.com/intro-to-introspection">
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
>>> 
```
```python
>>> import inspect
>>> type(shy)
<class '__main__.Unknown'>
>>> 
```
```python
>>> import inspect
>>> inspect.getmro(type(shy))
```
```python
>>> import inspect
>>> inspect.getmro(type(shy))
(<class '__main__.Unknown'>,
 <class '__main__.Enigma'>,
 <class '__main__.Mystery'>,
 <class '__main__.Riddle'>,
 <class 'object'>)
>>> 
```
````
<BarBottom  color="#F8F8F0" bg="#271307" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
batteries-included includes introspection

Identify beyond the immediate type
-->

---
layout: image
image: https://images.unsplash.com/photo-1631641551473-fbe46919289d
---

````md magic-move
```python
>>> dir(shy)
['hint']
>>> 
```
```python
>>> inspect.getmembers(shy)
[('hint', 'Call me maybe')]
>>> 
```
```python
>>> inspect.getmembers(shy)
[('hint', 'Call me maybe')]
>>> inspect.getdoc(shy)
```
```python
>>> inspect.getmembers(shy)
[('hint', 'Call me maybe')]
>>> inspect.getdoc(shy)
'Some class of unknown purpose.'
>>> 
```
```python
>>> inspect.getmembers(shy)
[('hint', 'Call me maybe')]
>>> inspect.getdoc(shy)
'Some class of unknown purpose.'
>>> inspect.getmembers(type(shy))
```
```python {*|3,13,2,17,5|8}
>>> inspect.getmembers(type(shy))
[('__bool__', <function Mystery.__bool__ at 0x10d809bc0>),
 ('__call__', <function Unknown.__call__ at 0x10d809ee0>),
 ('__class__', <class 'type'>),
 ('__delattr__', <slot wrapper '__delattr__' of 'object' objects>),
 ('__dict__', {'__call__': <function Unknown.__call__ at 0x10d809ee0>, '__
 ('__dir__', <function Unknown.__dir__ at 0x10d809f80>),
 ('__doc__', 'Some class of unknown purpose.'),
 ('__eq__', <slot wrapper '__eq__' of 'object' objects>),
 ('__format__', <method '__format__' of 'object' objects>),
 ('__ge__', <slot wrapper '__ge__' of 'object' objects>),
 ('__getattribute__', <slot wrapper '__getattribute__' of 'object' objects
 ('__getitem__', <function Enigma.__getitem__ at 0x10d809d00>),
 ('__getstate__', <method '__getstate__' of 'object' objects>),
 ('__gt__', <slot wrapper '__gt__' of 'object' objects>),
 ('__hash__', <slot wrapper '__hash__' of 'object' objects>),
 ('__index__', <function Riddle.__index__ at 0x10d7afe20>),
 ('__init__', <function Unknown.__init__ at 0x10d809e40>),
 ('__init_subclass__', <built-in method __init_subclass__ of type object a
 ('__le__', <slot wrapper '__le__' of 'object' objects>),
 ('__lt__', <slot wrapper '__lt__' of 'object' objects>),
 ('__module__', '__main__'),
 ('__ne__', <slot wrapper '__ne__' of 'object' objects>),
 ('__new__', <built-in method __new__ of type object at 0x10d14f078>),
 ('__reduce__', <method '__reduce__' of 'object' objects>),
 ('__reduce_ex__', <method '__reduce_ex__' of 'object' objects>),
 ('__repr__', <function Mystery.__repr__ at 0x10d7af1a0>),
 ('__setattr__', <slot wrapper '__setattr__' of 'object' objects>),
 ('__sizeof__', <method '__sizeof__' of 'object' objects>),
 ('__str__', <slot wrapper '__str__' of 'object' objects>),
 ('__subclasshook__', <built-in method __subclasshook__ of type object at 
 ('__weakref__', <attribute '__weakref__' of 'Mystery' objects>),
 ('key', '2'),
 ('machine', <built-in function add>),
 ('message', '4')]
>>> 
```
```python
>>> [n for n, _ in inspect.getmembers(type(shy))]
['__bool__', '__call__', '__class__', '__delattr__', '__dict__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getstate__', '__gt__',
 '__hash__', '__index__', '__init__', '__init_subclass__', '__le__',
 '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', 'key', 'machine', 'message']
```
````

<BarBottom  color="#F8F8F0" bg="#271307" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
investigate again. Same and more info
-->

---
layout: image
image: https://images.unsplash.com/photo-1631641551473-fbe46919289d
---

````md magic-move
```python
>>> callable(shy)
True
>>> 
```
```python
>>> inspect.signature(shy)
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> 
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy()
>>> 
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy(False)
''
>>> 
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy(False, 'hello')
''
>>> 
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy(False, shy.message, shy.key, shy.machine)
'greetings from the unknown'
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#271307" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- signagure is a super power -->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

# Striking Out on Your Own

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
inspect?.. just some python code

if we figure out its tricks we can come up with our own
-->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

<div class="grid grid-cols-2 w-full h-full auto-rows-fr">
  <div class="slidev-layout repadh1">
    <h1>Introspection Axioms</h1>
  </div>
  <div class="slidev-layout ii-content repadh2 default slidev-page" style="background-color: rgb(65 25 19 / 92%)">
    <h2>Names Resolve Inner- to Outer-Most Scope</h2>
    <h2>Everything Is an Object</h2>
    <h2>Attribute Lookup Is Based on Inheritance</h2>
  </div>
</div>

<style>
  .slidev-layout {
    padding: 0;
  }
  .slidev-layout .repadh1 {
    padding: 3rem;
  }
  .slidev-layout .repadh2 {
    padding: 2.5rem;
  }
</style>

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
no more primitive type

will allow you to ask good questions about your code
-->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

<div class="grid grid-cols-2 w-full h-full auto-rows-fr">
  <div class="slidev-layout repadh1">
    <h1>Scope Resolution</h1>
  </div>
  <div class="slidev-layout ii-content repadh2 default slidev-page" style="background-color: rgb(65 25 19 / 92%)">
    <h2>Names Resolve in LEGB Order</h2>
    <ul>
      <li><u><b>L</b></u>ocal</li>
      <li><u><b>E</b></u>nclosing</li>
      <li><u><b>G</b></u>lobal</li>
      <li><u><b>B</b></u>uiltin</li>
    </ul>
  </div>
</div>

<style>
  .slidev-layout {
    padding: 0;
  }
  .slidev-layout .repadh1 {
    padding: 3rem;
  }
  .slidev-layout .repadh2 {
    padding: 2.5rem;
  }
</style>

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
Python lexically scoped

or raise NameError
-->

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
                object at 0x101876390>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'shy': ⣀⡠⠔⠊⠉⠑⠢⢄⣀⡠⠔⠊⠉⠑⠢⢄}
>>> 
```
```python
>>> 'locals' in locals()
```
```python
>>> 'locals' in locals()
False
>>> 
```
```python
>>> 'locals' in globals()
False
>>> 
```
```python
>>> hasattr(__builtins__, 'locals')
True
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- if you want to inspect something you have to be able to identify it -->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

<div class="grid grid-cols-2 w-full h-full auto-rows-fr">
  <div class="slidev-layout repadh1">
    <h1>Everything Is an Object</h1>
  </div>
  <div class="slidev-layout ii-content repadh2 default slidev-page" style="background-color: rgb(65 25 19 / 92%)">
    <h2>Objects Have a Type</h2>
    <h2>Objects Have Attributes</h2>
    <h2>Attributes Are Kept in a Dictionary</h2>
    <h2>Special Info Kept in Special Attributes</h2>
    <ul><li><a href="https://docs.python.org/3/reference/datamodel.html" style="text-decoration:none">Data Model</a></li></ul>
  </div>
</div>

<style>
  .slidev-layout {
    padding: 0;
  }
  .slidev-layout .repadh1 {
    padding: 3rem;
  }
  .slidev-layout .repadh2 {
    padding: 2.5rem;
  }
</style>

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
putting a '.' after a thing always valid - the lookup might not exist

all objects are also namespaces

Data Model is your map when introspecting. You may know 'magic' or 'dunder'
-->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

````md magic-move
```python
>>> locals
<built-in function locals>
>>> 
```
```python
>>> __builtins__.locals
<built-in function locals>
>>> 
```
```python
>>> __builtins__.__dict__['locals']
<built-in function locals>
>>> 
```
```python
>>> __dict__
```
```python
>>> __dict__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '__dict__' is not defined. Did you mean: '__doc__'?
>>> 
```
```python
>>> import sys
>>> 
```
```python
>>> import sys
>>> sys.modules[__name__]
```
```python
>>> import sys
>>> sys.modules[__name__]
<module '__main__' (<_frozen_importlib_external.SourceFileLoader
                    object at 0x104c2e390>)>
>>> 
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
                object at 0x101876390>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'shy': ⣀⡠⠔⠊⠉⠑⠢⢄⣀⡠⠔⠊⠉⠑⠢⢄,
 'sys': <module 'sys' (built-in)>}
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
namespaces are a dicts wearing a mask. syntactic sugar

all objects are also namespaces

need to do more work than the provided tools
-->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

<div class="grid grid-cols-2 w-full h-full auto-rows-fr">
  <div class="slidev-layout repadh1">
    <h1>Attribute Lookup</h1>
  </div>
  <div class="slidev-layout ii-content repadh2 default slidev-page" style="background-color: rgb(65 25 19 / 92%)">
    <h2>Current Instance</h2>
    <h2>Current Class</h2>
    <h2>Parent Classes in MRO</h2>
      <ul>
        <li><u><b>M</b></u>ethod</li>
        <li><u><b>R</b></u>esolution</li>
        <li><u><b>O</b></u>rder</li>
      </ul>
  </div>
</div>

<style>
  .slidev-layout {
    padding: 0;
  }
  .slidev-layout .repadh1 {
    padding: 3rem;
  }
  .slidev-layout .repadh2 {
    padding: 2.5rem;
  }
</style>

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
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
[('hint', 'Call me maybe')]
>>> 
```
```python
>>> shy.__dict__
```
```python
>>> shy.__dict__
{'hint': 'Call me maybe',
 'key': slice(None, None, -1),
 'machine': <built-in function getitem>,
 'message': 'nwonknu eht morf sgniteerg'}
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

````md magic-move
```python
>>> [n for n, _ in inspect.getmembers(type(shy))]
['__bool__', '__call__', '__class__', '__delattr__', '__dict__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getstate__', '__gt__',
 '__hash__', '__index__', '__init__', '__init_subclass__', '__le__',
 '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', 'key', 'machine', 'message']
>>> 
```
```python
>>> type(shy)
<class '__main__.Unknown'>
>>>
```
```python
>>> shy.__class__
<class '__main__.Unknown'>
>>>
```
```python
>>> shy.__class__.__dict__
```
```python {*|2,3,5}
>>> shy.__class__.__dict__
{'__call__': <function Unknown.__call__ at 0x101af9ee0>,
 '__dir__': <function Unknown.__dir__ at 0x101af9f80>,
 '__doc__': 'Some class of unknown purpose.',
 '__init__': <function Unknown.__init__ at 0x101af9e40>,
 '__module__': '__main__'}
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- only methods from Unknown, not the rest of the MRO -->

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

````md magic-move
```python
>>> inspect.getmro(type(shy))
(<class '__main__.Unknown'>,
 <class '__main__.Enigma'>,
 <class '__main__.Mystery'>,
 <class '__main__.Riddle'>,
 <class 'object'>)
>>> 
```
```python
>>> shy.__class__.__mro__
(<class '__main__.Unknown'>,
 <class '__main__.Enigma'>,
 <class '__main__.Mystery'>,
 <class '__main__.Riddle'>,
 <class 'object'>)
>>> 
```
```python
>>> [n for cls in shy.__class__.__mro__
     for n in cls.__dict__.keys()]
['__module__', '__doc__', '__init__', '__call__', '__dir__', '__module__',
 'machine', '__init__', '__getitem__', '__doc__', '__module__', 'message',
 '__repr__', '__bool__', '__dict__', '__weakref__', '__doc__', '__module__
 'key', '__init__', '__index__', '__dict__', '__weakref__', '__doc__',
 '__new__', '__repr__', '__hash__', '__str__', '__getattribute__',
 '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__',
 '__gt__', '__ge__', '__init__', '__getitem__', '__doc__', '__module__',
 'message', '__repr__', '__bool__', '__dict__', '__weakref__', '__doc__',
 '__module__', 'key', '__init__', '__index__', '__dict__', '__weakref__',
 '__doc__', '__new__', '__repr__', '__hash__', '__str__',
 '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__',
 '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__',
 '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__',
 '__format__', '__sizeof__', '__dir__', '__class__', '__doc__']
>>> 
```
```python
>>> sorted({n for cls in shy.__class__.__mro__
            for n in cls.__dict__.keys()})
['__bool__', '__call__', '__class__', '__delattr__', '__dict__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getstate__', '__gt__',
 '__hash__', '__index__', '__init__', '__init_subclass__', '__le__',
 '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', 'key', 'machine', 'message']
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---
layout: image
image: https://images.unsplash.com/photo-1507707161256-bbcd7fe3359e
---

````md magic-move
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> 
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy.__class__.__call__
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy.__class__.__call__
<function Unknown.__call__ at 0x109271da0>
>>> 
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy.__class__.__call__.__code__
<code object __call__ at 0x108ff18b0, file "./unknown.py", line 57>
>>> 
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy.__class__.__call__.__code__.co_varnames
('self', 'locked', 'message', 'key', 'machine')
>>> 
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy.__class__.__call__.__defaults__
(True, '', None, <function <lambda> at 0x101a9f100>)
>>> 
```
```python
>>> inspect.signature(shy)
<Signature (
  locked: bool = True,
  message: str = '',
  key: ~Key = None,
  machine: Callable[[str, ~Key], Optional[~Answer]] =
    <function <lambda> at 0x101a9f100>
 ) -> Optional[~Answer]>
>>> shy.__class__.__call__.__annotations__
{'key': ~Key,
 'locked': <class 'bool'>,
 'machine': typing.Callable[[str, ~Key], typing.Optional[~Answer]],
 'message': <class 'str'>,
 'return': typing.Optional[~Answer]}
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#7A391E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
might think, as I, that inspect.signature is easy

it's all one line in the source

at runtime, scattered throughout the interpreter

self - when this deep, workings of python not hidden
-->

---
layout: image
image: https://images.unsplash.com/photo-1422452098470-722310d3ad74
---

# Innovative Introspection

<BarBottom  color="#F8F8F0" bg="#9A592E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
now we have seen how inspect can shine light on you code

you can take the same approach to answer questions about your code no one else has asked before
-->

---
layout: image
image: https://images.unsplash.com/photo-1422452098470-722310d3ad74
---

````md magic-move {at:1}
```python
>>> callable(shy)
True
>>> 
```
```python
>>> def indexable(obj):
...     return (hasattr(obj, "__getitem__")
...          or hasattr(obj, "__class_getitem__"))
... 
>>> 
```
```python
>>> indexable(shy)
```
```python
>>> indexable(shy)
True
>>> 
```
```python
>>> shy[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./unknown.py" line 44, in __getitem__
    raise IndexError
IndexError
>>> 
```
```python
>>> shy[shy.key]
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#9A592E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
not \_\_index\_\_. keep the data-model guide close as you explore on your own

when calling shy, it's own attributes were the key

I guess we're still learning new things about shy

might not be done with shy, but are done with this talk
-->

---
layout: image
image: https://images.unsplash.com/photo-1422452098470-722310d3ad74
---

<div class="grid grid-cols-2 w-full h-full auto-rows-fr">
  <div class="slidev-layout repadh1">
    <h1>Review</h1>
  </div>
  <div class="slidev-layout ii-content repadh2 default slidev-page" style="background-color: rgb(134 94 50 / 92%)">
    <h2>What's Available</h2>
    <ul><li>LEGB</li></ul>
    <h2>What Is It</h2>
    <ul><li><code style="color: var(--prism-function)">type<span style="color: var(--prism-punctuation)">()</span></code> Is the Object's <code style="color: var(--prism-property)">__class__</code></li></ul>
    <h2>What Does It Have</h2>
    <ul><li>Attributes in <code style="color: var(--prism-property)">__dict__</code></li></ul>
  </div>
</div>

<style>
  .slidev-layout {
    padding: 0;
  }
  .slidev-layout .repadh1 {
    padding: 3rem;
  }
  .slidev-layout .repadh2 {
    padding: 2.5rem;
  }
</style>

<BarBottom  color="#F8F8F0" bg="#9A592E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
might not be done with shy, but are done with this talk

3 core questions to ask of your code

and MRO it its lineage
-->

---
layout: image
image: https://images.unsplash.com/photo-1422452098470-722310d3ad74
---

<div class="grid grid-cols-2 w-full h-full auto-rows-fr">
  <div class="slidev-layout repadh1">
    <h1>Review</h1>
  </div>
  <div class="slidev-layout ii-content repadh2 default slidev-page" style="background-color: rgb(134 94 50 / 92%)">
    <h2>Built-In Introspection</h2>
    <ul><li><code style="color: var(--prism-function)">help<span style="color: var(--prism-punctuation)">()</span></code> Is a Powerful Use of Introspection</li></ul>
    <h2><code style="color: var(--prism-foreground)">inspect</code> Module</h2>
    <ul>
      <li>Access Magic Methods</li>
      <li>Takes Care of MRO</li>
    </ul>
    <h2>Data Model is the Map to an Object's Secrets</h2>
  </div>
</div>

<style>
  .slidev-layout {
    padding: 0;
  }
  .slidev-layout .repadh1 {
    padding: 3rem;
  }
  .slidev-layout .repadh2 {
    padding: 2.5rem;
  }
</style>

<BarBottom  color="#F8F8F0" bg="#9A592E" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
1/5 of builtins can be used for introspection

`inspect` handles edge cases for you
-->

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

<BarBottom  color="#F8F8F0" bg="#9A592E" title="slides.ucodery.com/intro-to-introspection">
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
>>> shy(shy, type(shy).message, type(shy).key, type(shy).machine)
```
```python
>>> shy(shy, type(shy).message, type(shy).key, type(shy).machine)
'42'
>>> 
```
````

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
```
```python
>>> shy(shy, shy, shy, shy.machine)
'Spanish Inquisition'
>>> 
```
```python
>>> shy.machine
<built-in function getitem>
>>> 
```
```python
>>> shy.machine
<built-in function getitem>
>>> inspect.getdoc(shy.machine)
'Same as a[b].'
>>> 
```
```python
>>> shy(shy, shy, shy, shy.machine)
'Spanish Inquisition'
>>> 
```
```python
>>> shy[shy]
'Spanish Inquisition'
>>> 
```
````

<BarBottom  color="#F8F8F0" bg="#282634" title="slides.ucodery.com/intro-to-introspection">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!-- shy(...) can be 'factored out' to shy[shy] -->
