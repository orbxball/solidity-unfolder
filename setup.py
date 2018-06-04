from setuptools import setup
from setuptools import find_packages


with open('README.md') as f:
    long_description = f.read()

setup(
    name='solidity-unfolder',
    packages=find_packages(),

    description='A Python package to unfold soldity code with imports into a single file.',
    long_description=long_description,
    long_description_content_type='text/markdown',


    author='Jun-You Liu',
    author_email='junyouliu9@gmail.com',

    url='https://github.com/Jy-Liu/solidity-unfolder',
    version='1.0.1',
    license='MIT',

    keywords='soldity solidity-unfolder solidity-flattener \
              smart-contracts ethereum',

    install_requires=[],
    scripts=['bin/solu'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    python_requires='>=3',
)
