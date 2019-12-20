import os
import csv

csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)

    candidate_list = {}
    voters = 0
    votes_cast = 0
    percent_of_votes = 0
    most_votes = 0
    most_voted = ""

    for row in csvreader:
        candidate = row[2]
        voters += 1
        if candidate in candidate_list.keys():
            candidate_list[candidate] += 1
        else:
            candidate_list[candidate] = 1
    
    print("Election Results")    
    print("----------------")
    print(f"Total Votes: {voters}")
    print("----------------")

    for candidate in candidate_list:
        votes_cast += candidate_list[candidate]

        percent_of_votes = (candidate_list[candidate])/(voters) * 100
        print(f"{candidate}: {int(percent_of_votes)}% {votes_cast}")
        
        if candidate_list[candidate] > most_votes:
            most_voted = candidate
            most_votes = candidate_list[candidate]
        


    print("----------------")
    print(f"Winner: {most_voted}")
    print("----------------")