from matchup import mixup
from thue_morse import createSequence

def create_teams(selected_contacts, player_data):
    present_players = {}
    for i in selected_contacts:
        present_players[i] = player_data.get(i)
    return setup_teams(present_players)



def takeSecond(elem):
    return elem[1]


def setup_teams(available_dict):
    playyerseq = mixup(available_dict)
    teamseq = createSequence(6)
    team_g = []
    team_d = []
    for i in range(len(teamseq)):
        if 0 <= i < len(playyerseq):
            if teamseq[i] == '1':
                team_g.append(playyerseq[i])
            else:
                team_d.append(playyerseq[i])

    teams = "\nTeam G:  " + str(team_g)[1:-1] + "\n\nTeam D:  " + str(team_d)[1:-1]
    return teams.replace("'","").replace(",","  ").split('\n')