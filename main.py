import os;
import csv;

def analyze_budget_data(file_path) :

    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    total_change = 0
    greatest_increase = {"date": None, "amount": float("-inf")}
    greatest_decrease = {"date": None, "amount": float("inf")}

    # Open and read the CSV file
    with open("budget_data.csv", 'r') as file:
        # Skip the header row
        next(file)

        # Loop through each line in the file
        for line in file:
            # Split the line into date and profit/loss
            date, profit_loss = line.strip().split(',')

            # Convert profit/loss to an integer
            profit_loss = int(profit_loss)

            # Increment the total number of months
            total_months = total_months + 1

            # Add profit/loss to the net total
            net_total = net_total + profit_loss

            # Calculate the change in profit/loss
            change = profit_loss - previous_profit_loss

            # Add the change to the total change
            total_change -= change

            # Update the greatest increase if applicable
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            # Update the greatest decrease if applicable
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

            # Update the previous profit/loss for the next iteration
            previous_profit_loss = profit_loss

    # Calculate the average change
    average_change = total_change / (total_months - 1)

    # Return the analysis results
    return {
        "Total Months": total_months,
        "Net Total": net_total,
        "Average Change": average_change,
        "Greatest Increase": {"date": greatest_increase['date'], "amount": greatest_increase['amount']},
        "Greatest Decrease": {"date": greatest_decrease['date'], "amount": greatest_decrease['amount']}
    }


# Example usage
file_path = 'budget_data.csv'
analysis_results = analyze_budget_data('budget_data.csv')

# Print the analysis results
print("Financial Analysis")

print("-----------------------------")
print(f"Total Months: {analysis_results['Total Months']}")
print(f"Net Total: ${analysis_results['Net Total']}")
print(f"Average Change: ${analysis_results['Average Change']:.2f}")
print(f"Greatest Increase in Profits: {analysis_results['Greatest Increase']['date']} "
      f"(${analysis_results['Greatest Increase']['amount']:.2f})")
print(f"Greatest Decrease in Profits: {analysis_results['Greatest Decrease']['date']} "
      f"(${analysis_results['Greatest Decrease']['amount']:.2f})")
