from player import PlayerStats, PlayerReader
from rich.console import Console
from rich.prompt import Prompt

def main():
    console = Console()
    available_seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]

    console.print("NHL statistics by nationality", style="bold blue")

    while True:
        console.print(f"Available seasons: [{'/'.join(available_seasons)}]", style="bold green")
        season = Prompt.ask("Enter the season")
        if season not in available_seasons:
            console.print(f"Invalid season: {season}", style="bold red")
            continue

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        available_nationalities = stats.get_available_nationalities()

        while True:
            console.print(f"Available nationalities: [{'/'.join(available_nationalities)}]", style="bold green")
            nationality = Prompt.ask("Enter the nationality")
            if nationality not in available_nationalities:
                console.print(f"Invalid nationality: {nationality}", style="bold red")
                continue

            players = stats.top_scorers_by_nationality(nationality)

            for player in players:
                console.print(player)

            another_nationality = Prompt.ask("Do you want to check another nationality? (yes/no)")
            if another_nationality.lower() != "yes":
                break

        another_season = Prompt.ask("Do you want to check another season? (yes/no)")
        if another_season.lower() != "yes":
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console = Console()
        console.print("\nExiting program", style="bold red")
