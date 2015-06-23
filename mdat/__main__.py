import json
import sys
import argparse
from core import BestAlternative

__author__ = 'pbc'


def main():
    '''
    A class to determine the best alternative given a matrix of labeled alternatives and labeled criteria.

    Input
    -----

    Input data can be in the form of a JSON string with this structure:

        {
            "accuracy": {
                "fit": 0.1,
                "sig": 0.2,
                "col": 0.3
            },
            "comfort": {
                "fit": 0.4,
                "sig": 0.5,
                "col": 0.6
            },
            "duration": {
                "fit": 0.7,
                "sig": 0.8,
                "col": 0.9
            },
            "time": {
                "fit": 0.4,
                "sig": 0.3,
                "col": 0.2
            }
        }


    Output
    ------

    Output data is either a string with the label of the best alternative or a json string in this format

    {
        "best_alternative": "fit",
        "choquet_scores": {
            "fit": 2.8,
            "sig": 1.2,
            "col": 2.0
        }
    }


    Usage:

        usage: mdat.py [-h] [-i {json}] [-o {json,brief}] [infile] [outfile]

        Select the best of two or more alternatives given responses to a list of
        criteria

        positional arguments:
          infile
          outfile

        optional arguments:
          -h, --help            show this help message and exit
          -i {json}, --input {json}
                                Specify the file type used as input. Valid types: json
          -o {json,brief}, --output {json,brief}
                                Specify the file type used as input. Valid types:
                                json, text
    '''

    # define the list of acceptable arguments
    parser = argparse.ArgumentParser(
        description='Select the best of two or more alternatives given responses to a list of criteria')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument(
        '-i',
        '--input',
        choices=['json'],
        dest='input',
        default='json',
        help='Specify the file type used as input. Valid types: json')
    parser.add_argument(
        '-o',
        '--output',
        choices=['json', 'brief'],
        dest='output',
        default='brief',
        help='Specify the file type used as input. Valid types: json, text')

    # prepare the arguments we were given
    args = parser.parse_args()

    # Prepare the input
    if args.input == 'json':
        ba = BestAlternative(jsonScores=args.infile.read())
    else:
        print "Unsupported input type"
        return()

    # generate and return the output
    if args.output == 'json':
        args.outfile.write(json.dumps(ba.calculate()) + "\n")
    elif args.output == 'brief':
        args.outfile.write(ba.calculate()['best_alternative'] + "\n")
    else:
        print "Unsupported output type"
        return()

if __name__ == "__main__":
    main()
