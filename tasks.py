from invoke import task


@task
def lint_python(c):
    """Perform python code formatting with black, isort and flake8"""
    c.run("black ./tasks.py SoapLibrary/")
    c.run("isort ./tasks.py SoapLibrary/")
    c.run("flake8 ./tasks.py SoapLibrary/")


@task
def lint_robot(c):
    """Perform robot code formatting with robotidy"""
    c.run("robotidy Tests/")


@task(lint_python, lint_robot)
def lint(c):
    """
    Perform code formatting for both robot and python code.
    Short option for `inv lint-python && inv lint-robot`.
    """
    pass


@task
def test(c):
    """Runs robot acceptance tests"""
    c.run("robot --loglevel DEBUG Tests/")
