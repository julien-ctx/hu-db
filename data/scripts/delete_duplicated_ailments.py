import json

# Load herbs.json file
with open('../herbs.json', 'r') as herbs_file:
    herbs_data = json.load(herbs_file)

def remove_duplicate_ailments(herbs_data):
    for herb in herbs_data:
        if 'properties' in herb:
            top_choices_ailments = set(herb['properties'].get('top_choices_ailments', []))
            other_options_ailments = set(herb['properties'].get('other_options_ailments', []))
            
            common_ailments = top_choices_ailments & other_options_ailments
            
            if common_ailments:
                updated_other_options = other_options_ailments - top_choices_ailments
                herb['properties']['other_options_ailments'] = list(updated_other_options)
                
                print(f"Removed {', '.join(common_ailments)} from 'other_options_ailments' of '{herb.get('key', 'Unnamed')}'.")
        else:
            print(f"Herb '{herb.get('key', 'Unnamed')}' does not have 'properties' property.")

remove_duplicate_ailments(herbs_data)

with open('../herbs_modified.json', 'w') as modified_file:
    json.dump(herbs_data, modified_file, indent=4)
