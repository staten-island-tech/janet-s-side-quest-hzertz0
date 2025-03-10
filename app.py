## This function opens the CSV for You!
days = 30
stores = 12

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
    sort_list = []

    for rows in data[1:]:
        avg = round(sum(rows[1:]) / days, 2) # find average
        sort_list.append((rows[0], avg)) # append average of all stores to sort_list

    sort_list.sort(key=lambda x: x[1], reverse=True) # sort 

    for name, avg in sort_list:
        print(f"The average sales for {name} is ${avg}")
averagesales(data)

""" def averageall(data):
    for rows in data[1:]:
        avg = round(sum(rows[1:]) / days, 2)
        sum(avg)/ stores """
    







    

