"""
Objective : build program that build table(list and dict) from CSV file
then put it in another table call class TableDB

class Table
> whole list that come from CSV file
- represent CSV file
- filter out not want data
> state variable :
    1.row
    2.line

class TableDB:
- collect Table
> attribute
    1. list
"""
#transfer CSV to list file
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

class TableDB:
    def __init__(self):
        self.databased = []
    def insert(self, table:object):
        if not isinstance(table ,Table):
            raise TypeError
        self.databased.append(table)
    def search(self, table_name):
        answer = None
        for items in self.databased:
            if items.table_name == table_name :
                answer = items
        return answer

class Table:
    def __init__(self, table_name = 'table', table = []):
        self.table_name = table_name
        self.table = table
    def filter(self, condition):
        filter_list = []
        for item in self.table:
            if condition(item):
                filter_list.append(item)
        return filter_list
    def aggregate(self, aggregation_function, aggregation_key):
        aggr_value = {}
        for item in self.table:
            aggr_value[item['city']] = item[aggregation_key]
        if aggregation_function is not None:
            aggr_value = aggregation_function(aggr_value)
        return aggr_value
    def read_value(self, say, say2):
        if type(self.table) == dict:
            for items,value in self.table.items() :
                print(f"{say} of {items:<10} in {say2} is {value}  ")
    def __str__(self):
        return f"{self.table}\n"
    def __repr__(self):
        return self.__str__()

# Change to OOP format and contain in DB
cities_oop = Table("cities", cities)
countries_oop = Table("countries", countries)
DB = TableDB()
DB.insert(cities_oop)
DB.insert(countries_oop)

# Build separate Table for each interested country
Italy_all_info = cities_oop.filter(lambda _x: _x['country'] == 'Italy')
Sweden_all_info = cities_oop.filter(lambda _x: _x['country'] == 'Sweden')
Italy = Table("Italy", Italy_all_info)
Sweden = Table("Sweden", Sweden_all_info)
DB.insert(Italy)
DB.insert(Sweden)

## aggregate only temperature
# Build and store all temperature of cities in Italy
operate = DB.search("Italy")
list_temp_Italy = operate.aggregate(aggregation_function = None, aggregation_key = "temperature")
temp_Italy = Table("temperature_Italy", list_temp_Italy)
DB.insert(temp_Italy)
# Build and store all temperature of cities in Sweden
operate = DB.search("Sweden")
list_temp_Sweden = operate.aggregate(aggregation_function = None, aggregation_key = "temperature")
temp_Sweden = Table("temperature_Sweden", list_temp_Sweden)
DB.insert(temp_Sweden)


# - print the average temperature for all the cities in Italy
print("the average temperature for all the cities in Italy")
operate = DB.search("temperature_Italy")
operate.read_value("temperature", "Italy")
print()
# - print the average temperature for all the cities in Sweden
print("the average temperature for all the cities in Sweden")
operate = DB.search("temperature_Sweden")
operate.read_value("temperature", "Sweden")
print()
# - print the min temperature for all the cities in Italy
operate = DB.search("Italy")
min_temp_Italy = operate.aggregate(aggregation_function = lambda x: min(x.values()), aggregation_key = "temperature")
print(f"min temperature in Italy is {min_temp_Italy}")
# - print the max temperature for all the cities in Sweden
operate = DB.search("Sweden")
max_temp_Sweden = operate.aggregate(aggregation_function = lambda x: max(x.values()), aggregation_key = "temperature")
print(f"max temperature in Sweden in {max_temp_Sweden}")