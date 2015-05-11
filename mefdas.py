
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
        # mu(∅) := 0
        # mu(X) := 1

    def set_fm_for_singleton_sets(self):
        # set fuzzyMeasure for sets with exactly one member

    def set_fm_for_complex_sets(self):
        # set fuzzyMeasure for sets with 2 or more members

        # Random generation of a fuzzy measure mu on a set X
        # note: 'undefined' means we have not yet calculated and stored the value of mu for mu(foo)
        # copy list of subsets X to my_x
        # for each A popped randomly from my_x:
            # if mu(A) is undefined:
                # min := 0
                # max := 1
                # for each B in X:
                    # case B ⊂ A :
                        # if mu(B) is defined:
                            # mu(B) = max(mu(B), min)
                    # case B ⊃ A :
                        # if mu(B) is defined:
                            # mu(B) = min(max, mu(B))
                    # else:
                        # do nothing
                # mu(A) := random value between min and max


if __name__ == "__main__":
    import sys
    mefdas(int(sys.argv[1]))