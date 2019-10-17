import csv
import random

def create_player_group(file):
    reader = csv.reader(open(file, 'r'))
    player_group = {}
    for row in reader:
        player_group[row[0]] = row[1]
    return player_group
    
def mixup(players):
    all_levels = []
    lev1 = []
    lev2 = []
    lev3 = []
    lev4 = []
    lev5 = []
    for key in players:
        if(players.get(key)=='1'):
            lev1.append(key)
        if(players.get(key)=='2'):
            lev2.append(key)
        if(players.get(key)=='3'):
            lev3.append(key)
        if(players.get(key)=='4'):
            lev4.append(key)
        if(players.get(key)=='5'):
            lev5.append(key)
    all_levels.append(lev1)
    all_levels.append(lev2)
    all_levels.append(lev3)
    all_levels.append(lev4)
    all_levels.append(lev5)
    for x in all_levels:
        random.shuffle(x)
    final_list= sum(all_levels,[])
    return final_list
