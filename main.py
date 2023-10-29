# The source of CSV is https://www.datablist.com/learn/csv/download-sample-csv-files

import csv

#Search the csv by Sex
def sex_search(sex):
    personal_info = []
    other_info = []

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)

        for column in data:
            #Get all the name in the data by sex 
            if sex == "Female" and column["Sex"] == "Female":
                personal_info.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])
                other_info.append("Sex: " + column["Sex"] + "  Email: " + column["Email"] + 
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"])

            elif sex == "Male" and column["Sex"] == "Male":
                personal_info.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])
                other_info.append("Sex: " + column["Sex"] + "  Email: " + column["Email"] + 
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"])
    return personal_info, other_info

def name_job_search(name_job):
    personal_info = []
    other_info = []

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)
        content_data = ""
        search_input = ""

        for column in data:
            
            #See if the chosen option to search is first or last name or a job
            
            if name_job == "First Name":
                content_data = column["First Name"].lower()
                if search_input == "": #To make it happen one time in loop
                    search_input = input("Type a letter/s or word/s for the First Name:").lower() 

            elif name_job == "Last Name":
                content_data = column["Last Name"].lower()
                if search_input == "": #To make it happen one time in loop
                    search_input = input("Type a letter/s or word/s for the Last Name:").lower()

            elif name_job == "Job Title":
                content_data = column["Job Title"].lower()
                if search_input == "": #To make it happen one time in loop
                    search_input = input("Type a letter/s or word/s for the Job Title:").lower() 

            #Find out whos smaller in size between the 2 words
            len_name = min(len(content_data),len(search_input)) 

            #Gets the name base on the search
            counter = 0
            for i in range(int(len_name)):
                if content_data[i] == search_input[i]:
                    counter = counter + 1 #Adds one if each letter is the same

                    #If everything is the same then it will append to the list
                    if counter == int(len_name): 
                        personal_info.append(column["Index"] + " " + column["First Name"] + " " + column["Last Name"])
                        other_info.append("Sex: " + column["Sex"] + "  Email: " + column["Email"] + 
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"])
                        counter = 0
    return personal_info, other_info



print("Use the 'Search' to find data of a person either by typing First or Last Name, Sex, and Job Title.")
user = input("\nSearch:").title()

content, other_content = name_job_search(user)

for i in other_content:
    print(i)





