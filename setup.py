#!/usr/bin/env python

from distutils.core import setup

setup(name='genetic_algorithm',
      version='1.1',
      description='Python genetic algorithm',
      author='Guillaume Briand',
      url='https://github.com/Ethoytaryn/genetic_algorithm.git',
      packages=['src', 'src.Metier', 'src.Metier.genetique', 'src.Tools'], requires=['matplotlib']
      )
