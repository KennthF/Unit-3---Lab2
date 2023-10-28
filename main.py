# The source of CSV is https://www.datablist.com/learn/csv/download-sample-csv-files

import csv

with open("data_people.csv", "r") as csv_content:
    data = csv.reader(csv_content)

print("Use the 'Search' to find data of a person either by First or Last Name, Gender, and Job.")
user = input("\nSearch:")





