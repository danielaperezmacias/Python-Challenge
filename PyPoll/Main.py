import os
import csv

csv_path = "/Users/danielaperez-macias/Desktop/Projects/Python-Challenge/PyPoll/Resources/election_data.csv"
csv_output = os.path.join("Python-Challenge", "PyPoll", "election_data.txt")

total_votes = 0
candidates = []
votes_won = {}
winner_of_election = ""

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            votes_won[candidate] = 0

        votes_won[candidate] += 1

        if votes_won[candidate] > votes_won.get(winner_of_election, 0):
            winner_of_election = candidate

percentages = {}
for candidate, votes in votes_won.items():
    percentage = (votes / total_votes) * 100
    percentages[candidate] = percentage

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes_won[candidate]})")
print("-------------------------")
print(f"Winner: {winner_of_election}")
print("-------------------------")

output_path = "election_results.txt"
with open(output_path, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate in candidates:
        txt_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes_won[candidate]})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner_of_election}\n")
    txt_file.write("-------------------------\n")

