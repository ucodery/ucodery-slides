---
theme: default
highlighter: shiki
lineNumbers: false
colorSchema: 'light'
fonts:
  sans: PT Serif
drawings:
  persist: false
transition: slide-left
title: You Are Sharing Your Code Wrong
layout: default
class: text-center
---
<!-- https://www.flickr.com/photos/27215653@N00/3638034382 -->

<img src="/images/this-side-up.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:25%;">

# You Are Sharing Your Code Wrong
## (and what to do about it)
### Jeremiah Paige (he/him)

<style>
  h2 {
    position: relative;
    top: 35%;
  }
  h3 {
    position: relative;
    padding-top: 2rem;
    top: 35%;
  }
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>

<!--
I'm J.P. and I'll explain to you

_if_, and _how to fix_ wrong sharing

bold assertion

don't worry, before we leave this talk a better way will be shown
-->

---
layout: default
class: text-center
---

<img src="/images/to-label.jpg" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:25%;">

# If you write code, you share code

<style>
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>

<!--
another bold assertion

everyone here writes code; so you all share code

You __maight__ be using less-than-optimal sh

if everyone shares, high chance some are sharing wrong
-->

---
layout: default
---

## Not I ...

<v-clicks>

- programmers online
- conference acquaintances
- colleagues
- friends
- yourself

</v-clicks>

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

---
layout: default
---

## If you ...

<v-clicks>

- pip install
- nox, tox, hatch
- CI
- (continuous) deploy
- docker

</v-clicks>

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
sharing doesn't require >1 person or >1 machine

sharing doesn't require code to leave the machine

deploy: including `cp`

convinced yet?
-->

---
layout: default
class: text-center
---

<img src="/images/rwanda-stamp.png" style="position: absolute; right: 1.5rem; top: 1.5rem; max-height:13%;">
<img src="/images/prague-stamp2.png" style="position: absolute; right: 2rem; top: 1rem; max-height:20%;">

# How do you share your code?

<style>
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>

<!--
move the carefully crafted code to a harsh new environment

take the code from "works on my machine" to "works on your machine"
-->

---
layout: default
---

````md magic-move
```python
import geopy.geocoders
import urllib3

def locate(desc):
    locator = geopy.geocoders.Nominatim(user_agent="metuirology").geocode(desc)
    return locator.latitude, locator.longitude

def fetch_forecast(lat, lon):
    location = urllib3.request("GET", f"https://api.weather.gov/points/{lat},{lon}")
    forecast = urllib3.request("GET", location.json()["properties"]["forecast"])
    return [
        "🌨️" if "snow" in (sF := period["shortForecast"].lower()) else
        "🌧️" if "rain" in sF else
        "☁️" if "cloud" in sF else
        "☀️"
        for period in forecast.json()["properties"]["periods"]
    ]

if __name__ == "__main__":
    import sys
    print("\t".join(fetch_forecast(*locate(sys.argv[1]))))
```

```text
📄 metuirology.py
```
````

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
## Hand out the literal code

where do they put it? interactive Python? jupyter notebook? .py file?

must use a "good" file name

## Hand out a file

venv location?, active?, user-site-dir? PYTHONPATH?

saving a file is not the end of the sharing journey, its only the beginning.
-->

---
layout: default
---

````md magic-move
```bat
$ python /path/to/download/metuirology.py
```

```bat
$ cd /path/to/download/
$ python -m metuirology
```
````

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
be explicit with Python; side-step problem

can't import file not on PYTHONPATH, even knowning ABS path

;;;

this fixes import; still a side-step
-->

---
layout: default
---

````md magic-move
```text
📄 metuirology.py
```

```text
📄 metuirology.py
📄 requirements.txt
```

```text
📄 metuirology.py
📄 locate.py
📄 forcast.py
📄 requirements.txt
```

```text
📄 metuirology.zip
```
````

<div v-click.hide="1">

- `urllib3==2.2.*`
- `geopy==2.4.*`

</div>

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
## Hand out requirements

sharing code _and_ METADATA

What does a reciever do with requirements? Sounds like their problem!

pip install? conda install? uv? apt? Same Env!

How did you install them? remember?

## Hand out multiple files

are all files needed for any to work?

reciever must now unzip. Or not...
-->

---
layout: default
---


```bat
$ PYTHONPATH="/path/to/download/metuirology.zip:$PYTHONPATH" python
>>> import metuirology
```

<br/>

<v-clicks>

```bat
>>> sys.path.append("/path/to/download/metuirology.zip")
>>> import metuirology
```

</v-clicks>

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
being in the dir with .zip doesn't add this for you

side-step instructing user to unzip; ADD telling them how to edit bashrc

seem to be simple share story; appealing

I've seen all these strategies before
-->

---
layout: default
---

## Works until it doesn't

````md magic-move
```text
/home/ucodery/.venv/bin/python: No module named metuirology
```

```text
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/path/to/download/metuirology.py", line 10, in <module>
    from locate import place_to_lat_lon
ImportError: cannot import name 'place_to_lat_lon' from 'locate' (unknown location)
```

```
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/path/to/download/metuirology.py", line 9, in <module>
    import urllib3
ModuleNotFoundError: No module named 'urllib3'
```

```text
Traceback (most recent call last):
  File "/path/to/download/metuirology.py", line 10, in <module>
    from . import locate
ImportError: attempted relative import with no known parent package
```

```text
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/path/to/download/__main__.py", line 1, in <module>
    from . import metuirology
  File "/path/to/download/metuirology.py", line 10, in <module>
    from .. import locate
ImportError: attempted relative import beyond top-level package
```
````

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
failed to put module in PYTHONPATH

failed to put ALL modules in PYTHONPATH

failed to install deps (in same environment)

using package features in not-package

using relative imports like FS navigation

fixing immediate failures instead of root cause

the code is not resiliant to being shared

so far concentrate on giving away *code*; these are all fist-attempts at sharing

low effort for US; trade-offs for the reciever **because**...
-->

---
layout: default
class: text-center
transition: view-transition
---

<img src="/images/ireland-stamp.png" style="position: absolute; right: 1.5rem; top: 1rem; max-height:13%;">
<img src="/images/netherlands-stamp.png" style="position: absolute; right: 5rem; top: 1rem; max-height:13%;">
<img src="/images/spain-stamp.png" style="position: absolute; right: 1.5rem; top: 5.1rem; max-height:13%;">
<img src="/images/france-stamp.png" style="position: absolute; right: 4.9rem; top: 4.9rem; max-height:15%;">
<img src="/images/special.png" style="position: absolute; right: 0rem; top: 5.5rem; max-height:14%;">

# Sharing code is a three step exercise

<v-clicks>

## wrapping➞delivering➞unwrapping

</v-clicks>

<style>
  h2 {
    position: relative;
    top: 35%;
  }
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>

<!--
between two parties

less work on one end is more work on the other. vise versa

not disconnected checkpoints; connected pipeline

so far not considered the 2nd party burden

duct tape & bubblegum vs "unbox-worthy"

a package is the best way to share your code

responsible thing to do
-->

---
layout: default
class: text-center
---

<img src="/images/ireland-stamp.png" style="position: absolute; right: 1.5rem; top: 1rem; max-height:13%;">
<img src="/images/netherlands-stamp.png" style="position: absolute; right: 5rem; top: 1rem; max-height:13%;">
<img src="/images/spain-stamp.png" style="position: absolute; right: 1.5rem; top: 5.1rem; max-height:13%;">
<img src="/images/france-stamp.png" style="position: absolute; right: 4.9rem; top: 4.9rem; max-height:15%;">
<img src="/images/special.png" style="position: absolute; right: 0rem; top: 5.5rem; max-height:14%;">

# Sharing code is a three step exercise

## packaging➞distributing➞installing

<style>
  h2 {
    position: relative;
    top: 35%;
  }
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>

<!--
between two parties

less work on one end is more work on the other. vise versa

not disconnected checkpoints; connected pipeline

so far not considered the 2nd party burden

duct tape & bubblegum vs "unbox-worthy"

a package is the best way to share your code

responsible thing to do

I also will sometimes refer to the entire exercise as packaging

`wrapping➞delivering➞unwrapping`
-->

---
layout: default
class: text-center
---

# What users want is to run the code

<img src="/images/monty-stamp3.png" style="position: absolute; right: 1.5rem; top: 1.6rem; max-height:15%;">
<img src="/images/monty-stamp2.png" style="position: absolute; right: 5.25rem; top: 1.5rem; max-height:15%;">
<img src="/images/monty-stamp1.png" style="position: absolute; right: 8.7rem; top: 1.7rem; max-height:14.5%;">

<style>
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>

<!--
this includes script/exe, libraries/imports too

they want it to run when and where they say

don't want to think about any of the means, don't care what you decided

UNLESS is distracts, frustrates, stops them. If they can't or don't want to deal with your share

You might not care either, but whatever you *pass on thinking* about you force your consumers to care about

now you're giving them code and a PROBLEM
-->

---
layout: default
class: text-center
---

<img src="/images/lewis-clark.png" style="position: absolute; right: 1.5rem; top: 1.5rem; max-height:18%;">
<img src="/images/special.png" style="position: absolute; right: 2.5rem; top: 1.5rem; max-height:24%;">

# The best sharing strategy is the one that works every time

<style>
  h1 {
    font-size: 4rem;
    line-height: 1.2em;
    top: 35%;
  }
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>

<!--
every time is unreachable ideal state

strategies:

least number of steps (== 1)

has no user choices; "alternate path" instructions (OS)

low distraction, congnative overhead; process familiar to the reciever

generally get this following best-practices; **standards**

best-practices are familiar and capture **community inertia**

easy; intuitive; painless recieving

reciever has probably interacted with other packages before
-->

---
layout: default
---

````md magic-move
```python
import geopy.geocoders
import urllib3

def locate(desc):
    locator = geopy.geocoders.Nominatim(user_agent="metuirology").geocode(desc)
    return locator.latitude, locator.longitude

def fetch_forecast(lat, lon):
    location = urllib3.request("GET", f"https://api.weather.gov/points/{lat},{lon}")
    forecast = urllib3.request("GET", location.json()["properties"]["forecast"])
    return [
        "🌨️" if "snow" in (sF := period["shortForecast"].lower()) else
        "🌧️" if "rain" in sF else
        "☁️" if "cloud" in sF else
        "☀️"
        for period in forecast.json()["properties"]["periods"]
    ]

if __name__ == "__main__":
    import sys
    print("\t".join(fetch_forecast(*locate(sys.argv[1]))))
```
```python
# /// script
# dependencies = ["urllib3==2.2.*", "geopy==2.4.*"]
# ///
import geopy.geocoders
import urllib3

def locate(desc):
    locator = geopy.geocoders.Nominatim(user_agent="metuirology").geocode(desc)
    return locator.latitude, locator.longitude

def fetch_forecast(lat, lon):
    location = urllib3.request("GET", f"https://api.weather.gov/points/{lat},{lon}")
    forecast = urllib3.request("GET", location.json()["properties"]["forecast"])
    return [
        "🌨️" if "snow" in (sF := period["shortForecast"].lower()) else
        "🌧️" if "rain" in sF else
        "☁️" if "cloud" in sF else
        "☀️"
        for period in forecast.json()["properties"]["periods"]
    ]

if __name__ == "__main__":
    import sys
    print("\t".join(fetch_forecast(*locate(sys.argv[1]))))
```
````

<div v-click.hide="1">

```
urllib3==2.2.*
geopy==2.4.*
```

</div>

<style>
 li {
  line-height: 1.3em;
 }
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
shift sharing strategy to be less burdensome to reciever

now: 2 files & 2 install commands

next: 1 file & 1 install

best: 0 files & 0 install ????
-->

---
layout: default
---

## Inline Metadata

```text
# /// script
# requires-python = ">=3"
# dependencies = [
#   "some_dependency",
# ]
# ///
```

- Single-file executables
- Tool agnostic packaging standard

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
not a fantasy, reality

puposly designed to support ONE file

New standard: January 2024 (PEP-723)
-->

---
layout: default
---

```bat
$ hatch run metuirology.py
```

<br/>

```python
@nox.session
def weather(session):
    requirements = nox.project.load_toml("metuirology.py")["dependencies"]
    session.install(*requirements)
    session.run("metuirology.py", *session.posargs)
```

<br/>

```bat
$ uv run metuirology.py
```

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
Not supported by all env runners. Not supported by old versions of supported runners

Cannot install (pip), nor create a library for import ... or multi-file exe

Simple, but not very extensible solution (yet)

asking recievers to have specific `hatch` is a hidden install step (with version checking decision point)
-->

---
layout: default
class: text-center
---

<img src="/images/malaysia2-stamp.png" style="position: absolute; right: 1.5rem; top: 1.5rem; max-height:15%;">
<img src="/images/malaysia2-stamp.png" style="position: absolute; right: 5.1rem; top: 1.5rem; max-height:15%;">

# Restructure as a package

<style>
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>

<!--
we continue to converge on packaging as the best sharing strategy

take messy pile of PY files => organized project stack

requires specific FS layout
-->

---
layout: default
---

## Python project structure

- All project details specified in `pyproject.toml`
- Python code in one .py or one directory of .py files
- Every python directory contains an `__init__.py`

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
.py or dir is co-located with pyproject

directory can have more sub-directories of .py

The difference between a pile of co-located scripts and a python package? The presence of __init__.py files. Even if blank

init signals to python that if it is ok to look at/inside this dir when resolving an import
-->

---
layout: default
transition: view-transition
---

````md magic-move
```python
# /// script
# dependencies = ["urllib3==2.2.*", "geopy==2.4.*"]
# ///
import geopy.geocoders
import urllib3

def locate(desc):
    locator = geopy.geocoders.Nominatim(user_agent="metuirology").geocode(desc)
    return locator.latitude, locator.longitude

def fetch_forecast(lat, lon):
    location = urllib3.request("GET", f"https://api.weather.gov/points/{lat},{lon}")
    forecast = urllib3.request("GET", location.json()["properties"]["forecast"])
    return [
        "🌨️" if "snow" in (sF := period["shortForecast"].lower()) else
        "🌧️" if "rain" in sF else
        "☁️" if "cloud" in sF else
        "☀️"
        for period in forecast.json()["properties"]["periods"]
    ]

if __name__ == "__main__":
    import sys
    print("\t".join(fetch_forecast(*locate(sys.argv[1]))))
```
````

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

---
layout: default
---

````md magic-move
```toml
# pyproject.toml
[project]
dependencies = ["urllib3==2.2.*", "geopy==2.4.*"]
```

```toml
# pyproject.toml
[project]
name = "metuirology"
version = "1"
dependencies = ["urllib3==2.2.*", "geopy==2.4.*"]
```

```toml
# pyproject.toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
[project]
name = "metuirology"
version = "1"
dependencies = ["urllib3==2.2.*", "geopy==2.4.*"]
```
````

````md magic-move
```python
import geopy.geocoders
import urllib3

def locate(desc):
    locator = geopy.geocoders.Nominatim(user_agent="metuirology").geocode(desc)
    return locator.latitude, locator.longitude

def fetch_forecast(lat, lon):
    location = urllib3.request("GET", f"https://api.weather.gov/points/{lat},{lon}")
    forecast = urllib3.request("GET", location.json()["properties"]["forecast"])
    return [
        "🌨️" if "snow" in (sF := period["shortForecast"].lower()) else
        "🌧️" if "rain" in sF else
        "☁️" if "cloud" in sF else
        "☀️"
        for period in forecast.json()["properties"]["periods"]
   ]

if __name__ == "__main__":
    import sys
    print("\t".join(fetch_forecast(*locate(sys.argv[1]))))
```
````

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
build-system is a big choice you **must** make

all build-systems are 3rd party to CPython

secret: choice doesn't matter for pure-python

does bring a lot of impact; just choose one that works
-->

---
layout: default
---

````md magic-move
```text
📄 pyproject.toml
📄 metuirology.py
```

```text
📄 pyproject.toml
📄 metuirology.py
📄 locate.py
📄 forcast.py
```

```text
📄 pyproject.toml
📁 metuirology
  📄 metuirology.py
  📄 locate.py
  📄 forcast.py
```

```text
📄 pyproject.toml
📁 metuirology
  📄 __init__.py
  📄 metuirology.py
  📄 locate.py
  📄 forcast.py
```
````

<v-clicks>

## That's so many files!

</v-clicks>

<style>
  h2 {
    text-align: center;
  }
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
still just the script, but again 2 files! backwards!

*more* steps to deliver same as script; so far

1 pyproject defines 1 project -- not many

This has all been prep for packaging/ wrapping
-->

---
layout: default
---

```text
$ hatch build -t wheel
───────────────────── wheel ─────────────────────
dist/metuirology-1-py3-none-any.whl
```

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
time to wrap it all up; wheels

de-facto standard for dist

wheel is a packaging standard; not one tool
-->

---
layout: default
---

## A wheel lets you

- deliver one thing
- share a script, a library, or anything
- publish to a package repository

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
wheels open up possibilities

... plug-in, gui

PyPI is way to deliver 1/2 and have reciever deliver final mile
-->

---
layout: default
---

## A wheel lets the reciever

- install how they want
- track where a package came from
- know what other packages are required
- re-share without having to re-wrap

<style>
  .slidev-page {
    background-image: url("/images/cardboard.jpg");
    background-size: cover;
  }
</style>

<!--
don't even have to know what installer is used

work with any versions of tools older than one year

standards give *you* and the *recievers* choice; interoperability

re-share only involves last 2 share steps

code once wrapped can be shared as much as you want; actually really good
-->

---
layout: default
class: text-center
---

<img src="/images/czech-stamp.png" style="position: absolute; right: 1.5rem; top: 1.5rem; max-height:15%;">
<img src="/images/czech-stamp.png" style="position: absolute; right: 5.5rem; top: 1.5rem; max-height:15%;">
<img src="/images/dec-black-mark.png" style="position: absolute; right: .25rem; top: 2.5rem; max-height:12%;">

# Code is installed much more than it is packaged

<style>
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>

<!--
Just like "code is read much more than it is written"

Were sharing your code since the beginning. So much work to still be sharing

why should you care about hard packaging problems when you can pass some of it off to consumers? Because you are solving the problem once for everyone

making the sharing strategy *Robust*

any step you take out of the "install" instructions and put into the "packaging" process will save time multiplicitavely

packaging *is* a burden, but one you can remove from recievers
-->

---
layout: default
class: text-center
---

<img src="/images/usps-label.jpg" style="position: absolute; right: 1.5rem; top: 5%; max-height:90%;">

# Delivered

<PoweredBySlidev>
</PoweredBySlidev>

<style>
  h1 {
    font-size: 6rem;
    transform: rotate(-25deg);
    border: 2px solid;
    width: 50%;
    left: 5%;
    top: 40%;
  }
  .slidev-page {
    background-image: url("/images/cardboard-title.jpg");
    background-size: cover;
    background-position: -10%;
  }
</style>
