from setuptools import setup, find_packages
import os

version = '0.2.0'

setup(name='atreal.richfile.preview',
      version=version,
      description="Preview Support Plugin for RichFileQualifier",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='richfile plone preview atreal',
      author='atReal',
      author_email='contact@atreal.fr',
      url='http://svn.plone.org/svn/collective/atreal.richfile.preview/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['atreal', 'atreal.richfile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'atreal.richfile.qualifier>=1.1.0',
          'Products.AROfficeTransforms>=0.10.0'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
