from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mult_printers/__init__.py
from mult_printers import __version__ as version

setup(
	name="mult_printers",
	version=version,
	description="send print order to multible printers",
	author="Ahmed Abdulrahman",
	author_email="ahmed751995",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
