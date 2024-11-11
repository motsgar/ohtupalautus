import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    fin_players = Player.filter_players_by_nationality(players, "FIN")

    print(f"Players from FIN: {len(fin_players)}")

    for player in fin_players:
        print(player)

if __name__ == "__main__":
    main()
