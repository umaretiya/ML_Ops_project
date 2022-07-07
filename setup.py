from setuptools import setup
from typing import List,Dict,Tuple
    

# Declaring variables for setup functions
PROJECT_NAME = "housing-prediction"
VERSION = "0.0.1"
AUTHOR = "Keshav Umaretiya"
DESCRIPTION = "This is First Machine Learning Project"
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME  = "requirements.txt"


def get_requirements_list():
    """
    Return this function is going to return a name of 
    library which is mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines()


setup(
    name = PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires = get_requirements_list()
)