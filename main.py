# The source of CSV is https://www.datablist.com/learn/csv/download-sample-csv-files

import csv

#Search the csv by Sex
def sex_search(search):
    personal_info = []
    other_info = []

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)

        for column in data:
            #Get all the name in the data by sex 
            if search == "Female" and column["Sex"] == "Female":
                personal_info.append(column["First Name"] + " " + column["Last Name"])
                other_info.append("Sex: " + column["Sex"] + "  Email: " + column["Email"] + 
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"])

            elif search == "Male" and column["Sex"] == "Male":
                personal_info.append(column["First Name"] + " " + column["Last Name"])
                other_info.append("Sex: " + column["Sex"] + "  Email: " + column["Email"] + 
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"])
    return personal_info, other_info

def name_job_search(search):
    personal_info = []
    other_info = []

    #Reads the csv file
    with open("data_people.csv", "r") as csv_content:
        data = csv.DictReader(csv_content)
        content_data = ""

        for column in data:
            content_data = column["First Name"].lower() #Default Option for Search
            
            #See if the user wants to change the option for search
            if search == "First Name":
                content_data = column["First Name"].lower()
                search = input("Type a letter/s or word/s for the First Name:").lower() 

            elif search == "Last Name":
                content_data = column["Last Name"].lower()
                search = input("Type a letter/s or word/s for the Last Name:").lower()

            elif search == "Job Title":
                content_data = column["Job Title"].lower()
                search = input("Type a letter/s or word/s for the Job Title:").lower() 

            #Find out whos smaller in size between the 2 words
            len_search = min(len(content_data),len(search)) 
            #Gets the name base on the search
            counter = 0
            for i in range(int(len_search)):
                if content_data[i] == search[i]:
                    print(counter)
                    counter = counter + 1 #Adds one if each letter is the same

                    #If everything is the same then it will append to the list
                    if counter == int(len_search): 
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


search_input = ""
while search_input != "Stop":
    #Get the user input
    print("\n" + f"-"*150)
    print("Use the 'Search' to find a person in the database by either name or sex.")
    print("Options: by First Name, Last Name, Job Title, All")
    print(f"-"*150)
    search_input = input("\nSearch:").title()

    #Function call
    content_data = ""
    other_data = ""
    
    if search_input == 'Male' or search_input == 'Female':
        content_data, other_data = sex_search(search_input)

    elif search_input == 'All':
        content_data, other_data = call_all()

    else:
        content_data, other_data = name_job_search(search_input)
    
    
    if content_data == [] or content_data == "": #To see if it returns empty
        print("\n\tNot Found.")
    
    #Ask the user if they want to get more information depends on the name of the input
    else:    
        ask_detail_input = ""
        exit_continue_input = ""
        while exit_continue_input != "Exit":
            for info in content_data: #Just print a list of names to choose
                print(f"\n  -->\t{info}")

            print("\nType the full name for other information")
            ask_detail_input = input("Choose Name:").title()

            count = 0
            for info in content_data: #Will print the other info and the name
                if ask_detail_input == info:
                    print(f"\nName: {content_data[count]} --- {other_data[count]}")
                count = count + 1

            exit_continue_input = input("\nPress Enter to find more details or 'Exit' to go back to search:").capitalize()
