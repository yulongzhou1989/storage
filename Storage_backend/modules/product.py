class Product(object):

    def __init__(self, sku, product_name, shelf, quatity):
        self.sku = sku
        self.product_name = product_name
        self.shelf = shelf
        self.quatity = quatity

    def to_dict(self):
        return {
            'sku': self.sku,
            'prod_name': self.prod_name,
            'shelf':  self.shelf,
            'quatity': self.quatity
        }