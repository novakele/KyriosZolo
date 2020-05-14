import os

from setuptools import setup

def load_requirements(fname):
    with open(fname, "r") as fichier:
        reqs = fichier.read().split("\n")
        return reqs


kwargs = {
    "include_package_data": True,
    "install_requires": load_requirements("requirements.txt"),
}

if os.getenv("READTHEDOCS", False):
    setup(
        **kwargs, python_requires=">=3.7",
    )
else:
    setup(**kwargs)
