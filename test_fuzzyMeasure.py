from unittest import TestCase
import mefdas

__author__ = 'pbc'


class TestFuzzyMeasure(TestCase):
    def test_init(self):
        self.list_of_members = set([])
        mu = mefdas.fuzzyMeasure(self.list_of_members)
        self.assertEqual(len(mu.list_of_members), 0)

        mu = mefdas.fuzzyMeasure()
        self.assertEqual(len(mu.list_of_members), 0)

        mu = mefdas.fuzzyMeasure(set([1,2,3]))
        self.assertEqual(len(mu.list_of_members),3)

    def test_store_criteria(self):
        mu = mefdas.fuzzyMeasure()
        criteria = {'c1': .9, 'c2': 1, 'c3': .6}
        mu.store_criteria(criteria)
        criteria_labels = set(['c1','c2','c3'])
        self.assertSetEqual(mu.list_of_members,criteria_labels)
        self.assertDictEqual(mu.criteria,criteria)

    def test_make_all_subsets(self):
        list_of_members = set([])
        mu = mefdas.fuzzyMeasure()
        mu.list_of_members = set(['a','b','c','d','e','f','g','h','i','j','k','l','m'])
        mu.make_all_subsets()
        self.assertEqual(len(mu.set_of_all_subsets), 2**len(mu.list_of_members))

    def test_set_fm_for_trivial_cases(self):
        self.assertEqual(1,1)

    def test_set_fm_for_singleton_sets(self):
        self.assertEqual(1,1)
