---
layout: center
---

<code class="slidev-code language-text">
answer = <span v-mark="{strokeWidth: 10, color: '#339933'}">tuple()</span>
</code>

<!--YES-->

---
layout: center
---

<code class="slidev-code language-text">
answer = (<span v-mark="{strokeWidth: 10, color: '#339933'}">1, 2, 3</span>)
</code>

<!--YES-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">pow(2, 8)</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">answer = {1, 2, 3}</span>
</code>

<!--NO-->

---
layout: center
---

<code class="slidev-code language-text">
xy = "".join(<span v-mark="{strokeWidth: 10, color: '#339933'}">("x", "y")</span>)
</code>

<!--
YES

parens load-bearing
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">answer = (
"left"
"top"
"right"
"bottom"
)</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
def answer():
    return <span v-mark="{strokeWidth: 10, color: '#339933'}">1, "one"</span>
</code>
</pre>

<!--YES-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">print ()</span>
</code>
</pre>

<!--
NO

unless you are running python 2.7....
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">import os, sys</span>
</code>
</pre>

<!--
NO

import does not take arbitrary expressions, it takes names only
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
print(<span v-mark="{strokeWidth: 10, color: '#339933'}">("hello", "world", "!")</span>)
</code>
</pre>

<!--
YES

parens are load-bearing; not required to compile, but do change behaviour
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">answer = ("this")</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">from os.path import (
      join, basename
)</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
def answer():
    msg = (
      yield <span v-mark="{strokeWidth: 10, color: '#339933'}">2, "two"</span>
    )
</code>
</pre>

<!--YES-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">match Camelot:
    case (gold, white):
        return "Arthur"
    case (blue, white):
        return "Bedevere"
    case (red, green):
        return "Robin"
</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
answer = (
    ((<span v-mark="{strokeWidth: 10, color: '#339933'}">x, y</span>))
)
</code>
</pre>

<!--
YES load-bearing and couple facade
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
answer = <span v-mark="{strokeWidth: 10, color: '#339933', at: 1}">(</span>
<span v-mark="{strokeWidth: 10, color: '#339933', at: 1}">"Spam is"</span>
<span v-mark="{strokeWidth: 10, color: '#339933', at: 1}">" good for"</span>
<span v-mark="{strokeWidth: 10, color: '#339933', at: 1}">" you"</span>
<span v-mark="{strokeWidth: 10, color: '#339933', at: 1}">,)</span>
</code>
</pre>

<!--
YES load-bearing
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">(a, b, c) = range(3)</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
answer = <span v-mark="{strokeWidth: 10, color: '#339933'}">("Coconut"),</span>
</code>
</pre>

<!--
YES facade
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">world[:100, ::-1, 12:48]</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
answer = (<span v-mark="{strokeWidth: 10, color: '#339933'}">*"aei", *"ou", "y"</span>)
</code>
</pre>

<!--YES facade-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">assert sys.argv[:1], "no args"</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">answer = (c for c in "answer")</span>
</code>
</pre>

<!--
NO

This is a generator

No such thing as a tuple comprehension
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
ni = (<span v-mark="{strokeWidth: 10, color: '#339933'}">lambda a, b: a&lt;b, b&gt;a</span>)
</code>
</pre>

<!--YES-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">with (open(os.devnull) as n,
      redirect_stderr(n)):
    question()</span>
</code>
</pre>

<!--
NO

completely illegal < 3.10
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
match (<span v-mark="{strokeWidth: 10, color: '#339933'}">type(x), str(x)</span>):
    case needed:
        return True
    case _:
        return False
</code>
</pre>

<!--YES-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
assert <span v-mark="{strokeWidth: 10, color: '#339933', at: 1}">(</span>
    <span v-mark="{strokeWidth: 10, color: '#339933', at: 1}">os.getlogin() == me,</span>
    <span v-mark="{strokeWidth: 10, color: '#339933', at: 1}">"not me"</span>
<span v-mark="{strokeWidth: 10, color: '#339933', at: 1}">)</span>
</code>
</pre>

<!--YES load-bearing-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
try:
    answer = box[label]
except (<span v-mark="{strokeWidth: 10, color: '#339933'}">IndexError, KeyError</span>):
    os.exit()
</code>
</pre>

<!--
YES load-bearing

as of 3.10; before load-bearing but optional
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">l = lambda a, b: a+b</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">for a, b in zip("drm", "oei"):
    a + b</span>
</code>
</pre>

<!--NO-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
int(*<span v-mark="{strokeWidth: 10, color: '#339933'}">()</span>)
</code>
</pre>

<!--
YES

but doesn't go into int
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">def answer():
    global spam, eggs, cheese</span>
</code>
</pre>

<!--
NO

neither is nonlocal
-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
def answer(self, <span v-mark="{strokeWidth: 10, color: '#339933'}">*args</span>):
    self._answer = args
</code>
</pre>

<!--YES-->

---
layout: center
---

<pre>
<code class="slidev-code language-text">
<span v-mark="{type: 'crossed-off', strokeWidth: 10, color: 'red'}">del spam, eggs, cheese</span>
</code>
</pre>

<!--NO-->
