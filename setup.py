import io

from setuptools import find_packages
from setuptools import setup

# with io.open("README.rst", "rt", encoding="utf8") as f:
readme = "empty"

setup(
    name="coolpwn",
    version="1.0.0",
    url="https://flask.palletsprojects.com/tutorial/",
    license="BSD",
    maintainer="kais",
    maintainer_email="hjuj_91@163.com",
    description="framework for pwn",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)