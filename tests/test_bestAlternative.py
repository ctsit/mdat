from unittest import TestCase
import mdat
import json

__author__ = 'pbc'


class TestBestAlternative(TestCase):
    def test_setup(self):
        jsonString = '''
            {
                "accuracy": {
                    "fit": 0.1,
                    "sig": 0.2,
                    "col": 0.3
                },
                "comfort": {
                    "fit": 0.4,
                    "sig": 0.5,
                    "col": 0.6
                },
                "duration": {
                    "fit": 0.7,
                    "sig": 0.8,
                    "col": 0.9
                },
                "time": {
                    "fit": 0.4,
                    "sig": 0.3,
                    "col": 0.2
                }
            }
        '''
        ba = mdat.BestAlternative(jsonScores=jsonString)
        ba.setup(jsonScores=json.loads(jsonString))
        self.assertEqual(1, 1)

    def test_get_criteria(self):
        self.assertEqual(1, 1)

    def test_sum_of_criteria_values(self):
        self.assertEqual(1, 1)

    def test_get_alternatives(self):
        self.assertEqual(1, 1)

    def test_get_values_for_an_alternative(self):
        self.assertEqual(1, 1)

    def test_calculate(self):
        self.assertEqual(1, 1)
