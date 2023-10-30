#Check an input if it is either a number o letter
def validation(text):
    if text.isnumeric():
        return "number"
    
    elif text.isalpha():
        return "letter"


#Create a File and write the name and score in golf
def saving_score(player_num):
    player_information = {}
    player_count = 1
    counter = 0
    check_letter = ""
    check_number = ""

    #Loop the user till the player info is fill up
    while counter != player_num:
        player_name = input(f"\n{player_count}.Player Name:").strip()
        check_letter = validation(player_name)

        if check_letter != "letter":
            print("\n\tInvalid Player Name\n")
            check_letter = ""

        elif check_letter == "letter":
            player_score = input(f"{player_name}'s Score:")
            check_number = validation(player_score)

            if check_number == "number":
                player_information.update({player_name: player_score})
                player_count += 1
                counter += 1

            else:
                print("\n\tInvalid Score")
                check_number = ""

    
    with open("golf.txt", "w") as golf_write:
        golf_write.write(str(player_information))

    with open("golf.txt", "r") as golf_read:
        content_golf = golf_read.read()
        
    return content_golf


check = ""

while check != "number":
    player_count = input("Number of Player:")
    check = validation(player_count)

    if check != "number":
        print("\n\tInvalid Number\n")

content = saving_score(int(player_count))

print(content)

