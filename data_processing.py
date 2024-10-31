import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps) / len(temps))
print()

# Print all cities in Italy
cities_temp = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        cities_temp.append(city['city'])
print("All the cities in", my_country, ":")
print(cities_temp)
print()

# Print the average temperature for all the cities in Italy
# Write code for me
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The average temperature of all the cities in", my_country, ":")
print(sum(temps) / len(temps))
print()

# Print the max temperature for all the cities in Italy
# Write code for me
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The max temperature of all the cities in", my_country, ":")
print(max(temps))
print()

# Print the min temperature for all the cities in Italy
# Write code for me
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The min temperature of all the cities in", my_country, ":")
print(min(temps))
print()


# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list

# x = filter(lambda _x: _x['country'] == 'Italy', cities)
# print(x)
# for item in x:
#     print(item)

# Let's write a function to do aggregation given an aggregation function and an aggregation key
# function what you want to do find max , average , etc.
# key what you what to search temp ....
def aggregate(aggregation_key, aggregation_function, dict_list):
    aggr_value = {}
    for item in dict_list :
        aggr_value[item['city']] = item[aggregation_key]
    if aggregation_function is not None:
        aggr_value = aggregation_function(aggr_value)
    return aggr_value

# Let's write code to
_Italy = filter(lambda _x: _x['country'] == 'Italy', cities)
_Sweden = filter(lambda _x: _x['country'] == 'Sweden', cities)

# - print the average temperature for all the cities in Italy
avg_Italy = aggregate('temperature', None, _Italy)
for items,value in avg_Italy.items():
    print('temperature of',items ,'in Italy is ',value  )
print()

# - print the average temperature for all the cities in Sweden
avg_Sweden = aggregate('temperature', None, _Sweden)
for items,value in avg_Sweden.items():
    print('temperature of',items ,'in Sweden is ',value  )
print()

# - print the min temperature for all the cities in Italy
min_Italy = aggregate('temperature', lambda x: min(x.values()) , _Italy)
print(f"min temperature in Italy is {min_Italy}"+'\n')

# - print the max temperature for all the cities in Sweden
max_Sweden = aggregate('temperature', lambda x: max(x.values()) , _Sweden)
print(f"max temperature in Sweden in {max_Sweden}")