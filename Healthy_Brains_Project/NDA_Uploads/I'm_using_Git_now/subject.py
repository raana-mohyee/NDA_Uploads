# -*- coding: utf-8 -*-
"""
SUBJECT CLASS

This script defines the subject class for organizing data for the Healthy Brains Project NDA Upload.
"""

class Subject():
    
    SID = None # a string
    pGUID = None # a string
    intvw_date = None # a datetime object?
    age = None# an integer
    data = None # a DataFrame with one row
    index = None # a panda Int64 obj, behaves like an integer
