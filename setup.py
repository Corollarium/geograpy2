from setuptools import setup
import os

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

setup(name='geograpy2',
      version='0.1.0',
      description='Extract countries, regions and cities from a URL or text',
      long_description=long_description,
      url='https://github.com/Corollarium/geograpy2',
      download_url ='https://github.com/Corollarium/geograpy2',
      author='Corollarium',
      author_email='email@corollarium.com',
      license='MIT',
      packages=['geograpy2'],
      install_requires=[
            'numpy',
            'nltk',
            'newspaper',
            'jellyfish',
            'pycountry'
      ],
      scripts=['geograpy/bin/geograpy-nltk'],
      package_data = {
            'geograpy': ['data/*.csv'],
      },
      zip_safe=False)