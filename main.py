# The source of CSV is https://www.datablist.com/learn/csv/download-sample-csv-files

import csv

#Search the csv by Sex
def sex_search(sex):
    result = []

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)

        for column in data:
            #Get all the name in the data by sex 
            if sex == "Female" and column["Sex"] == "Female":
                result.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])

            elif sex == "Male" and column["Sex"] == "Male":
                result.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])
    return result

def name_search(name):
    result = []
    search_input = input("Type a letter/s or name:").lower() 

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)
        option_name = ""

        for column in data:
            #See if the chosen option to search is first or last name
            if name == "First Name":
                option_name = column["First Name"].lower()
            elif name == "Last Name":
                option_name = column["Last Name"].lower()

            #Find out whos smaller in size between the 2 words
            len_name = min(len(option_name),len(search_input)) 

            #Gets the name base on the search
            counter = 0
            for i in range(int(len_name)):
                if option_name[i] == search_input[i]:
                    counter = counter + 1 #Adds one if each letter is the same

                    #If everything is the same then it will append to the list
                    if counter == int(len_name): 
                        result.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])
                        counter = 0
            return result

print("Use the 'Search' to find data of a person either by First or Last Name, Sex, and Job.")
user = input("\nSearch:").title()

content = name_search(user)

for i in content:
    print(i)




