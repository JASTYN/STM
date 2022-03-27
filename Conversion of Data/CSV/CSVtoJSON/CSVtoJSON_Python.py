import os
import csv
import json

cd = os.path.dirname(os.path.abspath(__file__))

# CSV IMPORT
with open(os.path.join(cd, 'MOCK_DATA.csv')) as csvfile:    
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

jsondata = json.dumps(data, indent=4)

# JSON EXPORT
with open(os.path.join(cd, 'MOCK_DATA.json'),'w') as jsonfile:
    jsonfile.write(jsondata)    

print("Successfully migrated CSV data to JSON!")
