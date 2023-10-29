#Create a File and write the name and score in golf
def saving_score(player_num):
    player_information = {}
    count = 1
    for i in range(player_num):
        player_name = input(f"{count}.Player Name:").strip()
        player_score = int(input(f"{player_name}'s Score:"))
        player_information.update({player_name: player_score})

        count += 1
    
    with open("golf.txt", "w") as golf_file:
        golf_content = golf_file.write(str(player_information))
    
    return golf_content

player_count = input("Number of Player:")

content = saving_score(int(player_count))

