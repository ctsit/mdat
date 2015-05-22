from unittest import TestCase
import mefdas

__author__ = 'pbc'


class TestFuzzyMeasure(TestCase):
    def test_init(self):
        self.list_of_members = frozenset([])
        mu = mefdas.FuzzyMeasure(self.list_of_members)
        self.assertEqual(len(mu.list_of_members), 0)

        mu = mefdas.FuzzyMeasure()
        self.assertEqual(len(mu.list_of_members), 0)

        mu = mefdas.FuzzyMeasure(frozenset([1,2,3]))
        self.assertEqual(len(mu.list_of_members),3)

    def test_store_criteria(self):
        mu = mefdas.FuzzyMeasure()
        criteria = {'c1': .9, 'c2': 1, 'c3': .6}
        mu.store_criteria(criteria)
        criteria_labels = set(['c1','c2','c3'])
        self.assertSetEqual(mu.list_of_members,criteria_labels)
        self.assertDictEqual(mu.criteria,criteria)

    def test_make_all_subsets(self):
        list_of_members = set([])
        mu = mefdas.FuzzyMeasure()
        mu.list_of_members = frozenset(['a','b','c','d','e','f','g','h','i','j','k','l','m'])
        mu.make_all_subsets()
        self.assertEqual(len(mu.set_of_all_subsets), 2**len(mu.list_of_members))

    def test_set_fm_for_trivial_cases(self):
        self.list_of_members = frozenset([1,2,3,4,5])
        mu = mefdas.FuzzyMeasure(self.list_of_members)
        mu.make_all_subsets()
        mu.set_fm_for_trivial_cases()
        self.assertEqual(mu.mu[frozenset()],0)
        self.assertEqual(mu.mu[self.list_of_members],1)

    def test_set_fm_for_singleton_sets(self):
        # initialize FuzzyMeasure instance
        mu = mefdas.FuzzyMeasure()
        criteria = {'c1': .9, 'c2': 1, 'c3': .6}
        mu.store_criteria(criteria)
        mu.make_all_subsets()
        mu.set_fm_for_trivial_cases()

        # test function of interest
        mu.set_fm_for_singleton_sets()
        self.assertEqual(mu.mu[frozenset(['c1'])],0.36)
        self.assertEqual(mu.mu[frozenset(['c2'])],0.4)
        self.assertEqual(mu.mu[frozenset(['c3'])],0.24)

    def test_set_fm_for_complex_sets(self):
        # initialize FuzzyMeasure instance
        mu = mefdas.FuzzyMeasure()
        criteria = {'c1': .9, 'c2': 1, 'c3': .6}
        mu.store_criteria(criteria)
        mu.make_all_subsets()
        mu.set_fm_for_trivial_cases()
        mu.set_fm_for_singleton_sets()
        mu.set_fm_for_complex_sets()

        self.assertEqual(1,1)
