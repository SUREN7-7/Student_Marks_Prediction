from setuptools import find_packages,setup
from typing import List

#List is different from list() and is used as a return type

HYPEN_E_DOT='-e .'

# ->List[str] represents return type . and file_path:str represents the input parameter is str

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #['numpy\n', 'pandas\n', '-e .\n']

        requirements=[req.replace("\n","") for req in requirements]
        #['numpy', 'pandas', '-e .']

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Suren',
author_email='shyamsaratsuren77@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)

#The '-e .' refers / maps to setup.py so that when pip install -r requirements.txt  to maps to this file