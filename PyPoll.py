import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
print(
    f"\n==================\n"
    f"ELECTION RESULTS\n"
    f"==================\n\n"
    f"Total votes: {total_votes:,}\n\n"
    f"------------------\n"
    )        
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes)*100
    print(f"{candidate_name}: {votes:,} ({vote_percentage:.2f}%)")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"\n==================\n\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,} ({winning_percentage:.2f}%)\n\n"
    f"==================\n"
    )
print(winning_candidate_summary)