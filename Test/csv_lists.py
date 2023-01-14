import csv

line_count = 0
line = []
import os

while not os.path.isfile("csv11.csv"):
    print("Whoops! No such file! Double check the file name")
    break
else:
    with open("csv11.csv") as file:
        csv_reader = csv.reader(file)
        if csv_reader:
            for count in csv_reader:
                line_count = line_count + 1
            for row in range(0, line_count):
                print("4")
                line.append(row)
                percent = row / line_count
                print(f"{percent}%")
        else:
            print("file couldn't be read")
    print(line)
