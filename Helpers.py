import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.impute import KNNImputer

'''Function to convert a column of a dataframe to binary values'''
def binConvert(df, colName, unknownCol='<Unknown>'):
    # Convert null values to unknownCol
    df[colName].fillna(unknownCol, inplace=True)
    # Get unique values in the column
    values = df[colName].unique()
    # Ensure unknownCol is in the unique values
    assert unknownCol in values
    # Sanitize column names and create new binary columns
    for value in values:
        sanitized_value = ''.join(e for e in value if e.isalnum() or e == '_')
        new_col_name = f"{colName}_{sanitized_value}"
        df[new_col_name] = df[colName].apply(lambda x: 1 if x == value else 0)
    # Drop the original column
    df.drop(colName, axis=1, inplace=True)
    return df

'''Print all columns starting with colName_'''
def getConvertedValues(df, colName):
    values = df.columns[df.columns.str.startswith(colName + '_')]
    return values

'''
Function to use KNNImputer to fill in missing values
for a list of columns in a dataframe
Note: this function is for use with numerical columns
'''
def nearestNeighborEstimate(df, colNames, neighbors=2):
    knn_imputer = KNNImputer(n_neighbors=neighbors)
    if isinstance(colNames, str):
        colNames = [colNames]
    df_subset = df[colNames]
    df_imputed = pd.DataFrame(knn_imputer.fit_transform(df_subset), columns=colNames)
    df.update(df_imputed)
    return df