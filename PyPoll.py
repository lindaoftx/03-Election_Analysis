import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_analysis.txt")

total_votes = 0
total_cvotes = 0

candidate_options = []
candidate_votes = {}

county_options = []
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

turnout_highest = ""
turnout_count = 0
turnout_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        total_cvotes += 1
        candidate_name = row[2]
        county_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\n=========================================\n\n"
        f"* * * * *   ELECTION  RESULTS   * * * * *\n\n"
        f"=========================================\n\n"
        f"Total votes: {total_votes:,}\n\n"
        f"-----------------------------------------\n"
        f"Votes by County:\n"
        f"-----------------------------------------\n\n"
        )
    print(election_results, end="")
    txt_file.write(election_results)
    for county_name in county_votes:
        cvotes = county_votes[county_name]
        county_percentage = float(cvotes)/float(total_cvotes)*100
        county_results = (f"{county_name}: {cvotes:,} ({county_percentage:.2f}%)\n")
        print(county_results)
        txt_file.write(county_results)
        if (cvotes > turnout_count) and (county_percentage > turnout_percentage):
            turnout_count = cvotes
            turnout_percentage = county_percentage
            turnout_highest = county_name
    highest_turnout_summary = (
        f"\n=========================================\n\n"
        f"Highest voter turnout: {turnout_highest} County\n"
        f"\n=========================================\n\n"
        f"-----------------------------------------\n"
        f" Votes by Candidate:\n"
        f"-----------------------------------------\n\n"
        )
    print(highest_turnout_summary)
    txt_file.write(highest_turnout_summary)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        candidate_results = (f"{candidate_name}: {votes:,} ({vote_percentage:.2f}%)\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"\n=========================================\n\n"
        f" Election Winner: {winning_candidate}\n\n"
        f" Winning Vote Count: {winning_count:,} ({winning_percentage:.2f}%)\n\n"
        f"=========================================\n\n"
        f"* * * * * * * * * * * * * * * * * * * * *\n"
        )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)