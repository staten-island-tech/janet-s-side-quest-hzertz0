## This function opens the CSV for You!
red = "\033[31m"
reset = "\033[0m"
green = "\033[32m"

def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list

file_path = "SalesData.csv"  
data = csv_to_list(file_path)

def averagesales(data):
    sort_list = [] # assign 1
    avg = [] # assign 3
    days = len(data[0]) - 1

    for rows in data[1:]:
        avg_stores = round(sum(rows[1:]) / days, 2) # find average of each
        sort_list.append((rows[0], avg_stores)) # sort list

        avg.append(avg_stores) # assign 3

    sort_list.sort(key=lambda x: x[1], reverse=True) # sort 

    stores = len(avg) # find amount of numbers in list
    sumstores = sum(avg)
    assign3 = round(sumstores/stores, 2) # find average of all stores

    for name, avg_stores in sort_list: # sort by profit
        print(f"{reset}The average sales for {name} is ${avg_stores}")

        if avg_stores < 0.8 * assign3: # danger
            print(f"{red}Store in {name} is in risk of being closed!")
    
    # avg of all stores
    print(f"{green}All the stores's average earned is ${assign3}")
averagesales(data)




    







    

