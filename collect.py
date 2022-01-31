from enum import unique
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")


STRANDED_SWEATS_GUILD_ID = "61cdf8b48ea8c981ac653ff1"
BASE_API_URL = "https://api.hypixel.net"
GUILD_PATH = "/guild"
SKYBLOCK_PROFILES_PATH = "/skyblock/profiles"
STRANDED_GAMEMODE_NAME = "island"
MOJANG_UUID_TO_NAME = "https://api.mojang.com/user/profiles/{}/names"


def getAPIData(path: str, prms = {}) -> dict:
    prms["key"] = API_KEY
    r = requests.get(BASE_API_URL + path, params=prms)
    data = r.json()
    if data["success"]:
        return data
    else: raise Exception ("Something went wrong while retrieving data!")


def getGuildData(guild_id: str) -> dict: return getAPIData(GUILD_PATH, {"id": guild_id})["guild"]
def getUserProfiles(uuid: str) -> dict: return getAPIData(SKYBLOCK_PROFILES_PATH, {"uuid": uuid})["profiles"]

def getGuildMembers(guild_id: str) -> list:
    data = getGuildData(guild_id)
    return [member["uuid"] for member in data["members"]]

def getStrandedGamemodesFromPlayer(uuid: str) -> dict:
    profiles = getUserProfiles(uuid)
    stranded_gamemode = {"members": {uuid: {"last_save": 0}}}
    for profile in profiles:
        if not "game_mode" in profile: continue
        if profile["game_mode"] == STRANDED_GAMEMODE_NAME:
            if stranded_gamemode["members"][uuid]["last_save"] < profile["members"][uuid]["last_save"]:
                stranded_gamemode = profile
    return stranded_gamemode

def getKeyFromData(data: dict, key: str) -> str:
    try:
        return data[key]
    except Exception as e:
        return 0

def getMiningExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_mining")
def getAlchemyExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_alchemy")
def getTamingExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_taming")
def getEnchantingExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_enchanting")
def getFishingExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_fishing")
def getForagingExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_foraging")
def getCarpentryExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_carpentry")
def getCombatExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_combat")
def getSocialExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_social")
def getRunecraftingExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_runecrafting")
def getFarmingExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_farming")
def getFishingExp(member_data: dict): return getKeyFromData(member_data, "experience_skill_fishing")

def getUsernameFromUUID(uuid: str):
    data = requests.get(MOJANG_UUID_TO_NAME.format(uuid)).json()
    name = data[len(data) - 1]["name"]
    return name

def getPrefix(uuid: str):
    if uuid == "3b105f27ec6e479dadf66096fa9c5a60": return "[DEVELOPER] "
    if uuid == "ffb6f7b41b21499089e9bcd57ffabd67": return "[BRIDGE] "
    if uuid == "6fe716ba52f54acc9cff621353829a11": return "[GET SOME SLEEP BRO] "
    if uuid == "f08cdc8dfba347d78e280120bab54441": return "[CERTIFIED NERD] "
    return ""

def getUniqueMinions(member_data: dict): 
    crafted_generators = getKeyFromData(member_data, "crafted_generators")
    if not crafted_generators: return 0
    return len(crafted_generators)
def getUniquePets(member_data: dict): 
    pets = getKeyFromData(member_data, "pets")
    if not pets: return 0
    return len(pets)
def getUniqueCollection(member_data: dict): 
    total = 0
    if not getKeyFromData(member_data, "collection"): return 0

    for collec in getKeyFromData(member_data, "collection"):
        if not "_BLOCK" in collec: total += 1
    return total
def getProfileBalance(stranded_profile_data: dict):
    if not "banking" in stranded_profile_data: total_bal = 0
    else: total_bal = stranded_profile_data["banking"]["balance"]
    for member in stranded_profile_data["members"]:
        if not "coin_purse" in stranded_profile_data["members"][member]: total_bal += 0
        else: total_bal += stranded_profile_data["members"][member]["coin_purse"]
    return total_bal

def generatePlayerData(uuid: str) -> dict:
    stranded_profile_data = getStrandedGamemodesFromPlayer(uuid)

    member_data = stranded_profile_data["members"][uuid]
    suffix = ""
    if not getForagingExp(member_data): suffix = " (API IS OFF? Or they are just bald)"
    if member_data["last_save"] == 0: suffix = " (NOT EVEN PLAYING STRANDED WTF)"

    player_data = {
        "uuid": uuid,
        "prefix": getPrefix(uuid),
        "suffix": suffix,
        "username": getUsernameFromUUID(uuid),
        "unique_pets": getUniquePets(member_data),
        "mining_exp": getMiningExp(member_data),
        "alchemy_exp": getAlchemyExp(member_data),
        "taming_exp": getTamingExp(member_data),
        "enchanting_exp": getEnchantingExp(member_data),
        "foraging_exp": getForagingExp(member_data),
        # "carpentry_exp": getCarpentryExp(member_data),
        "combat_exp": getCombatExp(member_data),
        # "social_exp": getSocialExp(member_data),
        # "runecrafting_exp": getRunecraftingExp(member_data),
        "farming_exp": getFarmingExp(member_data),
        "fishing_exp": getFishingExp(member_data),
        "collections_unlocked": getUniqueCollection(member_data),
        "unique_minions": getUniqueMinions(member_data),
        "profile_bank": getProfileBalance(stranded_profile_data)
    }
    return player_data






members = ['3badbf28742f416296232e3714077d09']
members = [*members, *getGuildMembers(STRANDED_SWEATS_GUILD_ID)]

total_members = len(members)
data = []
current_members_done = 0
for member in members:
    current_members_done += 1
    dt = generatePlayerData(member)
    data.append(dt)
    print(f"{current_members_done}/{total_members}: {dt['prefix']}{dt['username']}{dt['suffix']}")



with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
