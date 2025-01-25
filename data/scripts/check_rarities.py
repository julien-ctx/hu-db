import json

with open('../rarities.json', 'r') as rarities_file:
    valid_rarities = json.load(rarities_file)

with open('../herbs.json', 'r') as herbs_file:
    herbs_data = json.load(herbs_file)

def check_rarity(data, valid_rarities):
    for item in data:
        rarity = item.get('description', {}).get('rarity', "")
        
        if rarity not in valid_rarities:
            print(f"ID {item['id']} : Invalid rarity: {rarity}")

check_rarity(herbs_data, valid_rarities)
