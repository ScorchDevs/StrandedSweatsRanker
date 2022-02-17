import json

with open('ranked.json', 'r') as f:
    player_data = json.load(f)

pretty = ""
    
new_values = sorted(player_data, key=lambda k: k["avg_score"], reverse=True)

for i in range(len(new_values)):
    pretty += f"{i+1}. {new_values[i]['prefix']}{new_values[i]['username']} (avg score: {int(new_values[i]['avg_score'])}, avg rank: {int(new_values[i]['avg_rank'])}){new_values[i]['suffix']}\n"

with open('pretty.txt', 'w') as f:
    f.write(pretty)