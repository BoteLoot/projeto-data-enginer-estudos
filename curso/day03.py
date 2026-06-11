def city_classification(population):
    if population > 1000000:
        return "Metropolis"
    elif population > 500000:
        return "Large City"
    elif population > 100000:
        return "Medium City"
    else:
        return "Small City"
    
cities = ["Belo Horizonte", "Rio de Janeiro", "São Paulo", "Pará de Minas", "Salvador"]
populations = {"Belo Horizonte": 257000, "Rio de Janeiro": 3120000, "São Paulo": 11880000, "Pará de Minas": 50000, "Salvador": 2840000}

# Classify and print the classification of each city    
for city in cities:
    try:
        population = populations[city]
        classification = city_classification(population)
        print(f"{city} is classified as a {classification}.")
    except KeyError as e:
        print(f"Error: City '{e.args[0]}' not found in the population data.")