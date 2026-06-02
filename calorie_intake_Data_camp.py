# Start coding here!
# Use as many cells as you need.
test = {
    'Croissant': 150, 'Orange juice': 250
}

deuxieme ={"Croissants, cheese": 150, "Orange juice, raw": 250}
# Calculer l'apport
def calculate_apport_calorique(food, quantity):
    result = {}
    calories = nutrition_dict[food]['calories'] / 100
    total_fat = nutrition_dict[food]['total_fat'] / 100
    protein = nutrition_dict[food]['protein'] / 100
    carbohydrate = nutrition_dict[food]['carbohydrate'] / 100
    sugars = nutrition_dict[food]['sugars'] / 100
    result['calories'] = calories * quantity
    result['total_fat'] = total_fat * quantity
    result['protein'] = protein * quantity
    result['carbohydrate'] = carbohydrate * quantity
    result['sugars'] = sugars * quantity

    return result

# some des apports de l'intake
def sum_of_intakes(list_of_intakes):
    calories, total_fat, protein, carbohydrate, sugars = 0, 0, 0, 0, 0

    for each_intake in list_of_intakes:
        c, f, p, carb, s = each_intake.values()
        calories += c
        total_fat += f
        protein += p
        carbohydrate += carb
        sugars += s

    total_consumption = {
        'calories': calories,
        'total_fat': total_fat,
        'protein': protein,
        'carbohydrate': carbohydrate,
        'sugars': sugars
    }

    return total_consumption

def nutritional_summary(intake):
    try:
        results_per_food = []
        
        for element in [*intake.items()]:
            food, quantity = element

            if food not in nutrition_dict:
                return food 

            result = calculate_apport_calorique(food, quantity)

            results_per_food.append(result)
        
        final_result = sum_of_intakes(results_per_food)
        
        return final_result
        
            
    except Exception as e:
        print(e)

nutritional_summary(test)
nutritional_summary(deuxieme)