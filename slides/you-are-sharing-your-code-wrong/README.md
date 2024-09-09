# You are sharing your code wrong (and what to do about it)

### Summary
Everyone who writes also distributes Python code. The only reliable way to share Python code is by packaging it, any other way hurts your consumers. Packaging can be an intimidating topic most would rather avoid but following just a few best practices of packaging can make your code much easier to share, even without going through the process of uploading to pypi.org.

### Description


### Outline
* Premise: all python code gets shared (3 min)
    * to other machines: deploying, git, CI
    * on the same machine: containers, tox, testing
* give your users what they want: a package (3 min)
    * users don't want to deal with source code
    * they want an import or a script that just runs
* A collection of python files does not make a package (5 min)
    * Most often a package is made up of files, but not always
    * PathFinder, and sys.path
* Organizing the scripts (2 min)
    * __init__.py, file hierarchy
* Bonuses for packaging (8 min)
    * relative imports
    * data imports
    * module execution
* basic pyproject.toml (4 min)
    * the only part of distribution packaging brought up
    * not enough to publish, but enough to install from source
* Conclusion (2 min)
    * the first step to packaging is not scary
    * a well-structured project makes for a more robust project
