import csv
def city_classification(population):
    if population > 1000000:
        return "Metropolis"
    elif population > 500000:
        return "Large City"
    elif population > 100000:
        return "Medium City"
    else:
        return "Small City"
cities = {"Belo Horizonte": 257000, "Rio de Janeiro": 3120000, "São Paulo": 11880000, "Brasília": 3120000, "Salvador": 2840000}

with open('cities.csv',mode='w',newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['City', 'Population', 'Classification'])
    for city, population in cities.items():
        classification = city_classification(population)
        writer.writerow([city, population, classification])

try:
    with open('cities.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            city, population, classification = row
            print(f"{city} is classified as a {classification}.")
except FileNotFoundError:
    print("Error: The file 'cities.csv' was not found.")