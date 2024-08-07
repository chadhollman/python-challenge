import os
import csv

# Path to the CSV file
election_csv = os.path.join('Resources', 'election_data.csv')

# Initialize variables
numrows = 0
candidates = {}

# Read the CSV file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header
    csvheader = next(csvreader)
    
    # Process each row
    for row in csvreader:
        numrows += 1
        candidate = row[2]
        
        # Count occurrences of each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Initialize variables to track the candidate with the highest percentage
max_percentage = 0
winner = ""


# Calculate percentages and find the winner
for candidate, count in candidates.items():
    percentage = (count / numrows) * 100
    print(f'{candidate}: {percentage:.3f}% ({count} votes)')
    
    # Check if this candidate has the highest percentage
    if percentage > max_percentage:
        max_percentage = percentage
        winner = candidate

# Prepare the output text
output_text = (
        'Election Results\n'
        '----------------------------\n'
        f'Total Votes: {numrows}\n'
        '----------------------------\n'
        f'{candidate}: {percentage:.3f}% ({count} votes)\n'
        '----------------------------\n'
        f'Winner: {winner}\n'
        '----------------------------\n'
)

# Define the output file path in the parent directory
output_file_path = os.path.join('Analysis', 'analysis.txt')
    
    # Write the output to the text file
with open(output_file_path, 'w') as output_file:
    output_file.write(output_text)

    # print the output to the console as well
    print(output_text)