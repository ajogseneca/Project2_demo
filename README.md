# Setting up a Python project with Poetry

This guide will show you how to set up a Python project using Poetry package manager.

##  Prerequisites

Make sure you have Python and Poetry installed on your system.

##  Installation

1.  Install Poetry by running `pip install poetry`.
2.  Create a new project with `poetry new my_project`.
3.  Add any dependencies you need using `poetry add <dependency_name>`.
4.  Install dependencies using `poetry install` command, which creates a virtual environment.
5.  Ensure that the virtual environment is created in the same directory as the project by running `poetry config virtualenvs.in-project true`.
6.  Activate the virtual environment by running `poetry shell`.

## Good to go !

You're now ready to start coding in your Python project with all dependencies installed in your virtual environment!

## Rename a file

There are several ways you can use poetry to publish the package such as PyPI, publish to private repos etc.
We can easily build and publish using poetry using poetry
Some commands are `poetry build`. to actually build the package and finally `poetry publish <the method you want to publish>`

