# Modèle d'entrée
test = {'Croissant': 150, 'Orange juice': 250}
deuxieme = {"Croissants, cheese": 150, "Orange juice, raw": 250}

# Liste centrale des nutriments pour le principe DRY
NUTRIENTS = ['calories', 'total_fat', 'protein', 'carbohydrate', 'sugars']

def calculate_apport_calorique(food: str, quantity: float, nutrition_db: dict) -> dict:
    """Calcule les apports pour un aliment unique de manière explicite et sécurisée."""
    # .get() protège contre une absence de clé dans la fiche de l'aliment
    food_stats = nutrition_db.get(food, {})
    factor = quantity / 100.0
    
    # Extraction explicite par clé : élimine le risque de désalignement
    return {nutrient: food_stats.get(nutrient, 0.0) * factor for nutrient in NUTRIENTS}


def nutritional_summary(intake: dict, nutrition_db: dict) -> dict | str:
    """Calcule le résumé global en mode streaming (accumulateur)."""
    # Initialisation de l'accumulateur (Évite les listes intermédiaires en mémoire)
    total_consumption = {nutrient: 0.0 for nutrient in NUTRIENTS}
    
    # Boucle directe sur l'itérateur (Consommation RAM minimale)
    for food, quantity in intake.items():
        if food not in nutrition_db:
            return food  # Sortie immédiate si l'aliment est inconnu
            
        # Calcul pour l'aliment actuel
        apport_aliment = calculate_apport_calorique(food, quantity, nutrition_db)
        
        # Accumulation directe et sécurisée par clé
        for nutrient in NUTRIENTS:
            total_consumption[nutrient] += apport_aliment[nutrient]
            
    return total_consumption

# Exécution propre (en passant le dictionnaire de nutrition en paramètre pour éviter les variables globales masquées)
# print(nutritional_summary(test, nutrition_dict))
# print(nutritional_summary(deuxieme, nutrition_dict))