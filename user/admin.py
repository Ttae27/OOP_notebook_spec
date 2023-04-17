#!how to authenticate api???

endpoint "notebookspec.com/admin/product/add"
    def add(json_file):
        product.add(jsonfile)
        return status_code and new json

endpoint "notebookspec.com/admin/product/modify"
    def modify(product_id :int, value_to_modify :list???):
        #?Probably need to change value format??
        product.modify(product_id, value_to_modify)
        #* Should return status/error, error message, new json file
        pass

endpoint "notebookspec.com/admin/product/delete"
    def delete(product_id):
        product.delete(product_id)
        return status_code and new json

#######################################################################

endpoint "notebookspec.com/admin/user/add"
    def add(json_file):
        user.add(jsonfile)
        return status_code and new json

endpoint "notebookspec.com/admin/user/modify"
    def modify(user_id :int, value_to_modify :list???):
        #?Probably need to change value format??
        user.modify(user_id, value_to_modify)
        #* Should return status/error, error message, new json file
        pass

endpoint "notebookspec.com/admin/user/delete"
    def delete(user_id):
        user.delete(user_id)
        return status_code and new json