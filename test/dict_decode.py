import json
from urllib.parse import unquote

encoded_str = "%7B%22brand_name%22%3A%20%5B%22INTEL%22%5D%2C%20%22series%22%3A%20%5B%22Core%20i3%22%2C%20%22Ryzen%207%22%5D%7D"
decoded_str = unquote(encoded_str)
decoded_dict = json.loads(decoded_str)
#!debug
print(decoded_dict)