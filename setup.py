from setuptools import setupwith open("README.md", "r") as fh:    long_description = fh.read()setup(    name = 'scmap',    version = '0.1.0',    description = 'Assigns rgb colors to points on sphere.',    long_description = long_description,    long_description_content_type = "text/markdown",    url = 'https://github.com/vedranaa/sphere-colormap',    author = 'Vedrana Andersen Dahl',    author_email = 'vand@dtu.dk',    license ='lgpl-2.1',    py_modules = ['scmap']    )