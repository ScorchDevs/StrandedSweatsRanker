import json
from operator import itemgetter
import collections

MIN_MAX_MAP = 1000

def getMaxOfKey(player_data: list, key: str):
    max = 0
    for player in player_data:
        if type(player[key]) is str: break
        if player[key] > max:
            max = player[key]
    return max

def getRankedValues(player_data: dict, key: str):
    rtn = {}
    data = sorted(player_data, key=lambda k: k[key], reverse=True)
    index = 1
    for player in data:
        rtn[player["uuid"]] = index
        index += 1
    return rtn


with open('data.json', 'r') as f:
    player_data = json.load(f)
    
keys = list(player_data[0].keys())

new_values = []
calced = {}

for key in keys:
    calced[key] = {}
    calced[key]["ranked"] = getRankedValues(player_data, key)
    calced[key]["biggest_value"] = getMaxOfKey(player_data, key)
    calced[key]["map_val"] = calced[key]["biggest_value"] / MIN_MAX_MAP
    if calced[key]["map_val"] == 0:
        calced[key]["map_val"] = 1

for player in player_data: 
    vals = {}
    ranks_added = 0
    ranks_amount = 0
    score_added = 0
    score_amount = 0
    for key in keys:
        vals[key] = player[key]
        if type(player[key]) is str: continue
        vals[key + "_score"] = player[key] / calced[key]["map_val"]
        vals[key + "_ranked"] = calced[key]["ranked"][player["uuid"]]
        ranks_added += vals[key + "_ranked"]
        score_added += vals[key + "_score"]
        ranks_amount += 1
        score_amount += 1
    vals["avg_rank"] = ranks_added / ranks_amount
    vals["avg_score"] = score_added / score_amount
    new_values.append(vals)

with open('ranked.json', 'w', encoding='utf-8') as f:
    new_values = sorted(new_values, key=lambda k: k["avg_score"], reverse=True)
    json.dump(new_values, f, ensure_ascii=False, indent=4)
