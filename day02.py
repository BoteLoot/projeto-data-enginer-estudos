def total_population(populations):
    total = sum(populations.values())
    return total

cities = ["Belo Horizonte", "Rio de Janeiro", "São Paulo", "Brasília", "Salvador"]
populations = {"Belo Horizonte": 2570000, "Rio de Janeiro": 3120000, "São Paulo": 11880000, "Brasília": 3120000, "Salvador": 2840000}
# Print the population of each city
for city in cities:
    population = populations[city]
    print(f"The population of {city} is {population}.")
# Calculate and print the total population
total_pop = total_population(populations)
print(f"The total population of the listed cities is {total_pop}.")