#Tasks to accomplish
#1. Total Number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidates received
#4. percentage of votes each candidate won
#5. Winner of election based on popular vote
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)