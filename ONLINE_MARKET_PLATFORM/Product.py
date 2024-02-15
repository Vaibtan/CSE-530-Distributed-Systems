from dataclasses import dataclass


ALLOWED_CATEGORY_TYPES = ["ELECTRONICS", "FASHION", "OTHERS"]

@dataclass
class Item:
    def __init__(self, id, name, category, quantity, description, price, rating, seller_address):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.description = description
        self.price = price
        self.rating = rating
        self.seller_address = seller_address
        

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Description: {self.description}, Price: {self.price}, Rating : {self.rating}, Seller Address: {self.seller_address}"
    
    @staticmethod
    def show_all_items(items):
        for item in items: print(item)

    @staticmethod
    def filter_by_name(items, name):
        return [item for item in items if name.lower() in item.name.lower()]

    @staticmethod
    def filter_by_category(items, category):
        return [item for item in items if category.lower() in item.category.lower()]

    @staticmethod
    def filter_items_double(items, name = None, category = None):
        results = []
        for item in items:
            if (name is None or item.name.lower() in name.lower()) and \
               (category is None or item.category.lower() in category.lower()):
                results.append(item)
        return results
    

#item = Item(1, "iPhone", "Electronics", 5, 
#    "iPhone 15.", "192.13.188.178:50052", "$500")
