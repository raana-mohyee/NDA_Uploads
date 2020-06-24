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
    
    def calcAge(self, bday):
        self.intvw_date = dt.datetime.strptime(str(self.intvw_date), "%Y-%m-%d %H:%M:%S")
        bday = dt.datetime.strptime(str(bday), "%m/%d/%Y")
        age = self.intvw_date - bday
        age_in_months = round(age.days/30)
        return age_in_months
    
    def __init__(self, sid):
        global rawData, pGUIDs
        self.SID = sid # a string?
        self.pGUID = pGUIDs.query("study_ids == @sid")['pGUIDs'].iloc[0]
        self.intvw_date = rawData.query("subnum == @sid")['StartDate'].iloc[0]
        bday = rawData.query("subnum == @sid")['SD1'].iloc[0]
        self.age = self.calcAge(bday)
        self.data = rawData.query("subnum == @sid")
        self.index = self.data.index
