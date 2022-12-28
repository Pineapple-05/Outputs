import csv

line = []
with open("csv1.csv") as file:
    csv_reader = csv.reader(file)
    for count in csv_reader:
        pass
    for row in csv_reader:
        print("4")
        line.append(row)
        percent = row / count
        print(f"{percent}%")
print(line)
