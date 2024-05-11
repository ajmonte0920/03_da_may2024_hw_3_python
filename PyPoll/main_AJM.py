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

# FINAL OUTPUT
# Output: header and "Total votes"
output = f"""Election Results
-----------------------------
Total Votes: {vote_count}
-----------------------------\n"""

# Output: list of candidates that received votes, percentages, & count
max_cand = ""
max_votes = 0

for candidate in candidate_dict.keys():
    # get candidate vote info
    votes = candidate_dict[candidate]
    perc = 100 * (votes / vote_count)
    # Candidate output
    line = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    output += line

    # get "Winner" info
    if votes > max_votes:
        max_cand = candidate
        max_votes = votes

# Output: "Winner"
last_line = f"""-------------------------
Winner: {max_cand}
-------------------------"""
output += last_line
print(output)

# write/save txt file to "analysis" folder
output_folder = "PyPoll/analysis"
output_file = os.path.join(output_folder, "output_ajm.txt")
with(open(output_file,'w')as f):
         f.write(output)