import json
from Mypack import req_handler as rh
from Mypack import LoggingNeeded as LN

url = "https://edge--non-prod--cda.hirealchemy.com/process"
pay = {"jd_text": "knowledge of java and spring", "title": "Java developer"}
pay_json = json.dumps(pay)
re = "POST"
header = {'Content-type': 'application/json'}
#test = LN('info', rh(url, header, re, pay))
#print(test)
try:
    t = 22/0
except BaseException as be:
    LN('error', str(be))
