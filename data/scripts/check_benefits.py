import json

with open('../benefits.json', 'r') as benefits_file:
    valid_benefits = json.load(benefits_file)

with open('../herbs.json', 'r') as herbs_file:
    herbs_data = json.load(herbs_file)

def check_benefits(data, valid_benefits):
    for item in data:
        benefits = item.get('properties', {}).get('benefits', [])
        
        invalid_benefits = [benefit for benefit in benefits if benefit not in valid_benefits]
        
        if invalid_benefits:
            print(f"ID {item['id']} : Invalid benefits: {', '.join(invalid_benefits)}")

check_benefits(herbs_data, valid_benefits)
