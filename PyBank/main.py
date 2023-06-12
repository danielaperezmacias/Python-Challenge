import csv 
import os

csv_path = "/Users/danielaperez-macias/Desktop/Projects/Python-Challenge/PyBank/Resources/budget_data.csv"
csv_output = os.path.join("Python-Challenge", "PyBank", "budget_data.txt")

total_months = 0
net_profit = 0
net_profit_losses = 0
profit_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_months += 1

        net_profit += int(row[1])

        if total_months > 1: 
            profit_change.append(int(row[1]) - net_profit_losses)

        if int(row[1]) - net_profit_losses > greatest_increase[1]:
            greatest_increase = [row[0], int(row[1]) - net_profit_losses]
        elif int(row[1]) - net_profit_losses < greatest_decrease[1]:
            greatest_decrease = [row[0], int(row[1]) - net_profit_losses]

        net_profit_losses = int(row[1])

change = sum(profit_change) / len(profit_change)


print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_profit}\n")
print(f"Average Change: ${change:.2f}\n")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")



output_path = "budget_data.txt"
with open(output_path,'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_profit}\n")
    txt_file.write(f"Average Change: ${change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")



