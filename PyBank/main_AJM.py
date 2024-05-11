# import os module 
import os

# import csv file module
import csv

# csv path 
csvpath = "PyBank/Resources/budget_data.csv"

# list the variables
month_count = 0
total_profit = 0

# list the for changes
last_month_profit = 0
changes = []
month_changes = []

# reading method: improved reading using csv module 
with open(csvpath) as csvfile:
     
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # read header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row of data after the header 
    for row in csvreader:
            print(row)

            # get month count
            month_count += 1
            print(month_count)

            # get total profit 
            total_profit = total_profit + int(row[1])
            print(total_profit)

            # calc changes info (precursor)
            if (month_count == 1):
                last_month_profit = int(row[1])
            else:
                 change = int(row[1]) - last_month_profit
                 changes.append(change)
                 month_changes.append(row[0])

                 # reset last month profit
                 last_month_profit = int(row[1])
    print(len(changes))

    #get average change
    avg_change = sum(changes) / len(changes)
    print(avg_change)

    #get/print changes
    max_change = max(changes)
    max_month_indx = changes.index(max_change)
    max_month = month_changes[max_month_indx]
    min_change = min(changes)
    min_month_indx = changes.index(min_change)
    min_month = month_changes[min_month_indx]
    print(max_change)
    print(max_month)
    print(min_change)
    print(min_month)

    # FINAL OUTPUT 
    output = f"""Financial Analysis
----------------------------------
Total Months: {month_count}
Total: ${total_profit}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""
    
    # print to terminal
    print(output)

    # write/save txt file to "analysis" folder
    output_folder = "PyBank/analysis"
    output_file = os.path.join(output_folder, "output_ajm.txt")
    with(open(output_file,'w')as f):
         f.write(output)



'''COMMENTS:
I referenced in-class activity material to help develop my complete script and referenced
the Xpert learning assitant to help write the specific portion of script that saves the summary output
to a specific folder.'''