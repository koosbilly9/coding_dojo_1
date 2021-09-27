import json

myRecord = {
    'name': 'Jay',
    'age': 99,
    'occupation': 'unknown',
    'previousJobs': ['plumber', 'busdriver'],
    'partner': {
        'name': 'May',
        'age': 95,
        'occupation': 'Retired',
        'previousJobs': ['plumber', 'busdriver', 'Union Rep'] }
}

j = json.dumps(myRecord)

with open('myRecord.json','w') as f:
  f.write(j)
  f.close()
