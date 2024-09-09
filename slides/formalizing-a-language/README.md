# Formalizing a Language

### Summary
Python's grammar is the rules that define what is accepted as a legal program. In order for text to get executed on a CPU it is first transformed into valid instructions according to these rules. This talk will show examples of these transformations as well as grammar pulled straight from cpython source and picked apart so it is as easy to understand as Python code.

### Description

### Outline
* Introduction (2 minutes)
      * how Python is  parsed by computers and humans
* Compiling (5 minutes)
      * lexing, parsing, and assembling Python code
* Formal Grammar (4 minutes)
      * What it is generally
      * how does python specifically use grammar
* Defining a Grammar (4 minutes)
      * overview of PEG
      * how to define a formal language with another formal language
* Python's Grammar (8 minutes)
      * examples of Python grammar written out and how to read it
      * recursive descent to build a practical AST example
* Conclusion (2 minutes)
      * how grammar rules shape the language
      * even more possibilities
