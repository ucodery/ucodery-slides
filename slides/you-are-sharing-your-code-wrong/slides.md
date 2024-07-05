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
layout: image
class: text-center
image: /images/cardboard-title.jpg
---
<!-- https://www.flickr.com/photos/27215653@N00/3638034382 -->

<img src="/images/this-side-up.jpg" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:25%;">

# You Are Sharing Your Code Wrong
## (and what to do about it)

<style>
  h2 {
    position: relative;
    top: 35%;
  }
</style>

<!--
bold assertion

don't worry, before we leave this talk a better way will be shown
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
---

<img src="/images/to-label.jpg" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:25%;">

# If you write code, you share code

<!--
another bold assertion

everyone here  writes code; so you all share code
-->

---
layout: image
image: /images/cardboard.jpg
---

## Not I ...

<v-clicks>

- programmers online
- conference acquaintances
- colleagues
- friends
- yourself

</v-clicks>

---
layout: image
image: /images/cardboard.jpg
---

## If you ...

<v-clicks>

- pip install
- nox, tox, hatch
- CI
- (continuous) deploy
- docker

</v-clicks>

<!--
sharing doesn't require >1 person or >1 machine

deploy: including `cp`

convinced yet?
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
---

<img src="/images/czech-stamp.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:15%;">
<img src="/images/czech-stamp.png" style="position: absolute; left: 5.5rem; top: 1.5rem; max-height:15%;">
<img src="/images/dec-black-mark.png" style="position: absolute; left: 2rem; top: 2.5rem; max-height:12%;">

# How do you share your code?

<!--
move the carefully crafted code to a harsh new environment

take the code from "works on my machine" to "works on your machine"
-->

---
layout: image
image: /images/cardboard.jpg
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

<!--
## Hand out the literal code

where do they put it? interactive Python? jupyter notebook? .py file?

must use a "good" file name

## Hand out a file

venv location?, active?, user-site-dir? PYTHONPATH?

saving a file is not the end of the sharing journey, its only the beginning.
-->

---
layout: image
image: /images/cardboard.jpg
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

<!--
knowning ABS won't help import
-->

---
layout: image
image: /images/cardboard.jpg
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

<!--
## Hand out requirements

What does a user do with requirements? Sounds like their problem!

pip install? conda install? uv? apt?

## Hand out multiple files

are all files needed for any to work?

user must now unzip.
-->

---
layout: image
image: /images/cardboard.jpg
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

<!--
being in the dir with .zip doesn't add this for you
-->

---
layout: image
image: /images/cardboard.jpg
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

<!--
failed to put module in PYTHONPATH

failed to put entire pkg in PYTHONPATH

failed to install deps (in same environment)

using package features in not-package

using relative imports like FS navigation

fixing immediate failures instead of root cause

These are all fist-attempts at sharing, converging on packaging, slowly

I've seen all these strategies before

trade-offs for your user **because**...
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
transition: view-transition
---

# Sharing code is a three step exercise

<img src="/images/australia-stamp.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:16%;">
<img src="/images/special.png" style="position: absolute; left: 1rem; top: 1.5rem; max-height:18%;">
<img src="/images/canada-stamp.png" style="position: absolute; left: 6.25rem; top: 1.5rem; max-height:15%;">
<img src="/images/papua-stamp.png" style="position: absolute; left: 11.75rem; top: 1.5rem; max-height:15%;">

<v-clicks>

## wrapping➞delivering➞unwrapping

</v-clicks>

<style>
  h2 {
    position: relative;
    top: 35%;
  }
</style>

<!--
between two parties

less work on one end is more work on the other. vise versa

connected pipeline

harin

maybe you stared to notice we slowly created a software distribtuion

a package is the best way to share your code

responsible thing to do
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
---

# Sharing code is a three step exercise

<img src="/images/australia-stamp.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:16%;">
<img src="/images/special.png" style="position: absolute; left: 1rem; top: 1.5rem; max-height:18%;">
<img src="/images/canada-stamp.png" style="position: absolute; left: 6.25rem; top: 1.5rem; max-height:15%;">
<img src="/images/papua-stamp.png" style="position: absolute; left: 11.75rem; top: 1.5rem; max-height:15%;">

## packaging➞distributing➞installing

<style>
  h2 {
    position: relative;
    top: 35%;
  }
</style>

<!--
between two parties

less work on one end is more work on the other. vise versa

maybe you stared to notice we slowly created a software distribtuion

a package is the best way to share your code

responsible thing to do

I also will sometimes refer to the entire exercise as packaging
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
transition: view-transition
---

# What tool users want is to run `cmd`

<img src="/images/australia-stamp.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:16%;">
<img src="/images/special.png" style="position: absolute; left: 1rem; top: 1.5rem; max-height:18%;">
<img src="/images/canada-stamp.png" style="position: absolute; left: 6.25rem; top: 1.5rem; max-height:15%;">
<img src="/images/papua-stamp.png" style="position: absolute; left: 11.75rem; top: 1.5rem; max-height:15%;">

<!--
don't want to think about any of the means: files, pip, internet, user-sitepackages

don't care what packaging format you use, or what distribution method you choose, EXCEPT the more difficult or fragile it is the more likely they will bail

You might not care either, but whatever you *pass on thinking* about you force your consumers to care about

this includes libraries/imports too
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
---

# What library users want is `import` to work

<img src="/images/australia-stamp.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:16%;">
<img src="/images/special.png" style="position: absolute; left: 1rem; top: 1.5rem; max-height:18%;">
<img src="/images/canada-stamp.png" style="position: absolute; left: 6.25rem; top: 1.5rem; max-height:15%;">
<img src="/images/papua-stamp.png" style="position: absolute; left: 11.75rem; top: 1.5rem; max-height:15%;">

<!--
don't want to think about any of the means: files, pip, internet, user-sitepackages

don't care what packaging format you use, or what distribution method you choose, EXCEPT the more difficult or fragile it is the more likely they will bail

You might not care either, but whatever you *pass on thinking* about you force your consumers to care about

this includes libraries/imports too
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
---

# The best sharing strategy is the one that works the first time every time

<img src="/images/australia-stamp.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:16%;">
<img src="/images/special.png" style="position: absolute; left: 1rem; top: 1.5rem; max-height:18%;">
<img src="/images/canada-stamp.png" style="position: absolute; left: 6.25rem; top: 1.5rem; max-height:15%;">
<img src="/images/papua-stamp.png" style="position: absolute; left: 11.75rem; top: 1.5rem; max-height:15%;">

<style>
  h1 {
    font-size: 3.4rem;
    line-height: 1.4em;
  }
</style>

<!--
least number of steps (== 1)

has no "alternate path" instructions (OS)

low congnative overhead; is familiar to the user

generally get this following best-practices; **standards**

user has probably interacted with other packages before

packaging == SW manufacturing line
-->

---
layout: image
image: /images/cardboard.jpg
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

- `urllib3==2.2.*`
- `geopy==2.4.*`

</div>

<style>
 li {
  line-height: 1.3em;
 }
</style>

---
layout: image
image: /images/cardboard.jpg
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

<!--
not a fantasy, reality
-->

---
layout: image
image: /images/cardboard.jpg
---

## Inline Metadata

```text
# /// script
# dependencies = [
#   "some dependency",
# ]
# ///
```

- Tool agnostic packaging standard
- One file only

<!--
Very New standard: January 2024 (PEP-723)

Not supported by all env runners. Not supported by old versions of supported runners

Cannot install (pip), nor create a library for import ... or multi-file exe

Simple, but not very extensible solution (yet)

here to tell you there is a better way
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
---

<img src="/images/czech-stamp.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:15%;">
<img src="/images/czech-stamp.png" style="position: absolute; left: 5.5rem; top: 1.5rem; max-height:15%;">
<img src="/images/dec-black-mark.png" style="position: absolute; left: 2rem; top: 2.5rem; max-height:12%;">

# Restructure as a package

<!--
we continue to converge on packaging as the best sharing strategy

take messy pile of PY files => organized project stack

requires specific FS layout
-->

---
layout: image
image: /images/cardboard.jpg
---

## Python project structure

- All project details specified in `pyproject.toml`
- Python code in one .py or one directory of .py files
- Every python directory contains an `__init__.py`

<!--
.py or dir is co-located with pyproject

directory can have more sub-directories of .py

The difference between a pile of co-located scripts and a python package? The presence of __init__.py files. Even if blank

init signals to python that if it is ok to look at/inside this dir when resolving an import
-->

---
layout: image
image: /images/cardboard.jpg
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

```toml{1,5,8,9|1,5-7,9|1-4,9}
📄 pyproject.toml
   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"
   [project]
   name = "metuirology"
   version = "1"
   dependencies = ["urllib3==2.2.*", "geopy==2.4.*"]
📄 metuirology.py
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
```
````

<!--
build-system is a big choice you **must** make

asking users to have specific `hatch` is 1 more share step

does bring a lot of impact; just choose one that works
-->

---
layout: image
image: /images/cardboard.jpg
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
</style>

<!--
after all this, the project definition stays the same!

1 pyproject defines 1 project -- not many

This has all been prep for packaging/ wrapping
-->

---
layout: image
image: /images/cardboard.jpg
---

```text
$ hatch build -t wheel
───────────────────── wheel ─────────────────────
dist/metuirology-1-py3-none-any.whl
```

<!--
time to wrap it all up; wheels

not only gain new deployment channels (PyPI) but also gain ability to work with any versions of tools older than one year
-->

---
layout: image
image: /images/cardboard.jpg
---

## A wheel lets you

- deliver one thing
- share a script, a library, or anything
- publish to a package repository

<!--
wheels open up possibilities
-->

---
layout: image
image: /images/cardboard.jpg
---

## A wheel lets your user

- install how they want
- track where a package came from and what it brought
- re-share without having to re-package

<!--
don't even have to know what installer is used

standards give *you* and your *users* choice; interoperability
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
---

<img src="/images/czech-stamp.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:15%;">
<img src="/images/czech-stamp.png" style="position: absolute; left: 5.5rem; top: 1.5rem; max-height:15%;">
<img src="/images/dec-black-mark.png" style="position: absolute; left: 2rem; top: 2.5rem; max-height:12%;">

# Code is installed much more than it is packaged

<!--
Just like "code is read much more than it is written"

Were sharing your code since the beginning. So much work to still be sharing

why should you care about hard packaging problems when you can pass some of it off to consumers? Because you are solving the problem once for everyone

making the sharing strategy *Robust*

any step you take out of the "install" instructions and put into the "packaging" process will save time multiplicitavely

packaging *is* a burden, but one you can remove from users
-->

---
layout: image
image: /images/cardboard-title.jpg
class: text-center
---

<img src="/images/inspected.png" style="position: absolute; left: 1.5rem; top: 1.5rem; max-height:25%;">

# Delivered

<PoweredBySlidev>
</PoweredBySlidev>

<style>
  h1 {
    font-size: 6rem;
    transform: rotate(-25deg);
    border: 2px solid;
    width: 50%;
    left: 25%;
  }
</style>
