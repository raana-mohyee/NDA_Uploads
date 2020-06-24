import pandas as pd

# load measures from project data dictionary
measures = ['TEPS', 'MAP-SR', 'CESD', 'COPE', 'CAPE']
dataDict = {m:pd.read_excel('dataPrep/HBP_NDA_DataDict.xlsx', sheet_name=m) for m in measures}

# load collected data & sort by 'subnum'
qltrcs_data = pd.read_csv('dataPrep/Healthy+Brains+Project+-+Qualtrics+Survey_April+23,+2020_09.22.csv').sort_values(by='subnum')
intvw_data = None # update when we get the database, remember to sort
Data = pd.concat([qltrcs_data, intvw_data], axis=1, sort=False)

# a function that makes the DataFrame for upload
def makeUploadDF(measure):
    global dataDict
    cols = dataDict[measure]['NDA varname']
    forUpld = pd.DataFrame(columns=cols)
    return forUpld

def getDataCollected(m):
    global dataDict
    m = dataDict[m]
    HBPvars = m['HBP varname']
    vars = {v:m.loc[m['HBP varname'] == v]['NDA varname'] for v in HBPvars} # might throw an error
    if isinstance(v, type(float('NaN'))):
        continue
    elif v == 'visit1_date':
        continue
    else:
        # get data for b

