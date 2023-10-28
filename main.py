# The source of CSV is https://www.datablist.com/learn/csv/download-sample-csv-files

import csv

#Search the csv by gender
def gender_search(gender):
    result = []
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)
        for row in data:
            if gender == "female" and row["Sex"] == "female":
                result.append(row["Index"], row["First Name"], row["Last Name"])
            elif gender == "male" and row["Sex"] == "male":
                result = row["Index"], row["First Name"], row["Last Name"]
    return result


print("Use the 'Search' to find data of a person either by First or Last Name, Gender, and Job.")
user = input("\nSearch:").lower()

content = gender_search(user)

print(content)



