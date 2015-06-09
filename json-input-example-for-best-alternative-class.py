import json

jsonstring = '''
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

print json.loads(jsonstring)


