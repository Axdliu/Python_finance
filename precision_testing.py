# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 15:52:24 2017

It turns out the classic float-point operation problem CANNOT be solved
by decimal setup

@author: User
"""

import decimal
from decimal import Decimal

print decimal.getcontext()


a1 = 0.12345678901234567
b1 = 0.12345678901234566
print a1-b1
print Decimal(a1) - Decimal(b1)

a2 = 0.1234567890123456
b2 = 0.1234567890123455
print a2-b2
print Decimal(a2) - Decimal(b2)

decimal.getcontext().prec = 50 # higher precision than default
print Decimal(a2) - Decimal(b2)