import json

with open('../symptoms.json', 'r') as symptoms_file:
    valid_symptoms = json.load(symptoms_file)

with open('../herbs.json', 'r') as herbs_file:
    herbs_data = json.load(herbs_file)

def check_symptoms(herbs_data, valid_symptoms):
    for herb in herbs_data:
        if 'properties' in herb:
            if 'top_choices_ailments' in herb['properties']:
                invalid_ailments = [ailment for ailment in herb['properties']['top_choices_ailments'] if ailment not in valid_symptoms]
                if invalid_ailments:
                    print(f"Herb '{herb.get('key', 'Unnamed')}' has invalid top_choices_ailments: {', '.join(invalid_ailments)}")
            
            if 'other_options_ailments' in herb['properties']:
                invalid_ailments = [ailment for ailment in herb['properties']['other_options_ailments'] if ailment not in valid_symptoms]
                if invalid_ailments:
                    print(f"Herb '{herb.get('key', 'Unnamed')}' has invalid other_options_ailments: {', '.join(invalid_ailments)}")
        else:
            print(f"Herb '{herb.get('key', 'Unnamed')}' does not have 'properties' property.")

check_symptoms(herbs_data, valid_symptoms)
