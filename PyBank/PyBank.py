# Import libraries
import pandas as pd

# Read file
df = pd.read_csv('budget_data.csv')

# Total months
total_months = len(df)
df['Change'] = df['Profit/Losses'].shift()

# Total profit
total = df['Profit/Losses'].sum()
df['Monthly_Change'] = df['Profit/Losses'] - df['Change']

# Average change
average_change = df['Monthly_Change'].mean()

# Set index
df.set_index('Date',inplace=True)

# Month of greatest increase
greatest_increase_month = df['Monthly_Change'].idxmax()

# Month of greatest decrease
greates_decrease_month = df['Monthly_Change'].idxmin()

# Profit greatest increase
greatest_increase = df.loc[df['Monthly_Change'].idxmax()]['Monthly_Change']

# Profit greatest decrease
greates_decrease = df.loc[df['Monthly_Change'].idxmin()]['Monthly_Change']

# Generate txt file
with open("budget_analysis.txt", "w") as text_file:

    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${total}\n")
    text_file.write(f"Average Change: ${round(average_change,2)}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greates_decrease_month} (${greates_decrease})")