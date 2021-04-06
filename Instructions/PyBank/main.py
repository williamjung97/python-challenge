# Creating file paths across OS
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Create empty lists for the values in CSV file
months = [] 
profit = []
profit_change = []

# Opening the CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read Header
    csv_header = next(csvreader)
    
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
    for x in range(1,len(profit)):
        profit_change.append(profit[x]-profit[x-1])
# Finding the Min and Max in Profit Change and Dates
# (Note: make sure to use + 1 when using the index to indicate the next month since we are looking for change
max_change = max(profit_change)
min_change = min(profit_change)

max_change_date = months[profit_change.index(max_change) + 1]
min_change_date = months[profit_change.index(min_change) + 1]

print("Financial Analysis")
print("---------------------------")
print(f"Total Months:{len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {str(max_change_date)} (${max(profit_change)})")
print(f"Greatest Decrease in Profits: {str(min_change_date)} (${min(profit_change)})")

pybank_analysis = os.path.join('Analysis', 'pybank.txt')
with open(pybank_analysis, "w") as text:
    text.write("Financial Analysis \n")
    text.write("--------------------------- \n")
    text.write(f"Total Months:{len(months)} \n")
    text.write(f"Total: ${sum(profit)} \n")
    text.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)} \n")
    text.write(f"Greatest Increase in Profits: {str(max_change_date)} (${str(max_change)}) \n")
    text.write(f"Greatest Decrease in Profits: {str(min_change_date)} (${str(min_change)})")
