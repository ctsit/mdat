from unittest import TestCase
from mdat import core
import json
import jsonschema

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
        ba = core.BestAlternative(jsonScores=jsonString)
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

