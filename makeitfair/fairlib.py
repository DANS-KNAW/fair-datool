import re
import numpy as np
import pandas as pd
import json
from io import StringIO
import os

basedir = "%s/%s" % (os.getenv("HOME"), "fair-datool")
datadir = "%s/data" % basedir
questionsfile = "sampedataset2.csv"

def readmetrics(filename):
    dataframe = pd.read_csv("%s/%s" % (datadir, filename))
    metrics = dataframe 
    metrics = metrics.replace(np.nan, '', regex=True)
    return metrics

def allmetrics():
    metrics = {}
    metrics['F'] = readmetrics('F.csv')
    metrics['I'] = readmetrics('I.csv')
    metrics['A'] = readmetrics('A.csv')
    return metrics

def readcodes(filename):
    dataframe = pd.read_csv("%s/%s" % (datadir, filename), names=['Question', 'Code','Reference'])
    codes = dataframe 
    return codes

def get_mappings(dataframe, codes):
    mapping = {}
    newcolumns = []
    for q in dataframe.columns:
        findcode = codes[codes['Question'] == q]
        if findcode['Code'].any():
            mapping[q] = findcode['Code'].values[0]
            newcolumns.append(mapping[q])
        else:
            newcolumns.append(q)
            #print "%s %s" % (q, findcode['Code'].values[0])
    return (mapping, newcolumns)

def find_datasets(df, doi):
    doikey = "Please enter the PID of the dataset you are going to review:(i.e. https://doi.org/10.1000/xyz123)"
    thisdata = df[df[doikey] == doi]
    return thisdata

def ratedata(dataframe, metrics, thisdata):
    metricscodes = ['F', 'A', 'I']
    result = {}
    for code in metricscodes:
        thismetrics = metrics[code]
        mcol = []
        for col in thismetrics.columns:
            if col in dataframe.columns:
                mcol.append(col)
        tmpdata = thisdata[mcol]
        tmpdata.ix[tmpdata.index[0]]
        tmpdata = tmpdata.replace(np.nan, '', regex=True)
        result[code] = tmpdata
    return result

def metrics_to_stars(stars, metrics):
    metricscodes = ['F', 'A', 'I']
    result = {}
    for code in metricscodes:
        thisindex = stars[code].columns
        newindex = []
        for colname in thisindex:
            newindex.append(colname)
        newindex.append(code)
        res = metrics[code][newindex]
        result[code] = res
    return result

def getstars(code, stars, metrics):
    A = metrics[code]
    B = stars[code]
    B[code] = 1
    # Merging assestment matrix with data matrix
    match = A[B.columns]

    thisstars = []
    for index1 in B.index:
        for m in match.index:
            matrix = match.ix[m].eq(B.ix[index1])
            result = matrix.drop(code)
            docheck = result.all()
            if docheck:
                thisstars.append(int(match.ix[m][code]))
    return np.array(thisstars).mean()

def fair_ranking(doi):
    metrics = allmetrics()
    codes = readcodes('Codes.csv')
    dataframe = pd.read_csv("%s/%s" % (datadir, questionsfile), delimiter=';')
    (mapping, newcols) = get_mappings(dataframe, codes)
    dataframe.columns = newcols
    thisdata = find_datasets(dataframe, doi)
    stars = ratedata(dataframe, metrics, thisdata)
    starsR = metrics_to_stars(stars, metrics)
    data = {}
    data['F'] = getstars('F', stars, metrics)
    data['A'] = getstars('A', stars, metrics)
    data['I'] = getstars('I', stars, metrics)
    data['R'] = np.array([data['F'], data['A'], data['I']]).mean()
    return data

#doi = "http://dx.doi.org/10.17632/crnmszmb8h.1"
#doi = "http://dx.doi.org/10.17632/yjrpmr5mwn.1"
#doi = "http://dx.doi.org/10.17632/nhtjgdkft4.1"
#data = fair_ranking(doi)
#print data
