# -*- encoding: utf8 -*-
######################################################
# Author: Chen KX <ckx1025ckx@gmail.com>             #
# License: BSD 2-Clause                              #
######################################################


from setuptools import setup

long_description = \
"""
ckxtraceviewer
======
ckxtraceviewer is a python-only solution to add a trace view to IDA Pro. 
Use `<Ctrl-Alt-I>` to open a window with an embedded _Qt console_. 
You can then load an execution trace which are automatically synchronized with `IDA VIEW-A`.
See full README on GitHub: <https://www.github.com/ckx/ckxtraceviewer>.
"""

setup(name='ckxtraceviewer',
      version='1.0',
      description='IDA plugin to embed a trace view inside IDA',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Chen KX',
      author_email='ckx1025ckx@gmail.com',
      url='https://www.github.com/ckx/ckxtraceviewer',
      packages=['ckxtraceviewer','ckxtraceviewer/ui'],
      install_requires=[
          'monkeyhex>=1.0',
      ],
      license="BSD",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Plugins",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
      ],
)