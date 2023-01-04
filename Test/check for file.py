import csv

reviews_data=[]

line_count = 0
    with open("csv1.csv") as file:
        csv_reader = csv.reader(file)
        for count in csv_reader:
            line_count = line_count + 1
        for r in range(0, line_count):
            reviews_data.append(r)
            percent = (r / line_count) * 100
            print(f"Loading data, {percent}%")

