import csv

with open ("csv11.csv") as file:
    csv_reader = csv.reader(file)
    headings = next(csv_reader)

    for row in csv_reader:
        print(f"{row[2]} is the leader of {row[0]}")
