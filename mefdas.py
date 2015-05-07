
#!/usr/bin/env python

"""mefdas.py: Description of what foobar does."""

__author__      = "Philip Chase(pbc@ufl.edu, Chris Barnes(cpb@ufl.edu), Roy Keyes (keyes@ufl.edu), Alex Loiacono (atloiaco@ufl.edu)"
__copyright__   = "Copyright 2015, CTS-IT University of Florida"


class fuzzyMeasure:
    '''A class to produce a fuzzy measure of based on a list of criteria'''

    def __init__(self, number_of_criteria):
        # build a data structure to hold all possible subsets of a set of size = number_of_criteria
        self.data = []

    def set_fm_for_trivial_cases(self):
        # set fuzzyMeasure for empty and complete sets

    def set_fm_for_singleton_sets(self):
        # set fuzzyMeasure for sets with exactly one member

    def set_fm_for_complex_sets(self):
        # set fuzzyMeasure for sets with 2 or more members


if __name__ == "__main__":
    import sys
    mefdas(int(sys.argv[1]))