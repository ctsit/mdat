
#!/usr/bin/env python

"""mefdas.py: Description of what foobar does."""

__author__ = "Philip Chase(pbc@ufl.edu, Chris Barnes(cpb@ufl.edu), " \
             "Roy Keyes (keyes@ufl.edu), Alex Loiacono (atloiaco@ufl.edu)"
__copyright__ = "Copyright 2015, CTS-IT University of Florida"

import itertools
import random
import operator

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
        self.set_of_all_subsets = make_all_subsets(self.list_of_members)

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
        random.shuffle(list_of_all_subsets)

        for A in list_of_all_subsets:
            if self.mu.get(A) is None:
                minimum_for_mu_A = 0
                maximum_for_mu_A = 1

                subsets_of_A = make_all_subsets(A)

                for B in subsets_of_A:
                    if self.mu.get(B) is not None:
                        minimum_for_mu_A = max(self.mu.get(B), minimum_for_mu_A)

                for B in list_of_all_subsets:
                    if self.mu.get(B) is not None:
                        if B.issuperset(A):
                            maximum_for_mu_A = min(maximum_for_mu_A, self.mu.get(B))

                self.mu[A] = random.uniform(minimum_for_mu_A,maximum_for_mu_A)

class ChoquetIntegral:
    ''' A class to calculate the Choquet Integral given a dictionary of criteria and a related fuzzy measure.

        Inputs
        ------
        The keys in the dictionary of criteria must match the names of the set members used to generate
        the keys to the fuzzy measure values. e.g. the keys in these criteria

            {
                'c1': 0.2,
                'c2': 0.4,
                'c3': 0.1
            }

        could be used to generate the frozensets that are used as the key values to look up values in this dictionary
        of fuzzy measures

            {
                frozenset([]): 0,
                frozenset(['c1']): 0.391304347826087,
                frozenset(['c2']): 0.3478260869565218,
                frozenset(['c3']): 0.2608695652173913,
                frozenset(['c1', 'c2']): 0.7683779330072605,
                frozenset(['c1', 'c3']): 0.8093446720056068,
                frozenset(['c2', 'c3']): 0.41548536225285937,
                frozenset(['c1', 'c2', 'c3']): 1
            }

        Outputs
        ------
        The class returns a single real number that is the Choquet Integral.  This value is a product of the
        differences between sorted criteria values and the corresponding fuzzy measures.

    '''

    def __init__(self,criteria={}, fuzzyMeasure={}):
        '''instantiate a Choquet Integral object'''
        self.criteria = criteria
        self.mu = fuzzyMeasure

    def get_criteria_keys_sorted_by_value(self):
        '''create the attribute, sigma, a list of criteria sorted by value'''
        self.criteria_keys_sorted_by_value = []

        # sort the criteria by value
        criteria_sorted_by_value = sorted(self.criteria.items(), key=operator.itemgetter(1))

        # make a list of the criteria keys in the
        for criterium in criteria_sorted_by_value:
            self.criteria_keys_sorted_by_value.append(criterium[0])

        return self.criteria_keys_sorted_by_value

    def calculate(self):
        '''Calculate the Choquet Integral and return just that value'''
        pass



if __name__ == "__main__":
    import sys
    mefdas(int(sys.argv[1]))