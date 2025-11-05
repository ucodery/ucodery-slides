---
lineNumbers: false
colorSchema: light
drawings:
  persist: false
transition: slide-left
title: Tuples, They're Everywhere
layout: intro
class: text-center
---

# Tuples, They're Everywhere

---
layout: center
---

# What are tuples

<!--
immutable sequences (themselves collections) of heterogeneous data
https://docs.python.org/3/library/stdtypes.html#tuple

single, double, triple, quadruple, ...
-->

---
layout: center
---

# Making Tuples

---
layout: center
---

````md magic-move
```
tuple()
```
```
tuple()
tuple([1, 2, 3])
```
```
tuple()
tuple([1, 2, 3])
tuple(sys.version_info)
```
```
tuple()
tuple([1, 2, 3])
tuple(sys.version_info)
tuple(range(16))
```
````

<!--
built-in; actually the class, calling it makes an instance
-->

---
layout: center
---

````md magic-move
```
(0, 1, 2)
```
```
(0, 1, 2)
(0,
 1,
)
```
```
(0, 1, 2)
(0,
 1,
)
(0,)
```
```
(0, 1, 2)
(0,
 1,
)
(0,)
()
```
````

<!--
display syntax; a shortcut built in to the grammar
-->

---
layout: center
---

> Note that it is actually the comma which makes a tuple, not the parentheses.
> The parentheses are optional, except in the empty tuple case,
> or when they are needed to avoid syntactic ambiguity.
> <p style="text-align: right;">- <a href="https://docs.python.org/3/library/stdtypes.html#tuple">library/stdtypes.html</a></p>

---
layout: center
transition: view-transition
---
```
t = (0, 1, 2)
```

---
layout: center
---
```
t = 0, 1, 2
```

---
layout: center
transition: view-transition
---
```
t = (0,
1,
)
```

---
layout: center
transition: view-transition
---
```
t = 0,
1,
```

<style>
.shiki .line span {
  color: orange;
}
</style>

<!--
this is interesting. depending on surrounding syntax, this might compile ok
but it is not the same meaning

This is 2 different 1-tuples, executed as 2 different statements (or error)

Another example:
```
0, * 6
```
SyntaxError!
```
(0,) * 6
```
Ok
-->

---
layout: center
---
```
t = 0, 1,
```

---
layout: center
transition: view-transition
---
```
t = (0,)
```

---
layout: center
transition: view-transition
---
```
t = 0,
```

---
layout: center
---
```
t = (0)
```

<style>
.shiki .line span {
  color: orange;
}
</style>

---
layout: center
transition: view-transition
---
```
t = ()
```

---
layout: center
transition: view-transition
---
```
t = 
```

<style>
.shiki .line span {
  color: red;
}
</style>

---
layout: center
transition: view-transition
---
```
t = ,
```

<style>
.shiki .line span {
  color: red;
}
</style>

---
layout: center
transition: view-transition
---
```
t = (,)
```

<style>
.shiki .line span {
  color: red;
}
</style>

---
layout: center
---
```
t = ()
```

---
layout: center
---

# Simple Rules for Making Tuples
- add a `,` make a tuple
- an empty tuple requires `()`
  - no commas allowed
- add `()` to disambiguate
  - for the computer
  - for the human

<!--
can create them wherever an expression is valid

some parens are load-bearing, some are just a facade-but neither are part of the tuple definition
-->

---
layout: intro
class: text-center
---

# Pop Quiz!

<!--
only valid code examples shown
-->

---
src: ./quiz.md
---

---
layout: intro
class: text-center
---

# Time's Up

<!--
Thank you for your time

I hope you learned something in the end

If not I hope you at least had fun
-->
