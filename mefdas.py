
#!/usr/bin/env python

"""mefdas.py: Description of what foobar does."""

__author__ = "Philip Chase(pbc@ufl.edu, Chris Barnes(cpb@ufl.edu), " \
             "Roy Keyes (keyes@ufl.edu), Alex Loiacono (atloiaco@ufl.edu)"
__copyright__ = "Copyright 2015, CTS-IT University of Florida"

import itertools
import random

def make_all_subsets(list_of_members):
        # make every possible subsets of given list_of_members
        # for size in (list_of_members):
            # use combinations to enumerate all combinations of size elements
            # append all combinations to self.data

        set_of_all_subsets = set([])

        for i in range(len(list_of_members),-1,-1):
            for element in itertools.combinations(list_of_members,i):
                set_of_all_subsets.add(frozenset(element))

        return sorted(set_of_all_subsets)

class FuzzyMeasure:
    '''A class to produce a fuzzy measure of based on a list of criteria'''

    def __init__(self, criteria={}):
        # initialize a class to hold all fuzzyMeasure related objects
        self.set_of_all_subsets = set([])
        self.mu = ()
        self.criteria = criteria
        self.list_of_members = frozenset(criteria.keys())
        self.setup()

    def setup(self):
        if len(self.criteria) < 1 :
            return
        self.make_all_subsets()
        self.set_fm_for_trivial_cases()
        self.set_fm_for_singleton_sets()
        self.set_fm_for_complex_sets()

    def store_criteria(self, criteria):
        self.list_of_members = frozenset(criteria.keys())
        self.criteria = criteria

    def make_all_subsets(self):
        # make every possible subsets of given list_of_members
        # for size in (list_of_members):
            # use combinations to enumerate all combinations of size elements
            # append all combinations to self.data

        self.set_of_all_subsets = set([])

        for i in range(len(self.list_of_members),-1,-1):
            for element in itertools.combinations(self.list_of_members,i):
                self.set_of_all_subsets.add(frozenset(element))

        return sorted(self.set_of_all_subsets)

    def set_fm_for_trivial_cases(self):
        # set fuzzyMeasure for empty and complete sets
        # mu[] := 0
        # mu[X] := 1
        self.mu = {frozenset(): 0, self.list_of_members: 1}

    def set_fm_for_singleton_sets(self):
        '''set fuzzyMeasure for sets with exactly one member'''

        sum_of_criteria_values = 0
        for criterium in self.criteria:
            sum_of_criteria_values += self.criteria[criterium]

        for criterium in self.criteria:
            singleton_set = frozenset([criterium])
            self.mu[singleton_set] = self.criteria[criterium]/sum_of_criteria_values

    def set_fm_for_complex_sets(self):
        # set fuzzyMeasure for sets with 2 or more members

        # Random generation of a fuzzy measure mu on a set X
        # note: 'undefined' means we have not yet calculated and stored the value of mu for mu(foo)
        # create list of sets from X and shuffle the list
        list_of_all_subsets = list(self.set_of_all_subsets)
        #print(list_of_all_subsets)
        random.shuffle(list_of_all_subsets)
        #print(list_of_all_subsets)
        #print self.mu

        for A in list_of_all_subsets:
            if self.mu.get(A) is None:
                minimum_for_mu_A = 0
                maximum_for_mu_A = 1

                subsets_of_A = make_all_subsets(A)

                for B in subsets_of_A:
                    if self.mu.get(B) is not None:
                        minimum_for_mu_A = max(self.mu.get(B), minimum_for_mu_A)
                #print "minimum of " + str(A) + str(minimum_for_mu_A)

                for B in list_of_all_subsets:
                    if self.mu.get(B) is not None:
                        if B.issuperset(A):
                            maximum_for_mu_A = min(maximum_for_mu_A, self.mu.get(B))
                #print "maximum of " + str(A) + str(maximum_for_mu_A)

                self.mu[A] = random.uniform(minimum_for_mu_A,maximum_for_mu_A)
        #print self.mu


if __name__ == "__main__":
    import sys
    mefdas(int(sys.argv[1]))