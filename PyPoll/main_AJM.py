 # import os module 
import os

# import csv file module
import csv

# csv path 
csvpath = "PyPoll/Resources/election_data.csv"

# list the variables
vote_count = 0
candidate_dict = {}

# reading method: improved reading using csv module 
with open(csvpath) as csvfile:
     
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # read header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row of data after the header
    for row in csvreader:
        # total vote cast
        vote_count +=1

         # list of candidates that received votes
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1
print(vote_count)
print(candidate_dict)
