from unittest import TestCase
import mefdas

__author__ = 'pbc'


class TestFuzzyMeasure(TestCase):
    def test_init(self):
        # self.list_of_members = frozenset([])
        fm = mefdas.FuzzyMeasure()
        self.assertEqual(len(fm.list_of_members), 0)

        fm = mefdas.FuzzyMeasure()
        self.assertEqual(len(fm.list_of_members), 0)

        criteria = {'c1': .9, 'c2': 1, 'c3': .6}
        fm = mefdas.FuzzyMeasure(criteria)
        self.assertEqual(len(fm.list_of_members),3)

    def test_store_criteria(self):
        fm = mefdas.FuzzyMeasure()
        criteria = {'c1': .9, 'c2': 1, 'c3': .6}
        fm.store_criteria(criteria)
        criteria_labels = set(['c1','c2','c3'])
        self.assertSetEqual(fm.list_of_members,criteria_labels)
        self.assertDictEqual(fm.criteria,criteria)

    def test_make_all_subsets(self):
        list_of_members = set([])
        fm = mefdas.FuzzyMeasure()
        fm.list_of_members = frozenset(['a','b','c','d','e','f','g','h','i','j','k','l','m'])
        fm.make_all_subsets()
        self.assertEqual(len(fm.set_of_all_subsets), 2**len(fm.list_of_members))

    def test_set_fm_for_trivial_cases(self):
        fm = mefdas.FuzzyMeasure()
        fm.list_of_members = frozenset([1,2,3,4,5])
        fm.make_all_subsets()
        fm.set_fm_for_trivial_cases()
        self.assertEqual(fm.mu[frozenset([])],0)
        self.assertEqual(fm.mu[fm.list_of_members],1)

    def test_set_fm_for_singleton_sets(self):
        # initialize FuzzyMeasure instance
        fm = mefdas.FuzzyMeasure()
        criteria = {'c1': .9, 'c2': 1, 'c3': .6}
        fm.store_criteria(criteria)
        fm.make_all_subsets()
        fm.set_fm_for_trivial_cases()

        # test function of interest
        fm.set_fm_for_singleton_sets()
        self.assertEqual(fm.mu[frozenset(['c1'])],0.36)
        self.assertEqual(fm.mu[frozenset(['c2'])],0.4)
        self.assertEqual(fm.mu[frozenset(['c3'])],0.24)

    def test_set_fm_for_complex_sets(self):
        # initialize FuzzyMeasure instance
        criteria = {'c1': .9, 'c2': .8, 'c3': .6, 'c4': .2}
        fm = mefdas.FuzzyMeasure(criteria)
        #print fm.mu

        self.assertEqual(1, 1)
