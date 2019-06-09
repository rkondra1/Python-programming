import urllib.request
import json

url = 'http://dummy.restapiexample.com/api/v1/employees'
val = urllib.request.urlopen(url).read().decode('UTF-8')
val = json.loads(val)
for key in val:
    print("ID is :",key['id'], "AND","Name:",key['employee_name'])```
