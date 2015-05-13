from unittest import TestCase
import mefdas

__author__ = 'pbc'


class TestFuzzyMeasure(TestCase):
    def test_make_all_subsets(self):
        mu = mefdas.fuzzyMeasure(3)
        a = set(['a','b','c','d','e','f','g','h','i','j','k','l','m'])
        mu.make_all_subsets(a)
        self.assertEqual(len(mu.set_of_all_subsets), 2**len(a))

    def test_set_fm_for_trivial_cases(self):
        self.assertEqual(1,1)

    def test_set_fm_for_singleton_sets(self):
        self.assertEqual(1,1)
