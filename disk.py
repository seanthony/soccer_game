def get_goalie():
    with open('goalie.txt', 'r') as file:
        goalie = file.read()
    return goalie
