# The source of CSV is https://www.datablist.com/learn/csv/download-sample-csv-files

import csv

#Search the csv by Sex
def gender_search(sex):
    result = []
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)
        for column in data:
            if sex == "female" and column["Sex"] == "Female":
                result.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])
            elif sex == "male" and column["Sex"] == "Male":
                result.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])
    return result


print("Use the 'Search' to find data of a person either by First or Last Name, Sex, and Job.")
user = input("\nSearch:").lower()

content = gender_search(user)

for i in content:
    print(i)




