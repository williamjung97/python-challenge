# Creating file paths across OS
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Setting up variables
votercount = 0
khanvotes = 0 
correyvotes = 0 
livotes = 0
otooleyvotes = 0

#Open the CSV file and make sure to read header row first
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

#Set up for loops to read each row of data 
    for row in csvreader:
        votercount += 1 

        #Using If Else statements to calculate total votes for the candidates
        if row[2] == "Khan":
            khanvotes += 1
        elif row[2] == "Correy":
            correyvotes += 1 
        elif row[2] == "Li":
            livotes += 1 
        else:
            otooleyvotes += 1

    # Set up equations to find percentages
    percentagekhan = (khanvotes / votercount)
    percentagecorrey = (correyvotes / votercount)
    percentageli = (livotes / votercount)
    percentageotooley = (otooleyvotes / votercount)

    #Use max function to determine which candidate had the most amount of votes
    winner = max(khanvotes, correyvotes, livotes, otooleyvotes)

    #Set up more If Else statements to determine winner
    if winner == khanvotes:
        winningcandidate = "Khan"
    elif winner == correyvotes:
        winningcandidate = "Correy"
    elif winner == livotes:
        winningcandidate = "Li"
    else:
        winningcandidate = "O'Tooley"

#Writing print statements (note: the ':.3%' is to get three decimal places in percent)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votercount}")
print("-------------------------")
print(f"Khan: {percentagekhan:.3%} ({khanvotes})")
print(f"Correy: {percentagecorrey:.3%} ({correyvotes})")
print(f"Li: {percentageli:.3%} ({livotes})")
print(f"O'Tooley: {percentageotooley:.3%} ({otooleyvotes})")
print("-------------------------")
print(f"Winner: {winningcandidate}")
print("-------------------------")

#Last convert print statement into a text file
election_results = os.path.join('Analysis', 'pypoll.txt')
with open(election_results, 'w') as text:
    text.write("Election Results \n")
    text.write("------------------------- \n")
    text.write(f"Total Votes: {votercount} \n")
    text.write("------------------------- \n")
    text.write(f"Khan: {percentagekhan:.3%} ({khanvotes}) \n")
    text.write(f"Correy: {percentagecorrey:.3%} ({correyvotes}) \n")
    text.write(f"Li: {percentageli:.3%} ({livotes}) \n")
    text.write(f"O'Tooley: {percentageotooley:.3%} ({otooleyvotes}) \n")
    text.write("------------------------- \n")
    text.write(f"Winner: {winningcandidate} \n")
    text.write("-------------------------")
    
    