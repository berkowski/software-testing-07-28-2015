### (Practical) Software Tests

Zac Berkowitz



### Disclaimer
- There are whole books, blogs, *idealogogies* about proper methods and practices for testing.
- *Teams* are devoted to this stuff in larger dev environments.
- The basics are simple, but their implementation can be dependant on language and frameworks.
- I'll talk about some methods I've found useful..



### Goals of Testing
- Predictable Codebases
- Some kind of runtime assurance.
- Robustness to changes.



### Practical Goals of Testing
- Easy to write / easier to run.
- Extendible.  Add new test cases as they crop up.



### Types of Software Tests
- Unit: <!-- .element: class="fragment highlight-green" data-fragment-index="1" -->
  - White box <!-- .element: class="fragment highlight-green" data-fragment-index="1" -->
  - Defined output for given input, with knowledge of internals  <!-- .element: class="fragment highlight-green" data-fragment-index="1" -->
- Functional:<!-- .element: class="fragment highlight-green" data-fragment-index="1" -->
  - Black box.  <!-- .element: class="fragment highlight-green" data-fragment-index="1" -->
  - Known outputs for given inputs, no knowledge of internals  <!-- .element: class="fragment highlight-green" data-fragment-index="1" -->
- Integration: Software modules combined and tested at their interfaces
- Regression: Software changes introduce new bugs?



### Tools
- Test-helpers (test runners, packages, etc.)<!-- .element: class="fragment highlight-green" data-fragment-index="1" -->
- Your IDE of choice.
- Test Environments
  - virtualenv (thin)<!-- .element: class="fragment highlight-green" data-fragment-index="1" -->
  - pyenv (medium)
  - vagrant/virtualbox (thick)



### Tools Alone Won't Save you....
- Source organization
- Adopt a coding style, *Use the adopted coding style*
- **Documentation, Documentation, Documentation**
   - inline and external
   - Tools like *sphinx* and *doxygen* for code-based user documentation



### What's Covered (Python)
- Using virtualenv to isolate your development environment
- Writing simple unit tests using python's *doctest* and *unittest* modules
- Dealing with 3rd party dependencies using python's *mock* module
- Automating testing with *py.test* and *setuptools* integration



### virtualenv
- Create lightweight, project-specific python environments.
- Easily bridge development/deployment python environment differences

  <pre><code class="bash" data-trim contenteditable>
# create a new virtualenv
$>virtualenv test_env
Using base prefix '/usr'
New python executable in test_env/bin/python3
Also creating executable in test_env/bin/python
Installing setuptools, pip...done.
# switch to the new directory and activate 
$>cd test_env
test_env$>source bin/activate
(test_env)test_env$>
</code></pre>



### Unit testing in Python
- doctests:  Write your tests in your python code's docstrings!

  <pre><code class="python">
def multiply(a,b):
      """
      Multiply two numbers together.
      Example:
      >>> multiply(3, 4)
      12
      """
  </code></pre>

- unittests:  For when your unit tests are more complicated, or you want to
  generate large numbers of tests



### Dealing with external code.
- *mock* is built into the *unittest* package in python 3.4
  - Backport is available for 2.7.x through pypi
- Stub external software modules OR hardware interaction.
- Tests are based on *assumed* functionality of what's stubbed. 
- Tests are only as good as your assumptions! <!-- .element: class="fragment highlight-green" data-fragment-index="0" -->



### Integrating with build tools
- Test runners ease running of test
  - Run unit-tests and doctests with one command!
  - Can generate more complicated tests
- *setuptools* (setup.py) can also be used as a testing gateway!
- We'll use py.test with a setup.py file to run tests more easily



### Extra Credit 1: Testing Qt signals and slots!
- Unit-tests can be extended to Qt's signals/slots mechanism!
  - Simulate user interactions with GUI objects (mouse clicks, keyboard strokes, etc.)
  - Listen for and check contents of emitted signals.
- For PyQt this is limited to PyQt5 (PyQt4 does not expose QSignalSpy)



### Extra Credit 2: C++ tests with gtest/gmock
- gtest and gmock, testing frameworks for c/c++
- Similar testing ideas as python example.



