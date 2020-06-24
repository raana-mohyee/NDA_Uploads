
import pandas as pd


# load measures from project data dictionary
measures = ['TEPS', 'MAPS-SR', 'CESD', 'COPE', 'CAPE']
dataDict = {m:pd.read_excel('dataPrep/HBP_NDA_DataDict.xlsx', sheet_name=m) for m in measures}

# load collected data
qltrcs_data = pd.read_csv('dataPrep/Healthy+Brains+Project+-+Qualtrics+Survey_April+23,+2020_09.22.csv')
intvw_data = None # update when we get the database

#########################################################################################################

# a function that makes the DataFrame for upload
def makeUploadDF(df):
    """
    Takes in a dataFrame containing info from a measure from the project NDA data dictionary,
    uses the NDA variable names for the measure to populate column names in dataFrame for upload.
    """
    assert isinstance(df, pd.DataFrame), "'df' must be a Pandas DataFrame object."
    cols = df['NDA varname']
    forUpld = pd.DataFrame(columns=cols)  # might throw an error
    return forUpld


# read collected data
def readCollectedData(meas, projvars):
    """
    Takes in a dataFrame containing the project data dictionary info for a single measure, string object   that is the name of the column containing the project variable names for that measure.
    """
    assert isinstance(meas, pd.DataFrame), "'meas' must be a Pandas DataFrame object."
    assert isinstance(projvars, str), "'projvars' should be a string."

    global qltrcs_data, intvw_data
    projvars = meas[projvars]








# WORKFLOW

# for each sheet (measure) in book
for m in measures:

    # read exisiting data and populate upload spreadsheet

        # for each HBP variable (where 'HBP varname' is not empty)

            # read data in Qualtrics data download

            # copy to measure dataFrame in appropriate column


    # read missing data and populate spreadsheet with appropriate values

        # encode empty cells in upload DataFrame as with missing value if specified

        # write to .csv file

