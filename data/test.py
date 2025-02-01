import json

# Charger les fichiers JSON
with open('symptoms.json', 'r') as f:
    symptoms_data = json.load(f)

with open('herbs.json', 'r') as f:
    herbs_data = json.load(f)

# Demander à l'utilisateur de saisir un symptôme
user_input = input("Entrez un symptôme (par exemple, 'acne'): ").strip()

# Rechercher l'objet correspondant au symptôme
symptom = None
for s in symptoms_data:
    if s["key"] == user_input:
        symptom = s
        break

if symptom:
    # Trouver les herbes recommandées pour ce symptôme
    recommended_herbs = symptom["recommended_herbs"]
    
    print(f"Herbes recommandées pour '{user_input}':")
    
    # Rechercher les informations sur chaque herbe recommandée
    for herb_id in recommended_herbs:
        # Trouver l'herbe correspondante dans herbs.json
        herb = next((h for h in herbs_data if h["id"] == herb_id), None)
        if herb:
            # Afficher le nom scientifique de l'herbe
            print(f"- {herb['scientific_name']}")
else:
    print(f"Le symptôme '{user_input}' n'a pas été trouvé.")
