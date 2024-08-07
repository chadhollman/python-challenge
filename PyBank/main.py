import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

numrows = 0
total = 0
changes = []
previous_value = None

# Initialize variables to track the greatest increase and decrease
greatest_increase = {'date': '', 'amount': float('-inf')}
greatest_decrease = {'date': '', 'amount': float('inf')}

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header
    csvheader = next(csvreader)
    
    for row in csvreader:
        # Increment the row count
        numrows += 1
        
        # Get the current month's profit/losses
        current_value = float(row[1])
        
        # Add the current value to the total
        total += current_value
        
        # Calculate the change from the previous month, if applicable
        if previous_value is not None:
            change = current_value - previous_value
            changes.append(change)
            
            # Check for greatest increase
            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = row[0]
            
            # Check for greatest decrease
            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = row[0]
        
        # Set the current value as the previous for the next iteration
        previous_value = current_value
    
    # Calculate the average change
    average_change = sum(changes) / len(changes) if changes else 0
    
    # Reformat the dates to display "MM-YYYY" or "MM-DD"
    greatest_increase_date = '-'.join(greatest_increase['date'].split('-')[1::-1])
    greatest_decrease_date = '-'.join(greatest_decrease['date'].split('-')[1::-1])
    
    # Prepare the output text
    output_text = (
        'Financial Analysis\n'
        '----------------------------\n'
        f'Total Months: {numrows}\n'
        f'Total: ${int(total)}\n'
        f'Average Change: ${round(average_change, 2)}\n'
        f'Greatest Increase in Profits: {greatest_increase_date} (${int(greatest_increase['amount'])})\n'
        f'Greatest Decrease in Profits: {greatest_decrease_date} (${int(greatest_decrease['amount'])})\n'
    )
    
    # Define the output file path in the parent directory
    output_file_path = os.path.join('Analysis', 'analysis.txt')
    
    # Write the output to the text file
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_text)

    # print the output to the console as well
    print(output_text)