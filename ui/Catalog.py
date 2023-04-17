endpoint "notebookspec.com/products/{product_cat}"
    current_cat = products.get({product_cat}, optional filter :???, optional sort: int)
    if (sort):
        current_cat.sort(key = ???) #*https://www.w3schools.com/python/python_lists_sort.asp
    
    return current_cat in json format

endpoint "notebookspec.com/products/compare"
    def compare(product_id_1, product_id_2):
        compare = [product.get(product_id_1),
                    product.get(product_id_2)
                    ]
        #*change format to json
        return the json

