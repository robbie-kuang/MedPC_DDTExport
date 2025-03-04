# MedPC DDT Export
This project is designed to help researchers parse and extract trial-by-trial data from MED-PC IV and V. Users can select a file directory to batch process data (e.g., put all data from one cohort into a folder) and a date range. The Python program will find the relevant data and export them to an Excel file. It will also calculate Large Reward Presses, Small Reward Presses, and Omissions. Note that there are separare files for mouse and rat DDT. This is only because mouse and rat DDT have different number of trials and blocks. You may also edit the code to accomodate the paradigm used in your lab. Please don't hesitate to reach out if you have any questions regarding that, I'm happy to help.

_How this may help you:_ You can use this to streamline and automate your data collection process, but it may also help broaden the analysis you can perform on your data! Our lab needed the trial-by-trial data to use machine learning techniques to quantify impulsivity behavior in rodents. 

## Instructions
1. Make sure to have openpyxl, pandas, and pathlib installed prior to running this script.
2. Create a folder with all the MED-PC data files you wish to process
3. Open either the mouse or rat extract code. Set the dictionary called "rewarddict" on ln 13 based on the large reward levers (left or right) of your experiment: {"SubjID":"L", "SubjID":"R", ...}
5. Run the code! Make sure to type in file paths and dates in the correct format as instructed


In the _SampleMedPCFiles_ folder: 
_SampleDDTTemplate_ --> Sample MED-PC macro for DDT

_SampleInput.DAT_ --> Sample MED-PC data output (i.e., input for this program)

_SampleOutput.xlsx_ --> Sample output from my mouse DDT extract


Feel free to reach out to hykuang4@gmail.com with any questions.
