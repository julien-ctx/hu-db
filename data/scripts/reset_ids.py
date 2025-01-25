import json

def update_herbs_json(input_file, output_file):
    with open(input_file, 'r') as f:
        herbs = json.load(f)

    for index, herb in enumerate(herbs):
        herb.pop('id', None)
        herb = {'id': index} | herb

    with open(output_file, 'w') as f:
        json.dump(herbs, f, indent=4)

update_herbs_json('../herbs.json', 'updated_herbs.json')
