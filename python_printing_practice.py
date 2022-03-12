
#F STRING FOR ADDING VARIABLE INTO STRINGS
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes/total_votes * 100:,.2f}% of the total votes.")

#EXTRA LINE - NO F STRING
#my_votes = int(input("How many votes did you get in the election?"))
#total_votes = int(input("What is the total votes in the election?"))
#percentage_votes = (my_votes/total_votes)*100
#print("I received" +str(percentage_votes)+"% of the total votes.")
