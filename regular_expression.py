# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 16:58:55 2017

@author: User
"""

import re
from datetime import datetime

series = """
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:30:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd'
"""
dt = re.compile("'[0-9/:\s]+'")
result = dt.findall(series)
print result

pydt = datetime.strptime(result[0].replace("'", ""), '%m/%d/%Y %H:%M:%S')
print pydt
print type(pydt)
