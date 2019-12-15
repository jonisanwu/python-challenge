import os
import csv

csvpath = os.path.join('budget_data.csv')

count_of_months = 0
profit_loss_total = float(0)
profit_loss_column = 1
average_change = float(0)


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    print(f"Header: {csv_header}")
    
    for row in csvreader:
        count_of_months += 1
# - += changes the variable itself. https://stackoverflow.com/questions/4841436/what-exactly-does-do-in-python - JW.        
        profit_loss = float(row[profit_loss_column])
        profit_loss_total += profit_loss
        # for row in csvreader:
        #     average_change = float(row[profit_loss_column]) - float(prior_row[profit_loss_column])
        #     average_change += average_change
        # average_change_total = average_change / count_of_months
        # print(average_change_total)
        
#   * The total number of months included in the dataset
    print(f"The Number of Months Calculated: {count_of_months} ")
#   * The net total amount of "Profit/Losses" over the entire period
    print(f"The Total is: {profit_loss_total}")
#   * The average of the changes in "Profit/Losses" over the entire period
    
#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period