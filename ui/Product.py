import sqlite3
class Product():
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
            print(type_quries)
            print(query)

            cursor.execute(query)
        else:
            query = f"SELECT * FROM {cat}" #select all product
            cursor.execute(query)

        products = cursor.fetchall()
        conn.commit()
        conn.close()
        return products

    def delete(cat, product_id):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE from " + cat + " WHERE id = (?)", product_id)
        conn.commit()
        conn.close()
        return {'status': 'Successfully delete product ' + str(product_id)}

    def modify(cat, product_id, product_key, product_value):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE " + cat + " SET " + product_key + " = " + product_value + " WHERE id = " + product_id)
        conn.commit()
        conn.close()
        return {'status': 'Successfully modify product ' + str(product_id)}

    def add(cat, product):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO " + cat + " VALUES ", product)
        conn.commit()
        conn.close()
        return {'status': 'Successfully add product'}


#!test
print(Product.get('cpu', {'brand_name': ['INTEL'], 'series': ['Core i3', 'Ryzen 7']}))