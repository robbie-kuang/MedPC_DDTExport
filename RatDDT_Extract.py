# This program is designed to help researchers export MED-PC IV and V data from the Delay Discounting Task from one experiment to a singular Microsoft Excel file.
# This is the rat version. 
# Robbie Kuang 02/20/2025

# IMPORTANT: Change the dictionary on line 13 (after imports) according to the large reward chambers for each Animal ID. 
# Make sure to have openpyxl, pandas, and pathlib installed prior to running this script. 

from datetime import date
from pathlib import Path
import pandas as pd

# CHANGE THIS DICTIONARY EVERYTIME 
rewarddict = {"DD1": "L", "DD2": "L","DD3": "L", "DD4": "L", "DD5": "R", "DD6": "R","DD7": "R", "DD8": "R", "DD01": "L", "DD10": "L", "DD11": "L","DD12": "L", "DD13": "L", "DD14": "R", "DD15": "R","DD16": "R", "DD16": "R", "DD17": "R", "DD18": "R"}

# User inputs the file directory and the date range they want the data from
dir = Path(input("Enter file directory for folder containing all data needed to be analyzed: "))
startdate = input("Enter start date (MM/DD/YYYY): ")
enddate = input("Enter end date (MM/DD/YYYY): ")

startdate = date(int(startdate[6:]),int(startdate[:2]),int(startdate[3:5]))
enddate=date(int(enddate[6:]),int(enddate[:2]),int(enddate[3:5]))

# Create dataframe with column labels
data = pd.DataFrame(index = [], columns = ['Chamber #', 'Animal ID', 'Impulsivity','Date', 'Block', 'Trial 1 - forced', 'Trial 2 - forced', 'Trial 3', 'Trial 4', 'Trial 5', 'Trial 6', 'Trial 7', 'Trial 8', 'Total large reward presses in free trials', 'Total small reward presses in free trials', 'Omissions in free trials'])
parsingdata = ['Chamber #', 'Animal ID', '','Date', 'Block', 'Trial 1 - forced', 'Trial 2 - forced', 'Trial 3', 'Trial 4', 'Trial 5', 'Trial 6', 'Trial 7', 'Trial 8', '', '', '']

# Open files from a file directory (Folder containing all data from animals in one cohort)
for file in dir.iterdir():
    file.resolve()
    currentfile = open(file, 'r', encoding="utf-8")
    # print(currentfile.readline())
    keepgoing = True 
    while(keepgoing): # Go through each file from the folder and looks for those dates within the range 
        line = currentfile.readline()
        
        if line == '': # End search when reach the end of file
            keepgoing = False
        
        if "Start Date: " in line:
            currentdate = date((2000+(int(line[18:20]))),int(line[12:14]),int(line[15:17]))
            
            if startdate <= currentdate <= enddate:
                parsingdata[3] = str(currentdate) # Add Date to parsingdata
                currentfile.readline() # Skip End Date line
                parsingdata[1] = (currentfile.readline()[9:]).replace('\n', '') # Add Animal ID to parsingdata and drop \n, if any
                currentfile.readline() # Skip Experiment line
                currentfile.readline() # Skip Group line
                parsingdata[0] = (currentfile.readline()[5:]).replace('\n', '') # Add Chamber # to parsingdata and drop \n, if any
                
                for i in range(43): # Skips lines until trial by trial data
                    currentfile.readline()
               
                for j in range(1,5): 
                    parsingdata[4] = j # Add Block # to parsingdata
                    row = (currentfile.readline()[9:]).replace('\n', '').split('  ')
                    for k in range(len(alldata)): 
                        parsingdata[5+k] = int(float(row[k])) # Add trial data (left lever = 1, right lever = 2) to parsing data
                    data.loc[len(data)] = parsingdata
    
    currentfile.close()
    
# Change lever output (1s and 2s) to reward output (0s and 1s)
for index in data.index: 
    # Create tally to sum trial 3-8 data for another 2 columns (large reward and small reward)
    largetally = 0
    smalltally = 0
    if rewarddict[data.at[index, 'Animal ID']] == "L": 
        for i in range(8):
            if data.iat[index, 4+i] == 2: 
                data.iat[index, 4+i] = 0
                if i > 1: 
                    smalltally += 1
            elif data.iat[index, 4+i] == 1:
                if i > 1:
                    largetally += 1
            elif data.iat[index, 4+i] == 0: 
                data.iat[index, 4+i] = -1
    else: 
        for i in range(8):
            if data.iat[index, 4+i] == 1: 
                data.iat[index, 4+i] = 0
                if i > 1: 
                    smalltally += 1
            elif data.iat[index, 4+i] == 2: 
                data.iat[index, 4+i] = 1
                if i > 1: 
                    largetally +=1
            elif data.iat[index, 4+i] == 0: 
                data.iat[index, 4+i] = -1
    data.at[index, 'Total large reward presses in free trials'] = largetally
    data.at[index, 'Total small reward presses in free trials'] = smalltally
    data.at[index, 'Omissions in free trials'] = 5 - largetally - smalltally
    
# Export dataframe as Excel file
savepath = input("Enter file directory for Excel output: ")
savepath = savepath + '\output.xlsx'
Path(savepath).resolve()
data.to_excel(savepath, index = False)
