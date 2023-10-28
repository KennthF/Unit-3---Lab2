# The source of CSV is https://www.datablist.com/learn/csv/download-sample-csv-files

import csv

#Search the csv by Sex
def gender_search(sex):
    result = []

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)

        for column in data:
            #Get all the name in the data by sex 
            if sex == "female" and column["Sex"] == "Female":
                result.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])

            elif sex == "male" and column["Sex"] == "Male":
                result.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])
    return result

def name_search(name):
    result = []
    search_input = input("Type a letter/s or name:") 

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)

        for column in data:
            #Gets all the name base on first or last name either by letter or word.
            if name == "first name":
                print("1")
                f_name = column["First Name"]
                for letter in f_name:
                    print("2")
                    i =+ 1
                    if search_input[i] == letter[i]:
                        print("3")
                        result.append(column["First Name"])
                
            #if name == "last name" and column["Last Name"] == "Last Name":


print("Use the 'Search' to find data of a person either by First or Last Name, Sex, and Job.")
user = input("\nSearch:").lower()

content = name_search(user)

for i in content:
    print(i)




