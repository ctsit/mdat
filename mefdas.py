
#!/usr/bin/env python

"""mefdas.py: Description of what foobar does."""

__author__      = "Philip Chase(pbc@ufl.edu, Chris Barnes(cpb@ufl.edu), Roy Keyes (keyes@ufl.edu), Alex Loiacono (atloiaco@ufl.edu)"
__copyright__   = "Copyright 2015, CTS-IT University of Florida"

import itertools


class fuzzyMeasure:
    '''A class to produce a fuzzy measure of based on a list of criteria'''

    def __init__(self, list_of_members=set([])):
        # initialize a class to hold all fuzzyMeasure related objects
        self.list_of_members = list_of_members


    def make_all_subsets(self,list_of_members):
        # make every possible subsets of given list_of_members
        # for size in (list_of_members):
            # use combinations to enumerate all combinations of size elements
            # append all combinations to self.data

        self.set_of_all_subsets = set([])

        for i in range(len(list_of_members),-1,-1):
            self.set_of_all_subsets.update(frozenset(itertools.combinations(list_of_members,i)))

        return sorted(self.set_of_all_subsets)

    def set_fm_for_trivial_cases(self):
        pass
        # set fuzzyMeasure for empty and complete sets
        # mu() := 0
        # mu(X) := 1

    def set_fm_for_singleton_sets(self):
        pass
        # set fuzzyMeasure for sets with exactly one member

    def set_fm_for_complex_sets(self):
        pass
        # set fuzzyMeasure for sets with 2 or more members

        # Random generation of a fuzzy measure mu on a set X
        # note: 'undefined' means we have not yet calculated and stored the value of mu for mu(foo)
        # create list of sets from X
        # shuffle list of sets of X
        # for each A in shuffled_list_X:
            # if mu(A) is undefined:
                # min := 0
                # max := 1

                # subsets_of_A = make_all_subsets(A)
                # for each B in subsets_of_A:
                    # if mu(B) is defined:
                        # min = maximum(mu(B), min)

                # for each B in X:
                    # if mu(B) is defined:
                        # case B is a superset of A :
                            # max = minimum(max, mu(B))
                            # break
                        # case other:
                            # do nothing
                    # else:
                        # mu(B) is undefined so do nothing
                # mu(A) := random value between min and max


if __name__ == "__main__":
    import sys
    mefdas(int(sys.argv[1]))