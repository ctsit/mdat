from unittest import TestCase
from mdat import core
import json
import jsonschema
from decimal import Decimal

__author__ = 'pbc'

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

class TestBestAlternative(TestCase):
    def test_setup(self):
        ba = core.BestAlternative(jsonScores=jsonString)
        ba.setup(jsonScores=json.loads(jsonString))
        self.assertEqual(1, 1)

    def test_get_criteria(self):
        ba = core.BestAlternative(jsonScores=jsonString)
        ba.setup(jsonScores=json.loads(jsonString))
        list_of_criteria = ba.get_criteria()
        expected_output = [u'accuracy', u'comfort', u'duration', u'time']
        self.assertEqual(len(ba.get_criteria()),4)
        self.assertEqual(sorted(list_of_criteria),expected_output)

    def test_sum_of_criteria_values(self):
        ba = core.BestAlternative(jsonScores=jsonString)
        ba.setup(jsonScores=json.loads(jsonString,parse_float=Decimal))
        dict_of_sums = ba.sum_of_criteria_values()
        expected_output = {u'duration': Decimal('2.4'), u'comfort': Decimal('1.5'), u'accuracy': Decimal('0.6'), u'time': Decimal('0.9')}
        self.assertEqual(dict_of_sums, expected_output)

    def test_get_alternatives(self):
        ba = core.BestAlternative(jsonScores=jsonString)
        ba.setup(jsonScores=json.loads(jsonString))
        list_of_alternatives = ba.get_alternatives()
        expected_output = [u'sig', u'col', u'fit']
        self.assertEqual(list_of_alternatives,expected_output)

    def test_get_values_for_an_alternative(self):
        ba = core.BestAlternative(jsonScores=jsonString)
        ba.setup(jsonScores=json.loads(jsonString))
        col_values = {u'duration': Decimal('0.9'), u'comfort': Decimal('0.6'), u'accuracy': Decimal('0.3'), u'time': Decimal('0.2')}
        fit_values = {u'duration': Decimal('0.7'), u'comfort': Decimal('0.4'), u'accuracy': Decimal('0.1'), u'time': Decimal('0.4')}
        sig_values = {u'duration': Decimal('0.8'), u'comfort': Decimal('0.5'), u'accuracy': Decimal('0.2'), u'time': Decimal('0.3')}
        self.assertEqual(ba.get_values_for_an_alternative('sig'),sig_values)
        self.assertEqual(ba.get_values_for_an_alternative('fit'),fit_values)
        self.assertEqual(ba.get_values_for_an_alternative('col'),col_values)

    def test_calculate(self):
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

        ba = core.BestAlternative(jsonScores=jsonString)
        asserted_result = '''
            {
                "best_alternative": "fit",
                "choquet_scores": {
                    "fit": 2.8,
                    "sig": 1.2,
                    "col": 2.0
                }
            }
        '''
        result = ba.calculate()
        schema = '''
            {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "title": "mdat output",
                "description": "An output data set for the Medical Decision Aids Tool python library",
                "type": "object",
                "required" : [ "best_alternative", "choquet_scores" ],
                "properties" : {
                    "best_alternative" : {
                        "description": "the name best alternative suggested by the matrix of responses",
                        "type" : "string"
                    },
                    "choquet_scores" : {
                        "description": "a list of alternatives with the Choquet Integral score for each",
                        "type" : "object",
                        "patternProperties": {
                            "^.+$": {
                                "type": "number",
                                "minimum" : 0
                            }
                        },
                        "minProperties": 2
                    }
                }
            }
        '''
        try:
            jsonschema.validate(json.loads(json.dumps(result)), json.loads(schema))
            self.assertEqual(1, 1)
        except jsonschema.ValidationError as e:
            self.assertEqual("", e.message, msg=e.message)
        except jsonschema.SchemaError as e:
            self.assertEqual("", e.message, msg=e.message)

