import json

with open('../geographical_areas.json', 'r') as areas_file:
    valid_geographical_areas = json.load(areas_file)

with open('../herbs.json', 'r') as herbs_file:
    herbs_data = json.load(herbs_file)

def check_geographical_areas(data, valid_geographical_areas):
    for item in data:
        geographical_areas = item.get('description', {}).get('geographical_areas', [])
        
        invalid_areas = [area for area in geographical_areas if area not in valid_geographical_areas]
        
        if invalid_areas:
            print(f"ID {item['id']} : Invalid geographical areas: {', '.join(invalid_areas)}")

check_geographical_areas(herbs_data, valid_geographical_areas)
