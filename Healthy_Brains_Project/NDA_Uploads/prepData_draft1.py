import pandas as pd

# load measures from project data dictionary
measures = ['TEPS', 'MAP-SR', 'CESD', 'COPE', 'CAPE']
dataDict = {m:pd.read_excel('dataPrep/HBP_NDA_DataDict.xlsx', sheet_name=m) for m in measures}

# load collected data -- HAVE TO SORT BY SUBNUM
qltrcs_data = pd.read_csv('dataPrep/Healthy+Brains+Project+-+Qualtrics+Survey_April+23,+2020_09.22.csv').sort_values(by='subnum')
intvw_data = None # update when we get the database, remember to sort
Data = pd.concat([qltrcs_data, intvw_data], axis=1, sort=False)

######################################
# LET'S TRY IT FOR ONE MEASURE FIRST #
######################################

# make upload dataFrame
teps_dd = dataDict['TEPS']
TEPS = pd.DataFrame(columns=teps_dd['NDA varname'])

# read collected data
for v in teps_dd['HBP varname']:
    if isinstance(v, type(float('NaN'))):
        continue
    elif v == 'visit1_date':
        continue
    else:
        dat = Data[v] # the data collected for variable 'v' (across subjects)
        TEPS[v] = dat

TEPS.to_csv('TEPS_prep_test.csv', index=False)


