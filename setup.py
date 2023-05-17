from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in operations_app/__init__.py
from operations_app import __version__ as version

setup(
	name="operations_app",
	version=version,
	description="Operations for droplet employees",
	author="Ryan Chau",
	author_email="ryanthelion.c@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
