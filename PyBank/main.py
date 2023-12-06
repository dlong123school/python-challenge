#The total number of months included in the dataset
# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
dataframe1 = pd.read_csv('./Resources/budget_data.csv')

#Get the number of rows 
numMonths = dataframe1.shape[0]
netProfit = dataframe1['Profit/Losses'].sum()

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
profitAvg = dataframe1['Profit/Losses'].mean()

#The greatest increase in profits (date and amount) over the entire period
#current minus pevious 
#The greatest decrease in profits (date and amount) over the entire period
dataframe1['Inc/Dec'] = dataframe1['Profit/Losses'] - dataframe1['Profit/Losses'].shift(1)
maxprofit = dataframe1['Inc/Dec'].max()
minprofit = dataframe1['Inc/Dec'].min()
avgchange = dataframe1['Inc/Dec'].mean()

#get index of the max and min profit in the column dataframe 
imaxprofit = dataframe1['Inc/Dec'].idxmax()
iminprofit = dataframe1['Inc/Dec'].idxmin()

#Print results to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: ",numMonths)
print("Total: $", netProfit)
print("Average Change: $", avgchange)
print("Greatest Increase in Profits: ",dataframe1['Date'][imaxprofit], maxprofit)
print("Greatest Decrease in Profits: ",dataframe1['Date'][iminprofit], minprofit)

#print results to text file 
import sys
sys.stdout = open('./Analysis/output.txt','wt')
print("Financial Analysis")
print("----------------------------")
print("Total Months: ",numMonths)
print("Total: $", netProfit)
print("Average Change: $", avgchange)
print("Greatest Increase in Profits: ",dataframe1['Date'][imaxprofit], maxprofit)
print("Greatest Decrease in Profits: ",dataframe1['Date'][iminprofit], minprofit)