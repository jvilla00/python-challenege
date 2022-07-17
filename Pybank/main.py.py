#pybank code
from calendar import month
import os
import csv
csvbudge= os.path.join("..", "Resources", "budget_data.csv")
with open(csvbudge, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')  
  header= next(csvreader)
  #print (csvreader)

  #variables
  months = []
  profit = []
  monthly_changes = []
  profit_change=[]
  for row in csvreader:
    profit.append(int(row[1]))
    months.append(row[0])


profittotal=sum(profit)
print(len(months))
print(profittotal)


for i in range(len(profit)-1) :
    monthly_changes.append(profit[i+1] - profit[i])

monthly_average= sum(monthly_changes)/ len(monthly_changes)
#print(monthly_changes)
print(monthly_average)
max_increase= max(monthly_changes)
min_decrease = min(monthly_changes)

print(max_increase)
print(min_decrease)

print("financial analysis")
print(".........................")
print(f"Months: {len(months)}")
print(f"total" + "$",{sum(profit)})
print(f"Average change:" + "$" + str(monthly_average))
print(f"max increase", max_increase)
print(f"min decrease", min_decrease)

output_file="pybankbudget.txt"

with open(output_file, "w") as file:
    file.write("financial analysis\n")
    file.write(".........................\n")
    file.write(f"Months: {len(months)}\n")
    file.write(f"total: ${sum(profit)}\n")
    file.write(f"Average change: $" + (str(monthly_average)) + "\n")
    file.write(f"max increase"+ (str(max_increase)) +"\n") 
    file.write(f"min decrease"+ (str(min_decrease)) + "\n")
