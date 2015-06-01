import json

jsonstring = '''{
    "scores": {
        "accuracy": {
            "fit": "0.1",
            "sig": "0.2",
            "col": "0.3"
        },
        "comfort": {
            "fit": "0.1",
            "sig": "0.2",
            "col": "0.3"
        },
        "duration": {
            "fit": "0.1",
            "sig": "0.2",
            "col": "0.3"
        },
        "time": {
            "fit": "0.1",
            "sig": "0.2",
            "col": "0.3"
        }
    }
}'''

print json.loads(jsonstring)


