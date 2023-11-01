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
        counter = 0
        holder = 0
        
        for column in data:
            #See if the user wants to change the option for search
            if search == "Last Name" or holder == 1:
                if holder == 0: #To avoid looping input
                    search = input("Type a letter/s or word/s for the Last Name:").title()
                content_data = column["Last Name"].title()
                holder = 1

            elif search == "Job Title" or holder == 2:
                if holder == 0: #To avoid looping input
                    search = input("Type a letter/s or word/s for the Job Title:").title() 
                    
                content_data = column["Job Title"].title()
                holder = 2
            
            else:
                if holder == 0:
                    content_data = column["First Name"].title()

            #Find out whos smaller in size between the 2 words
            len_search = min(len(content_data),len(search)) 
            
            #Gets the name base on the search
            for i in range(int(len_search)):
                if content_data[i] == search[i]:
                    counter =+ 1 #Adds one if each letter is the same

                    #If everything is the same then it will append to the list
                    if counter == int(len_search): 
                        if holder == 2:
                            personal_info.append(column["First Name"] + " " + column["Last Name"] + "  Job Title: " 
                                                 + column["Job Title"].title())
                        
                        else:
                            personal_info.append(column["First Name"] + " " + column["Last Name"])

                        other_info.append("Sex: " + column["Sex"] + "  Email: " + column["Email"] + 
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"].title())
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
                            "  Birthday: " + column["Date of birth"] + "  Job Title: " + column["Job Title"].title)
    return personal_info, other_info


search_input = ""
while search_input != "Stop":
    #Get the user input
    print("\n" + f"-"*75)
    print("Use the 'Search' to find a person in the database by either name or sex.")
    print("Options by: First Name, Last Name, Job Title, All")
    print(f"-"*75)
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
            for names in content_data: #Just print a list of names to choose
                print(f"\n  -->\t{names}")

            print("\nType the full name for other information")
            ask_detail_input = input("Choose Name:").title()

            count = 0
            for names in content_data: #Will print the other info and the name
                if ask_detail_input == names:
                    print(f"\nName: {content_data[count]} --- {other_data[count]}")
                    count = 0
                    break
                count = count + 1
            
            if count != 0: #If the count did not became 0 it means the input is not match
                print("\n\tNot Found.")

            exit_continue_input = input("\nPress Enter to find more details or 'Exit' to go back to search:").capitalize()

            

