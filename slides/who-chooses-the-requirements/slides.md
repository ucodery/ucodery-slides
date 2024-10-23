---
theme: purplin
highlighter: shiki
lineNumbers: false
colorSchema: light
drawings:
  persist: false
transition: slide-left
title: Who Chooses the Requirements
layout: intro
class: text-center
---

# Who Chooses the Requirements

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

---

# What Are Requirements
- code the project depends on that it does not own

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
resources generally, code, exists outside the project

used by the project to complete a task

also: dependencies
-->

---

# Where Are Requirements Recorded
- in code

<v-click>

```python
import more_itertools.more
```

</v-click>

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
as: include, import, require, use

but not of project-owned files

or in the built artifact
-->

---

# Who Chooses the Requirements
- author

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
or compiler help

not 2 min talk. not my answer

not the kind of requirement I am talking about. require new definition
-->

---

# What Are Requirements
- explicit annotating of linked code projects
- required to colocate with the final artifact
- combined with comatibility ranges

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
think at the project level

when in that project's history it is of use to this project

A range of what? versions mostly. When can they inner-operate
-->

---
layout: two-cols-header
---

# What Are Requirements

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>


::left::

```nushell
more-itertools>=10.1,<12
```

```nushell
more-itertools
```

```nushell
more-itertools<10.1,!=3,>12
```

::right::

```nushell
more-itertools>10.1
```

```nushell
more-itertools==10.1
```

<!-- center colums in page -->
<style>
  .slidev-layout {
    grid-template-rows: repeat(3, 1fr);
  }
</style>

<!--
Really all project requirements reflect some range - even without an op

no way to know how many discrete versions a range contains
-->

---

# Where Are Requirements Recorded
- in project configuration

<v-click>

```toml
# pyproject.toml
dependencies = ["more-itertools"]
```

</v-click>

<v-click>

- in external configuration

</v-click>

<v-click>

```yaml
# meta.yaml
requirements:
  run:
    - more-itertools
```

</v-click>

  <BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
    <Item text="@ucodery"><carbon:logo-github /></Item>
    <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
  </BarBottom>

---

# Who Chooses the Requirements
- maintainer
  - project
  - distro, repackager

  <BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
    <Item text="@ucodery"><carbon:logo-github /></Item>
    <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
  </BarBottom>

<!--
this seem to answer the question: Who chooses?

not the kind of requirement I am talking about
-->

---

# What Are Requirements
- resources the project depends on but does not control
- that are necessary and avalible to complete a task

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
expanded beyond just code

intentionally vague. Different types of tasks. Different types of resources

"requirements" as an idea has to fit around many distinct workflows

run/build/test
-->

---

# What Are Requirements

<v-click>

- Executing the `asciinema` program requires `python`

</v-click>

<v-click>

- Building the `asciinema` package requires `python`, `setuptools`, `wheel`, and `build`

</v-click>

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
library needs to be loaded from a file to complete program execution

run/build/test

really always _runtime_ depeding on what task is currently being run
-->

---

# When Are Requirements Resolved
- building: statically linking
- bundling: locking or vendoring
- executing: dynamic loading

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
no longer recorded, realized in the moment

at no point is installing/ uploading/ package management/ env isolation/ containerizing THE deciding resolver

--editable

was focusing on configuration records
so no change to _where_

1. on the author's machine
2. on the author's machine
3. on the user's machine

Where does the range of compatibility collapse to a point-in-time loadable resource?
-->

---
transition: view-transition
---

# Who Chooses the Requirements
- building: compiler
- bundling: solver
- executing: runner

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
(some) build tool selects which of many local versions to build against

install tool may be responsible for deploying multiple software projects
doesn't have to match what was built against

purpose-built tool for isolating requirements (and SAT solving)
-->

---
transition: view-transition
---

# Who Chooses the Requirements
- building: maintainer
- bundling: maintainer
- executing: user

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
not the tools. The person executing the tool (task)
wrong way to look at it. not looking as _current_ task

so then who picks the version used?
-->

---

# Who Chooses the Requirements
- building: user
- bundling: user
- executing: user

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
THIS is Who

what if user upgrades requirements on system _after_ installing the software?
-->

---

# Code Requirements
```python
import more_itertools.more
```

# Project Requirements
```nushell
more-itertools >= 10.0
```

# Execution Requirement
```nix
.../site-packages/more_itertools/more.py
```

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
1. imports/includes
abstract ideal

2. records/metadata
practical resource locacor

3. what is actually avalible/used
acutalized implementation

distinct, not disjointed, definitions

maitainers/authors do set the record, but don't choose the final resources

leaves it up to user to resolve the proj req to sth real

authors have as much say over exec reqs as any other user; and no more say
-->

---

# What Can You Do As a Maintainer
- provide hints as to what works
- provide warnings about what does not work

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
Help your user select what will work, but don't dictate to them. You can't anticipate all their needs

if a user needs to, they will use a req with or without your approval

not adding a range is still a decision - on that impacts installers

statically link/ vendor *I suppose* (still doesn't give you complete control)

either way, you don't have the last word
-->

---

# Guiderails, not Guarantees
- ## Overly Restrictive Ranges
  - based on known unknowns
  - based on unknown unknowns
  - immutable part of project release

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
represents intent on author's side. But does NOT make the final decision

disuades users from using new versions

don't put barriers around what worked for you only (what you could MAKE work; what you TOOK TIME to check)

author does not know the constrains their users must work under

some of these are attempts to remove choices by users (runners)

can be nice, can reduce errors; can equally make fixing bad requirements terrible

none of these can aboslutly remove the users' autonomy
it only makes it harder

Once committed in the version, there is no fix to overrestriction
-->

---

# Guiderails, not Guarantees
- ## Lockfiles
  - provides tight coupling _when the used by maintainer and installer_

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--

 ---
disabled: true
 ---

# Why Update Requirements
- new features
- better performance, speed/ reliability/ less memory
- fix bugs, CVEs
- incompatibility with other requirements
- previous version no longer available

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
Which of these does the author care about?

the maintainers?

the final user?

I say update, but in some cases may want to downgrade

non-author is probably not looking to add whole new requirements
-->

<!--last slide's notes-->
<!--
both sides have to buy into the premise/ value

great solution when you are both personas

nothing about lockfiles _forces_ the user to follow them

lockfiles can break, not cover all systems, users forced to work around them anyway
-->

---
layout: intro
class: text-center
---

# You Choose the Requirements of Every Task You Run

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>

<!--
It's good, actually, that the final user of software can change this.

autonomy over your system, to complete your task

you know your needs best, even if you don't often override the guiderails
-->

---
layout: intro
class: text-center
---

# Thanks

<BarBottom  color="#F8F8F0" bg="#363f36" title="slides.ucodery.com/who-chooses-the-requirements">
  <Item text="@ucodery"><carbon:logo-github /></Item>
  <Item text="@ucodery@fosstodon.org"><carbon:logo-mastodon /></Item>
</BarBottom>
