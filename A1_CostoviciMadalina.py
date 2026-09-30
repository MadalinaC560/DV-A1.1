import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# https://towardsdatascience.com/create-stunning-radar-plots-with-matplotlib-6a8e05054ff9/

# Styles for radar plots (remember to pip install first)
# https://towardsdatascience.com/upgrade-your-data-visualisations-4-python-libraries-to-enhance-your-matplotlib-charts-74361bc3b92e/?source=collection_tagged---------0----------------------------

data = pd.read_csv('farr.csv')

# Converting the data to numeric values and replacing missing values with 0
data["deaths"] = pd.to_numeric(data["deaths"], errors='coerce').fillna(0)
data["mean_temperature"] = pd.to_numeric(data["mean_temperature"], errors='coerce').fillna(0)
data["mortality_reference"] = pd.to_numeric(data["mortality_reference"], errors='coerce').fillna(0)
data["temperature_reference"] = pd.to_numeric(data["temperature_reference"], errors='coerce').fillna(0)

years = data["year"]
weekEnd = data["week_ending"]
deaths = data["deaths"]
meanTemp = data["mean_temperature"]
mortRef = data["mortality_reference"]
tempRef = data["temperature_reference"]

chartSegments = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
yearStart = 1840

# Function that extracts the deaths from a specific year
def extractDeathsfromYear(year):
    return deaths[years == year].tolist()

# Function that extracts the mean temperature from a specific year
def extractMeanTempfromYear(year):
    return meanTemp[years == year].tolist()

# Function that extracts the mortality reference from a specific year
def extractMortReffromYear(year):
    return mortRef[years == year].tolist()

# Function that extracts the temperature reference from a specific year
def extractTempReffromYear(year):
    return tempRef[years == year].tolist()

# Function that appends an element to the end of a list to create closed radar plots
def appendElementToEndOfList(inputList):
    if not inputList:
        return []

    newList = list(inputList)
    newList.append(newList[0])
    return newList

def buildRadarPlot(year, deathsInYear, meanTempInYear, mortRefInYear, tempRefInYear, segments):
    deathsInYear = extractDeathsfromYear(year)
    meanTempInYear = extractMeanTempfromYear(year)
    mortRefInYear = extractMortReffromYear(year)
    tempRefInYear = extractTempReffromYear(year)

    # Scaling the meanTemp and tempRef to match scale of deaths and mortRef for better visualization
    meanTempInYear = [t * 30 for t in meanTempInYear]
    tempRefInYear = [t * 30 for t in tempRefInYear]

    deathsInYear = appendElementToEndOfList(deathsInYear)
    meanTempInYear = appendElementToEndOfList(meanTempInYear)
    mortRefInYear = appendElementToEndOfList(mortRefInYear)
    tempRefInYear = appendElementToEndOfList(tempRefInYear)
    segments = appendElementToEndOfList(segments)

    label_loc = np.linspace(0, 2 * np.pi, num = len(segments))

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize = (10, 10), subplot_kw = dict(polar = True))
    ax.set_facecolor('#212946')
    fig.patch.set_facecolor('#181C2B')

    ax.plot(label_loc, deathsInYear, label = "Deaths", color = "deeppink", linewidth = 1, marker = 'o', markersize = 2)
    ax.plot(label_loc, meanTempInYear, label = "Mean Temperature", color = "deepskyblue", linewidth = 1, marker = 'o', markersize = 2)
    ax.plot(label_loc, mortRefInYear, label = "Mortality Reference", color = "limegreen", linewidth = 1, marker = 'o', markersize = 2)
    ax.plot(label_loc, tempRefInYear, label = "Temperature Reference", color = "orange", linewidth = 1, marker = 'o', markersize = 2)

    # Add semi-transparent fills (alpha=0.12 keeps it subtle so they don't block each other)
    ax.fill(label_loc, deathsInYear, color="deeppink", alpha=0.12)
    ax.fill(label_loc, meanTempInYear, color="deepskyblue", alpha=0.12)
    ax.fill(label_loc, mortRefInYear, color="limegreen", alpha=0.12)
    ax.fill(label_loc, tempRefInYear, color="orange", alpha=0.12)

    lines, labels = plt.thetagrids(np.degrees(label_loc), labels = segments)
    ax.grid(color='#2A3459', linestyle='--', linewidth=0.8)

    legend = plt.legend(loc = "upper right", bbox_to_anchor=(1.1, 1.1), framealpha = 1, facecolor ='#181C2B', edgecolor = 'none')
    plt.setp(legend.get_texts(), color='w')
    
    plt.title(str(year), size = 20, color = "white", y = 1.1)
    plt.show()

for m in range(0, 11):
    buildRadarPlot(yearStart, deaths, meanTemp, mortRef, tempRef, chartSegments)
    yearStart += 1
    m += 1