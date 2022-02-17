import json

print("Min Avg Score: ")
score = input()


with open('ranked.json', 'r') as f:
    player_data = json.load(f)

players = []

for player in player_data:
    if player["avg_score"] <= int(score):
        players.append(player["username"])

print(players)