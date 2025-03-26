import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

'''Function to convert a column of a dataframe to binary values'''
def binConvert(pd, colName, unknownCol='<Unknown>'):
    values = pd[colName].unique()
    # assert a value matches unknownCol
    assert unknownCol in values
    # convert null values to unknownCol
    pd[colName].fillna(unknownCol, inplace=True)
    # create new columns for each value - append colName_ to value
    # remove any spaces, commas, or periods from the value
    for value in values:
            pd[colName + '_' + value] = pd[colName].apply(lambda x: 1 if x == value else 0)
    # modify values to include the new columns
    values = [colName + '_' + value for value in values]
    #print (values)
    # assert the sum of each new column is equal to the number of rows in the dataframe
    assert pd[values].sum().sum() == pd.shape[0]
    # drop the original column
    pd.drop(colName, axis=1, inplace=True)
    return pd

'''Print all columns starting with colName_'''
def getConvertedValues(pd, colName):
    values = pd.columns[pd.columns.str.startswith(colName + '_')]
    return values

'''Function to replace nan values in a column with the nearest neighbor values'''
def nearestNeighborEstimate(pd, colName):
    # get the columns that are not null
    notNull = pd[pd[colName].notnull()]
    # get the columns that are null
    isNull = pd[pd[colName].isnull()]
    # create a new dataframe to store the results
    result = pd.DataFrame()
    # iterate through the columns that are null
    for index, row in isNull.iterrows():
        # calculate the distance between the row and all other rows
        distances = notNull.apply(lambda x: np.linalg.norm(x - row), axis=1)
        # find the index of the nearest neighbor
        nearest = distances.idxmin()
        # get the value of the nearest neighbor
        result = result.append(notNull.loc[nearest])
    # return the result
    return result