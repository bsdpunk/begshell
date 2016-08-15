#from distutils.core import setup
from setuptools import setup, find_packages

#dependecy_links = ["git+https://github.com/pexpect/pexpect.git#egg=pexpect-0.1"]
#install_requires = ['pyvmomi','pyvim']

setup(
    name='bs',
    version='0.01',
    packages=['bs',],
    #install_requires=install_requires,
    entry_points = { 'console_scripts': [
        "bs = bs.bs:cli", ],
        },
    author = "Dusty C",
    author_email = "bsdpunk@gmail.com.com",
    description = "A Modal Terminal for Financial Data",
    license = "BSD",
    keywords = "Shell cli terminal financial data",
    url = 'bsdpunk.blogspot.com'   
    )
