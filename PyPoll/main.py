import csv

# Files to load (Remember to change these)
file_to_load = "PyPoll/Resources/election_data.csv"


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # use of next to skip first title row in csv file
    next(reader) 
    number_of_votes = []
    candidate1 = []
    candidate2 = []
    candidate3 = []
    candidate4 = []


    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in reader:
        number_of_votes.append(row[0])
        if row[2] == "Khan":
            candidate1.append(row[2])
        if row[2] == "Correy":
            candidate2.append(row[2])
        if row[2] == "Li":
            candidate3.append(row[2])
        if row[2] == "O'Tooley":
            candidate4.append(row[2])
                  

    print("Election Results")
    print("-------------------------")

    print("Total Votes: ", len(number_of_votes))
    print("-------------------------")
    print("Total for Khan: ", len(candidate1), ", ", 100*(len(candidate1)/len(number_of_votes)), "%")
    print("Total for Correy: ", len(candidate2), ", ", 100*(len(candidate2)/len(number_of_votes)), "%")
    print("Total for Li: ", len(candidate3), ", ", 100*(len(candidate3)/len(number_of_votes)), "%")
    print("Total for O'Tooley: ", len(candidate4), ", ", 100*(len(candidate4)/len(number_of_votes)), "%")
    print("-------------------------")

