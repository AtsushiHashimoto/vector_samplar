#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from pip_github_test import __author__, __version__, __license__
 
setup(
        name             = 'vector_sampler',
        version          = __version__,
        description      = 'simple sampler for vector data.',
        license          = __license__,
        author           = __author__,
        author_email     = 'ahasimoto@mm.media.kyoto-u.ac.jp',
        url              = 'https://github.com/AtsushiHashimoto/vector_sampler.git',
        keywords         = 'random sampling',
        packages         = find_packages(),
        install_requires = [numpy],
        )
