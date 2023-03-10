from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    """
    This function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace('\n','') for req in requirements]

setup(
    name='mlproject-gk',
    version='0.0.1',
    author='GKrish',
    author_email='gopalinlatvia@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)