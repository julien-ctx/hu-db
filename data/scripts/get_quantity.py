import json

with open('../herbs.json', 'r') as herbs_file:
    herbs_data = json.load(herbs_file)
    
print(len(herbs_data), "herbs")
