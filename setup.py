import os
from runpy import run_path

from setuptools import find_packages, setup

# read the program version from version.py (without loading the module)
# __version__ = run_path('src/mai/version.py')['__version__']
import versioneer


def read(fname):
    """Utility function to read the README file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="mai",
    version=versioneer.get_version(),
    author="Alejandro Gil",
    author_email="alejandrogilelias940711@gmail.com",
    description="A short summary of the project",
    license="proprietary",
    url="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"mai": ["res/*"]},
    long_description=read("README.md"),
    install_requires=required,
    tests_require=[
        "pytest",
        "pytest-cov",
        "pre-commit",
    ],
    platforms="any",
    python_requires=">=3.8",
    cmdclass=versioneer.get_cmdclass(),
)
