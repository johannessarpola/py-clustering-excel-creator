#!/usr/bin/env python

from setuptools import setup
import unittest


def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(name='clustering_excel_creator',
      version='0.1',
      description='Creates Excels based on clustering result',
      author='Johannes Sarpola',
      author_email='johannes.sarpola@gmail.com',
      url='https://gitlab.com/johannessarpola/',
      packages=['app'],
      setup_requires=['pytest-runner', 'openpyxl'],
      tests_require=['pytest'],
      )
