from unittest import TestCase
import mefdas

__author__ = 'pbc'


class TestFuzzyMeasure(TestCase):
    def test_init(self):
        self.list_of_members = set([])
        mu = mefdas.fuzzyMeasure(self.list_of_members)
        self.assertEqual(len(mu.set_of_all_subsets), 1)

        mu = mefdas.fuzzyMeasure()
        self.assertEqual(len(mu.set_of_all_subsets), 1)

        self.list_of_members = set([1,2,3,4,5])
        mu = mefdas.fuzzyMeasure(self.list_of_members)
        self.assertEqual(len(mu.set_of_all_subsets), 2**len(self.list_of_members))

    def test_make_all_subsets(self):
        list_of_members = set([])
        mu = mefdas.fuzzyMeasure()
        print(mu.set_of_all_subsets)
        a = set(['a','b','c','d','e','f','g','h','i','j','k','l','m'])
        mu.make_all_subsets(a)
        self.assertEqual(len(mu.set_of_all_subsets), 2**len(a))

    def test_set_fm_for_trivial_cases(self):
        self.assertEqual(1,1)

    def test_set_fm_for_singleton_sets(self):
        self.assertEqual(1,1)
