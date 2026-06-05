from nutrition_dict import nutrition_dict

# Start coding here!
# Use as many cells as you need.
# Variable globale pour les fonctions et les tests
test_db1 = {
    'Cornstarch' : 450,
    'Nuts, pecans' : 40,
    'Eggplant, raw' : 50,
    'Croissants, cheese' : 150, 
    'Orange juice, raw' : 250
}

test_db2 = {
    'Croissant' : 150,
    'Orange juice' : 250,
    'Nama' : 1000,
    'Yaourt' : 500
}

test_db3 = {
    "Croissants, cheese": 150, 
    "Orange juice, raw": 250
}

# Nutrients take into account
NUTRIENTS = ['calories', 'total_fat', 'protein', 'carbohydrate', 'sugars']

# Fonction de calcul de l'apport nutritionel
def nutritional_intake(food, quantity, nutrition_dict):
    # Facteur de multiplication pour calcul de l'apport nutritionnel
    factor = quantity/100

    #recuperation de l'apport nutritionnel d'une nourriture
    food_stats = nutrition_dict.get(food, {})

    food_nutritional_intake = {nutrient : food_stats.get(nutrient, 0.0) * factor for nutrient in NUTRIENTS}

    #renvoi l'apport nutritionnel d'une nourriture
    return food_nutritional_intake

#
def nutritional_summary(intake):

    # Creation du l'apport total qui sera affiché
    total_intake = {nutrient : 0.0 for nutrient in NUTRIENTS}

    # Exraction de la consommation
    for food, quantity in intake.items():
        # Verification de l'existence de la nourriture
        if food not in nutrition_dict:
            print(food)
            return food

        # Calcul de l'apport nutritionnel
        food_nutritionnal_intake = nutritional_intake(food, quantity, nutrition_dict)

        # Ajout de l'apport de l'intake a l'intake total
        for nutrient in NUTRIENTS:
            total_intake[nutrient] += food_nutritionnal_intake[nutrient]

    # Affichage du resultat final
    print(total_intake)
    return total_intake
        

# Test
print("Test 1")
nutritional_summary(test_db1)
print("Test 2")
nutritional_summary(test_db2)
print("Test 3")
nutritional_summary(test_db3)