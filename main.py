from data_loader import W1_saveData, W2_saveData, W3_saveData, W4_saveData
from player import LeagueMember
from scryfall_api import get_commander_color
import json
import os

# Load data for each week
week1_players = W1_saveData()
week2_players = W2_saveData()
week3_players = W3_saveData()
week4_players = W4_saveData()
print(week1_players)
# Create a set to keep track of player names
player_names = set()

# Create a dictionary to keep track of LeagueMember instances
league_members = {}

#  add players from weekly data
def add_players_from_week(week_players):
    for i in week_players:
        name = i[2]
        if name not in player_names:
            player_names.add(name)
            player = LeagueMember("default_name", 0, None, None, None, None, None, None, None, None, None, None, None)
            player.updateplayer(name)
            league_members[name] = player
        else:
            pass
flag = 0       
def update_commander_and_opponents(league_members, week_data, week_number):
    for i in league_members:
        for j in week_data:
            if i == j[2]:
                if week_number == 1:
                    week1_opponents = [j[6], j[9], j[12]]
                    league_members[i].update_commanderW1(j[4])
                    league_members[i].update_week1_opponents(week1_opponents)
                    favorite_color = get_commander_color(j[4])
                    print(favorite_color)
                    league_members[i].updatefavcolor(favorite_color)
                elif week_number == 2:
                    week2_opponents = [j[7], j[10], j[13]]
                    league_members[i].update_commanderW2(j[4])
                    league_members[i].update_week2_opponents(week2_opponents)
                elif week_number == 3:
                    week3_opponents = [j[8], j[11], j[14]]
                    league_members[i].update_commanderW3(j[4])
                    league_members[i].update_week3_opponents(week3_opponents)
                elif week_number == 4:
                    week4_opponents = [j[9], j[12], j[15]]
                    league_members[i].update_commanderW4(j[4])
                    league_members[i].update_week4_opponents(week4_opponents)


# Add players from all weeks
add_players_from_week(week1_players)
add_players_from_week(week2_players)
add_players_from_week(week3_players)
add_players_from_week(week4_players)
#Add the ocmmanders and opponents to the players
update_commander_and_opponents(league_members,week1_players,1)
update_commander_and_opponents(league_members,week2_players,2)
update_commander_and_opponents(league_members,week3_players,3)
update_commander_and_opponents(league_members,week4_players,4)


#turn the dictionary into a json
json_dict = {key: obj.to_dict() for key, obj in league_members.items()}

try:
    f = open("thisseason.json", "x")
    print("File created")
    with open('thisseason.json', 'w') as f:
        json.dump(json_dict, f, indent=4)
except:
    with open('thisseason.json', 'w') as f:
        json.dump(json_dict, f, indent=4)