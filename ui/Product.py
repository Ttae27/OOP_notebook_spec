import sys
import sqlite3

# import data.py
sys.path.append('../oop_notebook_spec')
from data import *

class Product():
    def __init__(self) -> None:
        self.current_product = [] #store the current showing product

    def get(self, cat, filter=None):
        self.current_product = get_product(cat)
        def dict_factory(cursor, row):#convert list of tuple to list of dict
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        conn = sqlite3.connect('data/database.db')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        query = f"SELECT * FROM {cat}" #select all product
        cursor.execute(query)

    #     products = cursor.fetchall()
    #     conn.commit()
    #     conn.close()
    #     return products

    # def get(self, cat: str, filter :dict = None):
    #     def dict_factory(cursor, row):#convert list of tuple to list of dict
    #         d = {}
    #         for idx, col in enumerate(cursor.description):
    #             d[col[0]] = row[idx]
    #         return d
    #     conn = sqlite3.connect('data/database.db')
    #     conn.row_factory = dict_factory
    #     cursor = conn.cursor()
    #     product_list = data.get_list(cat)
    #     if filter:
    #         # Create filter query
    #         # type_quries = []
    #         # for type in filter.keys():
    #         #     #Change from list to tuple, if list has one item format to ('item')
    #         #     type_filter_tuple = f"('{filter[type][0]}')" if len(filter[type]) == 1 else tuple(filter[type])
    #         #     type_query = f"{type} IN {type_filter_tuple}"
    #         #     type_quries.append(type_query)
    #         # type_quries = ' AND '.join(type_quries)
    #         # query = f"SELECT * FROM {cat} WHERE {type_quries}"
    #         # cursor.execute(query)
    #         for key,value in filter:
    #             if 


    #     else:
    #         query = f"SELECT * FROM {cat}" #select all product
    #         cursor.execute(query)

    #     products = cursor.fetchall()
    #     conn.commit()
    #     conn.close()
    #     return products

    def delete_product(self, cat: str, product_id: int):
        for product in self.current_product:
            if product.id == product_id:
                self.current_product = delete_data(cat, product_id)
                return {'status': 'Successfully delete product ' + str(product_id)}
        return {'status': 'Failed delete product'}

    def update_price_product(self, cat: str, product_id: int, new_price: int):
        for product in self.current_product:
            if product.id == product_id:
                self.current_product = update_price_data(cat, product_id, new_price)
                return {'status': 'Successfully modified product ' + str(product_id)}
        return {'status': 'Failed modified product'}

    def add_product(self, cat, new_product: dict):
        for product in self.current_product:
            if product.id == new_product['id']:
                return {'status': 'Failed to added product'}
        new_product = tuple(new_product.values())
        self.current_product = add_data(cat, new_product)
        return {'status': 'Successfully added product'}