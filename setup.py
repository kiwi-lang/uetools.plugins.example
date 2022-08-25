#!/usr/bin/env python
from setuptools import setup

if __name__ == '__main__':
    setup(
        name='uetools.plugins.myplugin',
        version='0.0.0',
        description='uetools plugin example',
        author='Pierre Delaunay',
        packages=[
            'uetools.plugins.myplugin',
        ],
        install_requires=['uetools', 'simple-parsing'],
        setup_requires=['setuptools'],
        zip_safe=False,
        namespace_packages=['uetools.plugins'],
        entry_points={
            "UECLICommands": ["command = uetools.plugins.myplugin.command:MyNewCommand"],
        },
    )
