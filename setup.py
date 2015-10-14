from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'readme.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytestor',
    version='0.1',
    description='A helping hand migrating to pytest',
    long_description=long_description,
    url='https://github.com/switch87/pytestor',
    author='Gert Pellin (switch87)',
    author_email='pellingert@gmail.com',
    license='GPL version 2',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing Tools',
        'License :: OSI Approved :: GPL version 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='pytest unittest development',

    install_requires=['termcolor',],
    extras_require={
        'dev': [],
        'test': ['pytest'],
    },

    entry_points={
        'console_scripts': [
            'pytestor=pytestor',
        ]
    }
)
