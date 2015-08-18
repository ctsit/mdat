# MDAT

## Medical Decision Aid Tool

Master branch: [![Build Status](https://travis-ci.org/ctsit/mdat.svg?branch=master)](https://travis-ci.org/ctsit/mdat)
[![Coverage Status](https://coveralls.io/repos/ctsit/mdat/badge.svg?branch=master&service=github)](https://coveralls.io/github/ctsit/mdat?branch=master)

Develop branch: [![Build Status](https://travis-ci.org/ctsit/mdat.svg?branch=develop)](https://travis-ci.org/ctsit/mdat)
[![Coverage Status](https://coveralls.io/repos/ctsit/mdat/badge.svg?branch=develop&service=github)](https://coveralls.io/github/ctsit/mdat?branch=develop)

The MDAT is a set of software libraries to implement a _medical decision aid_.  These libraries are designed to select the best of two or more alternatives given responses to a list of criteria.

## Installation

To install from source, use setup.py

    python setup.py install

## Usage Instructions

_mdat --help_ provides current usage instructions:

    usage: mdat [-h] [-i {json}] [-o {json,brief,csv,csvnoheader}]
                [infile] [outfile]

    Select the best of two or more alternatives given responses to a list of
    criteria

    positional arguments:
      infile
      outfile

    optional arguments:
      -h, --help            show this help message and exit
      -i {json}, --input {json}
                            Specify the file type used as input. Valid types: json
      -o {json,brief,csv,csvnoheader}, --output {json,brief,csv,csvnoheader}
                            Specify the file type used as input. Valid types:
                            json, brief, csv, csvnoheader

## Input data

Sample input data should be a json file with two or more labeled alternatives, one or more labeled criteria, and the numeric responses to each criteria for each alternative.  This example input file shows response data for 4 criteria that could be used to determine the preferred type of colorectal cancer screening:

    {
        "Accuracy": {
            "Fecal Immunochemical Test": 0.1,
            "Flexible Sigmoidoscopy": 0.2,
            "Colonoscopy": 0.3
        },
        "Amount of colon examined": {
            "Fecal Immunochemical Test": 0.5,
            "Flexible Sigmoidoscopy": 0.7,
            "Colonoscopy": 0.8
        },
        "Complications": {
            "Fecal Immunochemical Test": 0.2,
            "Flexible Sigmoidoscopy": 0.1,
            "Colonoscopy": 0.9
        },
        "Cost": {
            "Fecal Immunochemical Test": 0.4,
            "Flexible Sigmoidoscopy": 0.8,
            "Colonoscopy": 0.9
        },
        "Discomfort": {
            "Fecal Immunochemical Test": 0.1,
            "Flexible Sigmoidoscopy": 0.3,
            "Colonoscopy": 0.9
        },
        "Sedation": {
            "Fecal Immunochemical Test": 1.0,
            "Flexible Sigmoidoscopy": 0.8,
            "Colonoscopy": 0.9
        },
        "Test Preparation": {
            "Fecal Immunochemical Test": 0.1,
            "Flexible Sigmoidoscopy": 0.2,
            "Colonoscopy": 1.0
        }
    }

## Output data

mdat can output data in three formats.

    $ mdat sample_data/test.json
    Colonoscopy

    $ mdat -o csv sample_data/test.json
    Fecal Immunochemical Test,Flexible Sigmoidoscopy,Colonoscopy
    0.4403085839715581,0.4472662851726272,0.887231735365237

    $ mdat -o json sample_data/test.json
    {"best_alternative": "Colonoscopy", "choquet_scores": {"Fecal Immunochemical Test": 0.43414030720240016, "Flexible Sigmoidoscopy": 0.4729342460226981, "Colonoscopy": 0.9068722937866821}}

## Requirements

This project requires Python 2.7 or greater.

This project uses Travis CI for automated testing. Please revise the .travis.yml to reflect any changes in required libraries as changes are made to the software.

## Contributions

The MDAT Team welcomes contributions to this project. Please fork and send pull requests with your revisions. Any code changes must be accompanied by corresponding unit tests to be accepted. Please configure your account at https://travis-ci.org to test your commits to your fork so you get quick feedback on any issues created by your changes.
