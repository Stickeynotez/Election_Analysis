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
#Initialize a total vote counter
total_votes = 0
#candidate options and candidate votes (list/Dictionary)
candidate_options =  []
candidate_votes = {}
winner = ""
winning_count = 0
winning_percentage = 0
#open election results and read the file
with open (file_to_load, "r") as election_data:
    #print file object
    print(election_data)
#create filename variable to a direct/indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#using open() function with the "W" mode - this is how to write to a file
#using with statement to open file as text file
#with open (file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
#open election results and read
with open (file_to_load) as election_data:
    #to do Read and analyze data 
    file_reader = csv.reader(election_data)
#print header row
    headers = next(file_reader)
    #print each row in CSV file 
    for row in file_reader:
        #2. add the total vote count
        total_votes += 1
        #print candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
        #add candidate to list
            candidate_options.append(candidate_name)
            #begin tracking vote counts
            candidate_votes[candidate_name] = 0
            #add vote to candidate
        candidate_votes[candidate_name] +=1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
#print candidate list
#print(candidate_options)
#3. print total votes
#print(total_votes)
#print candidate votes
#print(candidate_votes)
# create for loop for calculating vote% for each candidate.
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes) / float(total_votes)) * 100
        #add :.2f (makes float to 2 decimal places rather than continuous)
        print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
        #conditional statement to determine winner by popular vote
        candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #print candidate results
        print (candidate_results)
            #save results to text file
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winner = candidate_name
            #print out each name, vote count, and percentage of votes to terminal
    #print winning candidate
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winner}\n"
        f"winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print (winning_candidate_summary)
    #print winner to file
    txt_file.write(winning_candidate_summary)

