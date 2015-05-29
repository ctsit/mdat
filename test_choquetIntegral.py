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
    self.assertEqual(1, 1)
