#The total number of months included in the dataset
# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
dataframe1 = pd.read_csv('./Resources/election_data.csv')

#Get the number of rows in dataframe
totalVotes = dataframe1.shape[0]
uniqueCand = dataframe1

cand = dataframe1['Candidate'].unique()

#print results to console
print("Election Results")
print("------------------------------")
print("Total Votes", totalVotes)
print("------------------------------")

#winner is selected when the current is greater than the previous for all previous 
winner = ""
numPrev = 0

for name in cand:
    num = dataframe1['Candidate'].value_counts()[name]
    if num > numPrev:
        winner = name
    perc = (num/totalVotes)*100
    print(name, num, perc)
    numPrev = num
print("------------------------------")
print("Winner: ", winner)
print("------------------------------")


import sys
sys.stdout = open('./Analysis/output.txt','wt')

#print results to text file 
print("Election Results")
print("------------------------------")
print("Total Votes", totalVotes)
print("------------------------------")

winner = ""
numPrev = 0

for name in cand:
    num = dataframe1['Candidate'].value_counts()[name]
    if num > numPrev:
        winner = name
    perc = (num/totalVotes)*100
    print(name, num, perc)
    numPrev = num
print("------------------------------")
print("Winner: ", winner)
print("------------------------------")