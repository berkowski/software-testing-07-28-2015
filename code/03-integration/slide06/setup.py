import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        # Add doctests and make verbose by default
        self.pytest_args = ['--doctest-modules', '-v']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause  outside the eggs aren't loaded
        import pytest
        # if '--doctest-modules' not in self.pytest_args:
        #     self.pytest_args += " --doctest-modules"

        errno = pytest.main(self.pytest_args)
        return errno

setup(
    name = "WhoiMath",
    version = "0",
    author = "Zac Berkowitz",
    author_email = "zberkowitz@whoi.edu",
    description = ("WhoiMath package -- because our division is better!"),
    license = "BSD",
    keywords = "example math tutorial testing",
    packages=['whoiMath'],
    classifiers=[
                "Development Status :: 3 - Alpha",
                "Topic :: Utilities",
                "License :: OSI Approved :: BSD License",
        ],
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
)
