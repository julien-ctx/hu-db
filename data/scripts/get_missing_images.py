import os
import json

json_file_path = '../herbs.json'
images_directory = '../../images/'

try:
    with open(json_file_path, 'r', encoding='utf-8') as file:
        herbs = json.load(file)
except FileNotFoundError:
    print(f"Error: The file {json_file_path} was not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: Failed to parse {json_file_path} as JSON.")
    exit(1)

missing_images = []

for herb in herbs:
    if 'key' not in herb:
        print("Warning: An object in the JSON array is missing the 'key' field.")
        continue

    key = herb['key']
    image_file = f"{key}.jpg"
    image_path = os.path.join(images_directory, image_file)

    if not os.path.isfile(image_path):
        missing_images.append(image_file)

if missing_images:
    print("The following images are missing:")
    for image in missing_images:
        print(f"{image}".replace(".jpg", ""))
else:
    print("All images are present.")
