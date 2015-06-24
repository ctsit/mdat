from setuptools import setup

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
        "jsonschema",
    ],
    entry_points={
        'console_scripts': [
            'mdat = mdat.__main__:main',
        ],
    },
    tests_require=[
        "pytest",
        "jsonschema",
    ],
    test_suite='tests',
)
