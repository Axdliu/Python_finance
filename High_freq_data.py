# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 19:52:41 2017
High Frequency Data
@author: User
"""

import numpy as np
import pandas as pd
import datetime as dt
from urllib import urlretrieve

# !!!This link does not work any more.
# The Norwegian online broker Netfonds provides tick data for a multitude of stocks
url1 = 'http://hopey.netfonds.no/posdump.php?'
url2 = 'date=%s%s%s&paper=AAPL.O&csv_format=csv'
url = url1 + url2

year = '2014'
month = '09'
days = ['22', '23', '24', '25']
# dates might need to be updated

AAPL = pd.DataFrame()
for day in days:
    AAPL = AAPL.append(pd.read_csv(url % (year, month, day),\
                                   index_col=0, header=0, parse_dates=True))
AAPL.columns = ['bid', 'bdepth', 'bdeptht', 'offer', 'odepth', 'odeptht']
# shorter colummn names

