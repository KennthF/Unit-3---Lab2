# The source of CSV is https://www.datablist.com/learn/csv/download-sample-csv-files

import csv

#Search the csv by Sex
def sex_search():
    personal_info = []
    other_info = []
    search_input = input("Sex:").title() 

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)

        for column in data:
            #Get all the name in the data by sex 
            if search_input == "Female" and column["Sex"] == "Female":
                personal_info.append(column["First Name"] + " " + column["Last Name"])
                other_info.append("Sex: " + column["Sex"] + "  Email: " + column["Email"] + 
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"])

            elif search_input == "Male" and column["Sex"] == "Male":
                personal_info.append(column["First Name"] + " " + column["Last Name"])
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
                        personal_info.append(column["First Name"] + " " + column["Last Name"])
                        other_info.append("Sex: " + column["Sex"] + "  Email: " + column["Email"] + 
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"])
                        counter = 0
    return personal_info, other_info


def call_all():
    personal_info = []
    other_info = []

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)

        #Will add every content here
        for column in data:
            personal_info.append(column["First Name"] + " " + column["Last Name"])
            other_info.append("Sex: " + column["Sex"] + "  Email: " + column["Email"] + 
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"])
    return personal_info, other_info


first_input = ""
while first_input != "Stop":
    #Get the user input
    print("\n" + f"-"*150)
    print(f"Use the 'Search' to find data of a person either by typing 'First Name' or 'Last Name','Sex','Job Title' and 'All' to display everything or 'Stop' to end this prompt.")
    print(f"-"*150)
    first_input = input("\nSearch:").title()

    #Function call
    content_data = ""
    other_data = ""
    if first_input == 'First Name' or first_input == 'Last Name' or first_input == 'Job Title':
        content_data, other_data = name_job_search(first_input)
    
    elif first_input == 'Sex':
        content_data, other_data = sex_search()

    elif first_input == 'All':
        content_data, other_data = call_all()

    else:
        if first_input != "Stop": #To stop printing invalid when quiting
            print("\n\tInvalid Input")

    #Ask the user if they want to get more information depends on the name of the input
    second_input = ""
    while second_input != "Exit" and content_data != [] and content_data != "":
        for info in content_data: #Just print a list of names to choose
            print(f"\n  -->\t{info}")

        print("\nType the full name for other information or 'Exit' to go back to search")
        second_input = input("Choose Name:").title()

        count = 0
        for info in content_data: #Will print the other info and the name
            if second_input == info:
                print(f"\nName: {content_data[count]} --- {other_data[count]}")
            count = count + 1

        second_input = input("\nPress Enter to continue:")
