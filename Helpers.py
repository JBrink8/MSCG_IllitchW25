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
    print (values)
    # assert the sum of each new column is equal to the number of rows in the dataframe
    assert pd[values].sum().sum() == pd.shape[0]
    # drop the original column
    pd.drop(colName, axis=1, inplace=True)
    return pd

'''Print all columns starting with colName_'''
def getConvertedValues(pd, colName):
    values = pd.columns[pd.columns.str.startswith(colName + '_')]
    return values
