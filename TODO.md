Proposed, unwritten, talks.

# It’s not funny if I have to explain it

### Summary
Some may find execution confusion a laughing matter but this talk will take a serious, analytical look at how any why executables are not always as we want them.

### Description
This talk may be for you if you have ever wondered why one binary was run over another, or one library was linked to over another (or wasn’t). This talk may be for you if this execution confusion has ever lead you to run commands that degraded your system from cozy mystery to unknowabe Lovecraftian maze.

### Outline
* Introduction (2 minute)
* What is going on with Python? (4 minutes)
    * how interpreter is chosen
    * how imports are found
* Execution Confusion (4 minutes)
    * why `python` isn't always the Python we want
    * why `import`s are wrong or missing at times
* Is this a Python problem? (4 minutes)
    * sort of yes - poor decisions
    * sort of no - TMO (too many options)
* Stopping execution confusion (4 minutes)
    * don't mix isolation techniques
* Debug when execution confusion does happen (4 minutes)
    * understand the environment surrounding Python
    * understand Python's own environment lookup
* Conclusion (2 minutes)


# Who chooses the requirements

### Summary
Learn who really controls a software's environment and support, rather than dictate, healthy environment creation.

### Description
All modern software is the composition of independently developed projects. As a programmer you have some duty to record the relationship your project has to other projects in order to build and run correctly.

It is tempting to think that you, the software author, or you the package maintainer, are in full control over what those requirements are, but you are not. This misunderstanding is the source of many errors. And when authors do discover this but instead of accept it they make a power grab, all they really do is contribute to "dependency hell".

Don't add to dependency hell, add to the users' success and learn to live with less control.

### Overview
* Introduction (2 minutes)
* Mistaken identities of requirement control (3 minutes)
* What level of control different roles actually have (4 minutes)
* The motivation for upgrading/downgrading a requirement (3 minutes)
* The point of requirements in a project (6 minutes)
* Different users of a package working together for success (4 minutes)
* Conclusion (2 minutes)


# What's your personality type?

### Summary
Are you more of a goose or a duck? Do you ask for forgiveness or permission? Do you like to leap?
These are not a series of unrelated questions designed to say something about your psyche, but rather shorthands for different styles of programming. You might not know which describes you yet, but you probably already have a personal style.
In this talk, you will learn not only how to name some of your coding traits, but how to use a typechecker, like mypy, to embrace your authentic programming self.

### Outline
* Introduction (1 minute)
* Quick review of types in the runtime (3 min)
    * Python is a strongly typed language, weakly held
* Static v Dynamic typing (5 min)
    * do you like to verify types during runtime or during development?
* Duck v Goose typing (5 min)
    * do you ask the question is-a or has-a?
    * depending on static v dynamic the question is asked differently
* LBYL v EAFP typing (5 min)
    * would you rather catch exceptions than ask all these questions?
    * raising, asserting can still be used by static checkers
* type safety is a wide field (5 min)
    * there is not an always-best answer to these questions
    * it's not always one or the other for a code base
* Conclusion (1 min)


# Package Management: the Hard Part

### Summary
`pip install example`
A very familiar command and one that hides a lot of complexity - a lot to go wrong. But despite the command, it's not the installation that is difficult; it's the many complex steps to find a wheel that matches what the user intended that is difficult and will cause most failures.

### Description
In its fundamental use case a package manager has a few jobs: to select a package distribution that is compatible with both the user request and the current environment, download that distribution, and install it. Actually placing a wheel in a python environment is straightforward. And downloading doesn't have too many rough edges. But finding a distribution that works in the current environment and matches what the user wants is a Hard problem. In this talk we will briefly go over the many steps your package manager takes to figure this out for a typical use-case.

### Outline
* Introduction (1 minute)
* Installing - the user's perspective (2 minutes)
    * pip install, then use package
* Installing - the tool's perspective
    * name normalization (2 minutes)
    * find a workable version (5 minutes)
    * find a workable distribution (4 minutes)
    * downloading a wheel (1 minute)
    * unpacking a wheel (2 minutes)
* Source Distributions (4 minues)
    * added build step
* Backtracking (5 minutes)
    * when and why the tool might not be able to select the first matching wheel
* Installation overview (3 minutes)
    * bringing it all together
* Conclusion (1 miinute)
