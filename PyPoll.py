#Tasks to accomplish
#1. Total Number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidates received
#4. percentage of votes each candidate won
#5. Winner of election based on popular vote
#import modules for use
import os
import csv
#assign variable for the file to load the path
file_to_load = os.path.join("resources", "election_results.csv")
#open election results and read the file
with open (file_to_load, "r") as election_data:
    #print file object
    print(election_data)
#create filename variable to a direct/indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#using open() function with the "W" mode - this is how to write to a file
#using with statement to open file as text file
with open (file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
#open election results and read
with open (file_to_load) as election_data:
    #to do Read and analyze data 
    file_reader = csv.reader(election_data)
#print header row
    headers = next(file_reader)
    print(headers)
    #print each row in CSV file 
    for row in file_reader:
        print(row)