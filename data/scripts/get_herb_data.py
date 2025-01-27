import json

paths = {
    "en_common": "../en/common_names.json",
    "fr_common": "../fr/common_names.json",
    "en_desc": "../en/short_descriptions.json",
    "fr_desc": "../fr/short_descriptions.json"
}

GREEN = "\033[32m"
RESET = "\033[0m"

def load_json(file_path):
    """Charge un fichier JSON et retourne son contenu."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erreur: Le fichier {file_path} est introuvable.")
        return None
    except json.JSONDecodeError:
        print(f"Erreur: Le fichier {file_path} n'est pas un JSON valide.")
        return None

def get_plant_info(plant_key):
    """Récupère les informations sur la plante à partir des fichiers JSON."""
    en_common = load_json(paths["en_common"])
    fr_common = load_json(paths["fr_common"])
    en_desc = load_json(paths["en_desc"])
    fr_desc = load_json(paths["fr_desc"])

    if en_common and fr_common:
        print(f"\n{GREEN}Nom anglais:{RESET} {en_common.get(plant_key, 'Non trouvé')}")
        print(f"{GREEN}Nom français:{RESET} {fr_common.get(plant_key, 'Non trouvé')}")

    if en_desc and fr_desc:
        print(f"\n{GREEN}Description anglaise:{RESET} {en_desc.get(plant_key, 'Non trouvé')}")
        print(f"\n{GREEN}Description française:{RESET} {fr_desc.get(plant_key, 'Non trouvé')}")

def main():
    """Fonction principale pour gérer la boucle de l'utilisateur."""
    while True:
        plant_key = input("\nEntrez la clé d'une plante médicinale (ou 'quit' pour quitter): ").strip()
        if plant_key.lower() == 'quit':
            print("Fin du programme.")
            break
        get_plant_info(plant_key)

if __name__ == "__main__":
    main()
