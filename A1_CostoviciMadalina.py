import matplotlib as mpl
import numpy as np
import pandas as pd

# https://towardsdatascience.com/create-stunning-radar-plots-with-matplotlib-6a8e05054ff9/

data = pd.read_csv('farr.csv')

years = data["year"]
weekEnd = data["week_ending"]
deaths = data["deaths"]
meanTemp = data["mean_temperature"]
mortRef = data["mortality_reference"]
tempRef = data["temperature_reference"]

chartSegments = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

# replacing missing data with 0 to avoid errors when plotting (Data is not corrected)
for i in range(len(deaths)):
    if deaths[i] == "?":
        deaths[i] = 0

# replacing missing data with 0 to avoid errors when plotting (Data is not corrected)
for j in range(len(meanTemp)):
    if meanTemp[j] == "?":
        meanTemp[j] = 0

def extractDeathsfromYear(year):
    deathsFromYear = []
    counter = 0
    if years[counter] == year:
        deathsFromYear.append(deaths[counter])
        counter += 1
    else:
        return deathsFromYear

def extractMeanTempfromYear(year):
    meanTempFromYear = []
    counter = 0
    if years[counter] == year:
        meanTempFromYear.append(meanTemp[counter])
        counter += 1
    else:
        return meanTempFromYear

def extractMortReffromYear(year):
    mortRefFromYear = []
    counter = 0
    if years[counter] == year:
        mortRefFromYear.append(mortRef[counter])
        counter += 1
    else:
        return mortRefFromYear

def extractTempReffromYear(year):
    tempRefFromYear = []
    counter = 0
    if years[counter] == year:
        tempRefFromYear.append(tempRef[counter])
        counter += 1
    else:
        return tempRefFromYear



