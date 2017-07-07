"""
A dictionary of player name abbreviations
"""
import players

# Abbreviate all player names to their strategy names
abbreviations = {str(player): player for player in players.players}

# Some manual overwrites:

abbreviations["Contrite Tit For Tat"] = "CTfT"
abbreviations["Forgiving Tit For Tat"] = "FTfT"
abbreviations["Tit For Tat"] = "TfT"
abbreviations["Hard Tit For 2 Tats"] = "HTf2T"
abbreviations["Hard Tit For Tat"] = "HTfT"
abbreviations["CollectiveStrategy"] = "CS"
abbreviations["Two Tits For Tat"] = "2TfT"
abbreviations["Tit For 2 Tats"] = "Tf2T"
abbreviations["Win-Stay Lose-Shift: C"] = "WSLS"
abbreviations["Win-Shift Lose-Stay: D"] = "WShLSt"
abbreviations["DBS: 0.75, 3, 4, 3, 5"] = "DBS"

for name, player in abbreviations.items():
    if "Evolved" in name or "PSO" in name:
        abbreviations[name] = "{}$^{{*}}$".format(player)
    elif "Gradual Killer" in name:
        abbreviations[name] = "Gradual Killer"
    elif "ZD" in name:
        abbreviations[name] = player.name
    else:
        abbreviations[name] = str(player)
