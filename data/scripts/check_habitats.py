import json

with open('../habitats.json', 'r') as habitats_file:
    valid_habitats = json.load(habitats_file)

with open('../herbs.json', 'r') as herbs_file:
    herbs_data = json.load(herbs_file)

def check_habitats(data, valid_habitats):
    for item in data:
        habitat = item.get('description', {}).get('habitat', "")
        
        if habitat not in valid_habitats:
            print(f"ID {item['id']} : Invalid habitat: {habitat}")

check_habitats(herbs_data, valid_habitats)
