#!/usr/bin/env python

from setuptools import setup

setup(
    name='avinit',
    version='1.3.0',
    description='Generate avatars using name initials',
    author='Sergio Oliveira',
    author_email='seocam@seocam.com',
    url='https://github.com/CraveFood/avinit',
    packages=['avinit'],
    extras_require={
        'png': ['CairoSVG>=2.5.1,<3.0.0', 'cairocffi>=1.1.0']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
    ],
)
