from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in grocery/__init__.py
from grocery import __version__ as version

setup(
	name="grocery",
	version=version,
	description="fdf",
	author="dfd",
	author_email="df",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
