with open("testjason.json","r") as f:
    b = f.read()
    print(b)
    f.close()
 ##################################

import json
import pprint
with open("company1.json","r") as f:
    b = json.loads(f.read())
    print(b)
    f.close()
