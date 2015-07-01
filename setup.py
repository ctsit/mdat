from setuptools import setup

# @see https://pythonhosted.org/setuptools/setuptools.html

setup(
    name='mdat',
    version='0.3.0',
    packages=['mdat'],
    url='https://github.com/ctsit/mdat',
    license='Apache 2.0',
    author='pbc',
    author_email='ctsit@ctsi.ufl.edu',
    description='A decision aid designed to select the best of two or more alternatives given responses to a list of criteria',
    long_description=open('README.md').read(),
    install_requires=[
        "jsonschema == 2.5.1",
    ],
    entry_points={
        'console_scripts': [
            'mdat = mdat.__main__:main',
        ],
    },
    tests_require=[
        "jsonschema == 2.5.1",
    ],
    test_suite='tests',
)
