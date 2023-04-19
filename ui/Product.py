import sqlite3
from data import *

class Product():
    def __init__(self) -> None:
        pass

    def get(cat: str, filter :dict = None):
        def dict_factory(cursor, row):#convert list of tuple to list of dict
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        conn = sqlite3.connect('data/database.db')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        
        if filter:
            # Create filter query
            type_quries = []
            for type in filter.keys():
                #Change from list to tuple, if list has one item format to ('item')
                type_filter_tuple = f"('{filter[type][0]}')" if len(filter[type]) == 1 else tuple(filter[type])
                type_query = f"{type} IN {type_filter_tuple}"
                type_quries.append(type_query)
            type_quries = ' AND '.join(type_quries)
            query = f"SELECT * FROM {cat} WHERE {type_quries}"
            cursor.execute(query)
        else:
            query = f"SELECT * FROM {cat}" #select all product
            cursor.execute(query)

        products = cursor.fetchall()
        conn.commit()
        conn.close()
        return products

    def delete_product(cat, product_id):
        list_cat = get_list(cat)
        for lst in list_cat:
            if lst.id == product_id:
                list_cat.remove(lst)
                return {'status': 'Successfully delete product ' + str(product_id)}
        return {'status': 'Failed delete product'}

    def modify_product(cat, product_id, product_key, product_value):
        list_cat = get_list(cat)
        for lst in list_cat:
            if lst.id == product_id:
                lst.product_key = product_value
                return {'status': 'Successfully modified product ' + str(product_id)}
        return {'status': 'Failed modified product'}

    def add_product(cat, product):
        list_cat = get_list(cat)
        for lst in list_cat:


#!test
#print(Product.get('cpu', {'brand_name': ['INTEL'], 'series': ['Core i3', 'Ryzen 7']}))
