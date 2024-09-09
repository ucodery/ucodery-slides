# Site Unseen: hidden python customization

### Summary
Python has a dizzying array of environment variables, most of which are used for startup tuning. The list has grown so long that recent Python versions have split the description of these variables into their own help (--help-env). It is valuable to a Pythonista to know about all of these, but this talk will show you how to use a subset to personalize the Python runtime environment to your developer needs and preferences.

Python does a lot of work to customize itself when starting up. It also provides hooks for even more customization from users and packages during startup. Some of these are on by default while others require enabling. Learn how to take advantage of Python's startup to craft a custom interpreter.

### Outline
* Intro (1 minute)
* The site module (3 minutes)
    * what is its purpose
    * how to disable site (or just some parts)
    * executing site as a tool
* Expansion of import paths (6 minutes)
    * crux of virtual environment activation
    * more than one site-packages, for a reason
    * pth files, they're wild
* Better UX (4 minutes)
    * tab-complete
    * history
    * builtins bet bigger?!
* Unlimited customization (7 minutes)
    * sitecustomize/ usercustomize
    * PYTHONSTARTUP
        * how it differs from usercustomize and when to use each
* Debugging all this interpreter configuration (3 minutes)
    * turn things off so startup is deterministic
    * sometimes users write bad code (customization) but still want their interpreter to work
* Conclusion (1 minute)
