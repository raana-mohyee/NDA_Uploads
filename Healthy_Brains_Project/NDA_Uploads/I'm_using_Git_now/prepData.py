# -*- coding: utf-8 -*-
"""
This script imports Healthy Brains Project data and organizes it for upload to the NIH Data Archive.

Created on Wed Jun 24 10:49:34 2020

@author: rmohyee
"""

import pandas as pd
import datetime as dt
import numpy as np

# load measures from project data dictionary
measures = ['TEPS', 'MAP-SR', 'CESD', 'COPE', 'CAPE']
dataDict = {m:pd.read_excel('dataPrep/HBP_NDA_DataDict.xlsx', sheet_name=m) for m in measures}

# load pseudo-GUIDs
pGUIDs = pd.read_excel('dataPrep/HBP_NDA_DataDict.xlsx', sheet_name='pseudo-GUIDs')

# load collected data & sort by 'subnum'
qltrcs_data = pd.read_csv('dataPrep/Healthy+Brains+Project+-+Qualtrics+Survey_April+23,+2020_09.22.csv', skiprows=[1, 2]).sort_values(by='subnum')
intvw_data = None # update when we get the database, remember to sort by subnum
rawData = pd.concat([qltrcs_data, intvw_data], axis=1, sort=False)