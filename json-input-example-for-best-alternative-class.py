import json

jsonstring = '''
{
    "accuracy": {
        "fit": 0.1,
        "sig": 0.2,
        "col": 0.3
    },
    "comfort": {
        "fit": 0.1,
        "sig": 0.2,
        "col": 0.3
    },
    "duration": {
        "fit": 0.1,
        "sig": 0.2,
        "col": 0.3
    },
    "time": {
        "fit": 0.1,
        "sig": 0.2,
        "col": 0.3
    }
}
'''

jsonDict = json.loads(jsonstring)

list_of_criteria = jsonDict.keys()

print list_of_criteria

dict_of_sums = {}

for criteria in list_of_criteria:
    dict_of_sums[criteria] = sum(jsonDict[criteria].values())

print dict_of_sums