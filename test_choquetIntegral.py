from unittest import TestCase
import mefdas

__author__ = 'pbc'


class TestChoquetIntegral(TestCase):
  def test_get_criteria_keys_sorted_by_value(self):
    criteria = {'c1': .6, 'c2': .8, 'c3': .9, 'c4': .2}
    expected_key_order = ['c4', 'c1', 'c2', 'c3']
    ci = mefdas.ChoquetIntegral(criteria=criteria)
    ci.get_criteria_keys_sorted_by_value()
    # verify the correct attribute is set
    self.assertEqual(ci.criteria_keys_sorted_by_value, expected_key_order)
    # verify the correct array is returned is set
    self.assertEqual(ci.get_criteria_keys_sorted_by_value(), expected_key_order)

  def test_calculate(self):
    criteria = {'c1': .6, 'c2': .8, 'c3': .9, 'c4': .2}
    fuzzyMeasure = {
      frozenset(['c3', 'c4']): 0.32,
      frozenset(['c3', 'c2', 'c4']): 0.56,
      frozenset(['c3', 'c1']): 0.98,
      frozenset(['c3', 'c2']): 0.27,
      frozenset([]): 0,
      frozenset(['c3', 'c1', 'c4']): 0.98,
      frozenset(['c2']): 0.2375,
      frozenset(['c3', 'c2', 'c1', 'c4']): 1,
      frozenset(['c3', 'c2', 'c1']): 0.99,
      frozenset(['c1']): 0.325,
      frozenset(['c2', 'c1']): 0.81,
      frozenset(['c2', 'c1', 'c4']): 0.99,
      frozenset(['c4']): 0.25,
      frozenset(['c1', 'c4']): 0.97,
      frozenset(['c2', 'c4']): 0.27,
      frozenset(['c3']): 0.1875
    }
    expected_ChoquetIntegral = 0.66875
    ci = mefdas.ChoquetIntegral(criteria=criteria, fuzzyMeasure=fuzzyMeasure)
    self.assertAlmostEquals(ci.calculate(), expected_ChoquetIntegral)

    # Run second test
    criteria = {
      'c1': 0.2,
      'c2': 0.4,
      'c3': 0.1
    }

    fuzzyMeasure = {
      frozenset([]): 0,
      frozenset(['c1']): 0.391304347826087,
      frozenset(['c2']): 0.3478260869565218,
      frozenset(['c3']): 0.2608695652173913,
      frozenset(['c1', 'c2']): 0.7683779330072605,
      frozenset(['c1', 'c3']): 0.8093446720056068,
      frozenset(['c2', 'c3']): 0.41548536225285937,
      frozenset(['c1', 'c2', 'c3']): 1
    }

    expected_ChoquetIntegral = 0.2464030107
    ci2 = mefdas.ChoquetIntegral(criteria=criteria, fuzzyMeasure=fuzzyMeasure)
    self.assertAlmostEquals(ci2.calculate(), expected_ChoquetIntegral)
