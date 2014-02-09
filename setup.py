#!/usr/bin/env python

from distutils.core import setup

setup(name='AzureTableStore',
      version='1.0',
	  py_modules=['AzureTableStore'],
	  requires=['azure'],
      description='A weather forecast engine on Azure',
      author='Abhishek Dey',
      author_email='abhishekde@hotmail.com',
      url='http://www.asthmaccurate.cloudapp.net',
      
     )