from setuptools import setup

version = "{{cookiecutter.version}}"
name = "{{cookiecutter.project_name}}"
author = "{{cookiecutter.author_name}}"
author_email = "{{cookiecutter.author_email}}"
description = "{{cookiecutter.description}}"
license_ = "{{cookiecutter.license}}"

setup(
    name=name,
    version=version,
    packages=[''],
    url='',
    license=license_,
    author=author,
    author_email=author_email,
    description=description,
    install_requires=["importlib_metadata==8.5.0", "cookiecutter==2.6.0", "click==8.1.7", "build==1.2.2"]
)
