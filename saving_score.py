#Create a File and write the name and score in golf
def saving_score(player_num):
    player_information = {}
    count = 1
    for i in range(player_num):
        player_name = input(f"{count}.Player Name:").strip()
        player_score = int(input(f"{player_name}'s Score:"))
        player_information.update({player_name: player_score})

        count += 1
    
    with open("golf.txt", "w") as golf_write:
        golf_write.write(str(player_information))

    with open("golf.txt", "r") as golf_read:
        content_golf = golf_read.read()
        
    return content_golf

player_count = input("Number of Player:")

content = saving_score(int(player_count))

print(content)

