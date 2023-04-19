import requests
import json

# Define the dictionary
my_dict = {'brand_name': ['AMD'], 'series': ['Ryzen 3', 'Ryzen 7']}

# Convert the dictionary to a string
my_dict_str = json.dumps(my_dict)

# Encode the string
my_dict_encoded = requests.utils.quote(my_dict_str)

print(my_dict_encoded)
