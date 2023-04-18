import sqlite3
class Product():
    def __init__(self) -> None:
        pass

    def get(type: str, filter =  None):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM " + type)
        products = cursor.fetchall()
        conn.commit()
        conn.close()
        print(products)
        return products

    def delete(type, product_id):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE from " + type + " WHERE id = (?)", product_id)
        conn.commit()
        conn.close()
        return {'status': 'Successfully delete product ' + str(product_id)}

    def modify(type, product_id, product_key, product_value):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE " + type + " SET " + product_key + " = " + product_value + " WHERE id = " + product_id)
        conn.commit()
        conn.close()
        return {'status': 'Successfully modify product ' + str(product_id)}

    def add(type, product):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO " + type + " VALUES ", product)
        conn.commit()
        conn.close()
        return {'status': 'Successfully add product'}
