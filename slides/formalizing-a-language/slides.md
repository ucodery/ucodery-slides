---
theme: purplin
highlighter: shiki
lineNumbers: false
colorSchema: 'light'
drawings:
  persist: false
transition: slide-left
title: Formalizing a Language
layout: image
class: text-center
image: https://images.unsplash.com/photo-1515325915697-9279b4f7effc
---

<!-- https://images.unsplash.com/photo-1515325915697-9279b4f7effc -->

<p>
<h1 style="color: #F8F8F0;font-size: 5rem; font-weight: 700;">Formalizing a Language</h1>
<br/>
<h2 style="color: #F8F8F0;font-size: 2.5rem; font-weight: 300;">giving structure to raw text</h2>
</p>

<style>
div {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

---
layout: intro
---

# Python Language

- ## Written communication
- ## Letters form words
- ## Words form sentences

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# Python Language

- ## Written communication
- ## Letters form words
    - `def` `and` `os` `__init__`
    - `120` `"Python Language"` `3.14`
    - `==` `@` `//=`
- ## Words form sentences

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# Python Language

- ## Written communication
- ## Letters form words
- ## Words form sentences
    - ```python
      import numpy as np
      ```
    - ```python
      if seconds_since_ping() * 60 >= KEEP_ALIVE:
      ```

<style>
code {
  font-size: 1.5em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# Comprehending Python

```python
        up = requests.get("https://status.python.org")
```

- ## Python is read by humans
- ## Parsed similar to a natural language

<style>
code {
  font-size: 1.75em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

<!--
Code is read more often than it is read

 up equals requests dot get https status dot python dot org
-->

---
layout: intro
---

# Comprehending Python

```python
        up = requests.get("https://status.python.org")
```

- ## Python is read by computers
- ## Parsed into a syntax tree

<style>
code {
  font-size: 1.75em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

<!--
Code is read more often - by whom? computers
-->

---
layout: center
---

```mermaid {theme: 'base', themeVariables: {primaryColor: '#960050', primaryTextColor: '#F8F8F0'}, scale: 0.85}
flowchart TD
  A([Assign])
  B([Targets])
  C(NAME='up')
  D([Value])
  E([Call])
  F([Func])
  G([Attribute])
  I(NAME='requests')
  J([Value])
  K(NAME='get')
  L([Args])
  M("Constant=#quot;'https://status.python.org'#quot;")

  style A fill:#960050
  style B fill:#960050
  style C fill:#960050
  style D fill:#960050
  style E fill:#960050
  style F fill:#960050
  style G fill:#960050
  style I fill:#960050
  style J fill:#960050
  style K fill:#960050
  style L fill:#960050
  style M fill:#960050

  A-->B
  A-->D
  B---C
  D-->E
  E-->F
  E-->L
  F-->G
  G---K
  G-->J
  J---I
  L---M
```

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
class: text-center
---

# Compiling Python

<style>
h1 {
  font-weight: 700;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# Lexing

<!--
python -m tokenize -e <(echo 'up = requests.get("https://status.python.org")')
-->

- ## Turn a stream of characters into a stream of tokens
- ## Tells the computer what the words are

<br/>


```
        'up'                           NAME
        '='                            EQUAL
        'requests'                     NAME
        '.'                            DOT
        'get'                          NAME
        '('                            LPAR
        '"https://status.python.org"'  STRING
        ')'                            RPAR
        '\n'                           NEWLINE
```

<style>
code {
  font-size: 1.5em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

<!--
whitespace is not (usually) turned into a token
-->

---
layout: intro
---

# Parsing

<!--
python -m ast -m single <(echo 'up = requests.get("https://status.python.org")')
-->

- ## Turn a stream of tokens into a syntax tree
- ## Grammar defines the set of valid programs

<br/>

```python
        Assign(
           targets=[
              Name(id='up')],
           value=Call(
              func=Attribute(
                 value=Name(id='requests'),
                 attr='get'),
              args=[
                 Constant(value='https://status.python.org')],
              keywords=[]))
```

<style>
code {
  font-size: 1.5em;
}
</style>


<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

<!--
order between tree and line no longer lines up
parsing tells the computer about precidence
-->

---
layout: intro
---

# Assembling

<!--
python -m dis <(echo 'up = requests.get("https://status.python.org")')
-->

- ## Turn a syntax tree into bytecode
- ## Can be executed in the cpython virtual machine
- ## Can be saved as a pyc file

<br/>

```
        01100101  LOAD_NAME    (requests)
        10100000  LOAD_METHOD  (get)
        01100100  LOAD_CONST   ('https://status.python.org')
        10100001  CALL_METHOD  
        01011010  STORE_NAME   (up)
```

<style>
code {
  font-size: 1.5em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

<!--
order reflects AST bottom-up. not code order
-->

---
layout: intro
class: text-center
---

# Grammar

<style>
h1 {
  font-weight: 700;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# Formal Grammar

- ## Set of rules that define what combinations of words are valid
- ## Builds words into sentences
- ## Does not have to make sense

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

<!--
and so defines what word combos make not-this-language
build sentences into paragraphs, into essays ...
a gramatically correct program can crash
-->

---
layout: intro
---

# Formal Grammar

```python
        up = requests.get("https://status.python.org")
```

- ## Lexically valid
- ## Syntactically valid

<style>
code {
  font-size: 1.75em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# Formal Grammar

```python
        up := requests-get{"https://"++"status.python.org"}
```

- ## Lexically valid
- ## Not syntactically valid

<style>
code {
  font-size: 1.75em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# Formal Grammar

```mermaid {theme: 'neutral', themeVariables: {primaryColor: '#BFBFBF', primaryTextColor: '#F8F8F0'}, scale: 1.5}
flowchart LR
  A(TEXT)
  B(TOKENS)
  C(AST)
  D(BYTECODE)

  A-- lexing -->B
  B== parsing ==>C
  C-- assembling -->D

  linkStyle 1 stroke:#960050,color:#960050,stroke-width:3px;
```

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# Python's Grammar

- ## Parsing expression grammar (PEG)
- ## Packrat parser

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

<!--
grammar is the written rules; the parser is the program that fulfills those rules
PEG is a catagory of grammars. Python's rule implementation is unique
recusive decent parser
packrat = memoization
-->

---
layout: intro
---

# PEG's Grammar

- ## PEG is also a language
- ## Has its own syntax and rules

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# PEG Elements

- ## tokens
    - UPPERCASE NAMES
- ## keywords
    - 'quoted' "name"
- ## rules
    - lowercase names
    - ```
      rule: definition
      ```

<style>
code {
  font-size: 1.5em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

<!--
definitinos are comprised of tokens, keywords, and other rules
-->

---
layout: intro
---

# PEG Chaining

- ## match all elements
    - ```
      cheese stick
      ```
- ## match any one elements
    - ```
      cheese | banana
      ```
- ## group elements
    - ```
      cheese (stick | wheel)
      ```

<style>
code {
  font-size: 1.5em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# PEG Repetition

- ## 0 or 1 (optional)
    - ```
      [cheese stick]
      ```
    - ```
      banana?
      ```
- ## 0 or more
    - ```
      cheese*
      ```
- ## 1 or more
    - ```
      cheese+
      ```
- ## 1 or more with delimiter
    - ```
      ','.cheese
      ```
    
<style>
code {
  font-size: 1.5em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# PEG lookahead

- ## positive lookahead
    - ```
      &cheese
      ```
- ## negative lookahead
    - ```
      !cheese
      ```
- ## branch commit
    - ```
      ~ cheese
      ```

<style>
code {
  font-size: 1.5em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
class: text-center
---

# Python's Grammar

<style>
h1 {
  font-weight: 700;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|5,6}
assignment:
    | NAME ':' expression ['=' annotated_rhs]
    | ('(' single_target ')' | single_subscript_attribute_target)
        ':' expression ['=' annotated_rhs]
    | (star_targets '=')+ (yield_expr | star_expressions)
        !'=' [TYPE_COMMENT]
    | single_target augassign ~ (yield_expr | star_expressions)
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```mermaid {theme: 'base', themeVariables: {primaryColor: '#BFBFBF', primaryTextColor: '#F8F8F0'}, scale: 0.85}
flowchart TD
  A([Assign])
  B([Targets])
  C(NAME='up')
  D([Value])
  E([Call])
  F([Func])
  G([Attribute])
  I(NAME='requests')
  J([Value])
  K(NAME='get')
  L([Args])
  M("Constant=#quot;'https://status.python.org'#quot;")

  style A fill:#960050

  A-->B
  A-->D
  B---C
  D-->E
  E-->F
  E-->L
  F-->G
  G---K
  G-->J
  J---I
  L---M
```

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|2}
star_targets:
    | star_target !','
    | star_target (',' star_target )* [',']
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|3}
star_target:
    | '*' (!'*' star_target)
    | target_with_star_atom
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|4}
target_with_star_atom:
    | t_primary '.' NAME !t_lookahead
    | t_primary '[' slices ']' !t_lookahead
    | star_atom
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|2}
star_atom:
    | NAME
    | '(' target_with_star_atom ')'
    | '(' [star_targets_tuple_seq] ')'
    | '[' [star_targets_list_seq] ']'
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```mermaid {theme: 'base', themeVariables: {primaryColor: '#BFBFBF', primaryTextColor: '#F8F8F0'}, scale: 0.85}
flowchart TD
  A([Assign])
  B([Targets])
  C(NAME='up')
  D([Value])
  E([Call])
  F([Func])
  G([Attribute])
  I(NAME='requests')
  J([Value])
  K(NAME='get')
  L([Args])
  M("Constant=#quot;'https://status.python.org'#quot;")

  style B fill:#960050
  style C fill:#960050

  A-->B
  A-->D
  B---C
  D-->E
  E-->F
  E-->L
  F-->G
  G---K
  G-->J
  J---I
  L---M
```

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|4}
star_expressions:
    | star_expression (',' star_expression)+ [',']
    | star_expression ','
    | star_expression
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl
star_expression -> expression -> disjunction ->
conjunction -> inversion -> comparison ->
bitwise_or -> bitwise_xor -> bitwise_and ->
shift_expr -> sum -> term -> factor -> power ->
await_primary -> primary
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|4}
primary:
    | primary '.' NAME
    | primary genexp
    | primary '(' [arguments] ')'
    | primary '[' slices ']'
    | atom
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```mermaid {theme: 'base', themeVariables: {primaryColor: '#BFBFBF', primaryTextColor: '#F8F8F0'}, scale: 0.85}
flowchart TD
  A([Assign])
  B([Targets])
  C(NAME='up')
  D([Value])
  E([Call])
  F([Func])
  G([Attribute])
  I(NAME='requests')
  J([Value])
  K(NAME='get')
  L([Args])
  M("Constant=#quot;'https://status.python.org'#quot;")

  style D fill:#960050
  style E fill:#960050

  A-->B
  A-->D
  B---C
  D-->E
  E-->F
  E-->L
  F-->G
  G---K
  G-->J
  J---I
  L---M
```

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|2|6}
primary:
    | primary '.' NAME
    | primary genexp
    | primary '(' [arguments] ')'
    | primary '[' slices ']'
    | atom
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|2}
atom:
    | NAME
    | 'True'
    | 'False'
    | 'None'
    | &STRING strings
    | NUMBER
    | &'(' (tuple | group | genexp)
    | &'[' (list | listcomp)
    | &'{' (dict | set | dictcomp | setcomp)
    | '...'
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```mermaid {theme: 'base', themeVariables: {primaryColor: '#BFBFBF', primaryTextColor: '#F8F8F0'}, scale: 0.85}
flowchart TD
  A([Assign])
  B([Targets])
  C(NAME='up')
  D([Value])
  E([Call])
  F([Func])
  G([Attribute])
  I(NAME='requests')
  J([Value])
  K(NAME='get')
  L([Args])
  M("Constant=#quot;'https://status.python.org'#quot;")

  style F fill:#960050
  style G fill:#960050
  style I fill:#960050
  style J fill:#960050
  style K fill:#960050

  A-->B
  A-->D
  B---C
  D-->E
  E-->F
  E-->L
  F-->G
  G---K
  G-->J
  J---I
  L---M
```

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl
arguments: args [','] &')'
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|2-4}
args:
    | ','.(starred_expression
        | ( assignment_expression
          | expression !':=') !'=')+ [',' kwargs]
    | kwargs
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl {all|6}
atom:
    | NAME
    | 'True'
    | 'False'
    | 'None'
    | &STRING strings
    | NUMBER
    | &'(' (tuple | group | genexp)
    | &'[' (list | listcomp)
    | &'{' (dict | set | dictcomp | setcomp)
    | '...'
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```perl
strings: STRING+
```

<style>
code {
  font-size: 1.9em;
  line-height: 1.25;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: center
---

```mermaid {theme: 'base', themeVariables: {primaryColor: '#BFBFBF', primaryTextColor: '#F8F8F0'}, scale: 0.85}
flowchart TD
  A([Assign])
  B([Targets])
  C(NAME='up')
  D([Value])
  E([Call])
  F([Func])
  G([Attribute])
  I(NAME='requests')
  J([Value])
  K(NAME='get')
  L([Args])
  M("Constant=#quot;'https://status.python.org'#quot;")

  style L fill:#960050
  style M fill:#960050

  A-->B
  A-->D
  B---C
  D-->E
  E-->F
  E-->L
  F-->G
  G---K
  G-->J
  J---I
  L---M
```

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: intro
---

# Review

- ## Grammar alone defines what is correct syntax
    - And so also syntax errors
- ## Parser generates AST directly from tokens following the grammar
    - Rule recursion structurally matches the syntax tree
    - Syntax tree order informs the bytecode order

<style>
li {
  font-size: 1.1em;
}
</style>

<BarBottom  color="#F8F8F0" bg="#282634" title="Formalizing a Language">
  <Item text="@ucodery">
    <carbon:logo-github />
  </Item>
  <Item text="@ucodery@fosstodon.org">
    <carbon:logo-mastodon />
  </Item>
</BarBottom>

---
layout: image
class: text-center
image: https://images.unsplash.com/photo-1515325915697-9279b4f7effc
---

<h1 style="color: #F8F8F0;font-size: 5rem; font-weight: 700;">Thanks!</h1>

<style>
div {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
