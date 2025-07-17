class SweetShop:
    def __init__(self):
        self.sweets = {}

    # To add Sweets
    def add_sweet(self, id, name, category, price, quantity):
        if id in self.sweets:
            raise ValueError("Sweet ID already exists.")
        self.sweets[id] = {
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }

    # To Delete Sweets    
    def delete_sweet(self, id):
        if id not in self.sweets:
            raise KeyError("Sweet ID not found.")
        del self.sweets[id]

    # To view Sweets
    def view_sweets(self):
        return list(self.sweets.values())

    # To search Sweets
    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        result = []
        for sweet in self.sweets.values():
            if name and name.lower() not in sweet["name"].lower():
                continue
            if category and category.lower() != sweet["category"].lower():
                continue
            if min_price and sweet["price"] < min_price:
                continue
            if max_price and sweet["price"] > max_price:
                continue
            result.append(sweet)
        return result
    
    # To Sort Sweets
    def sort_sweets(self, key="name", reverse=False):
        return sorted(self.sweets.values(), key=lambda x: x[key], reverse=reverse)

    # To purchase sweets
    def purchase_sweet(self, id, qty):
        if id not in self.sweets:
            raise KeyError("Sweet not found.")
        if self.sweets[id]["quantity"] < qty:
            raise ValueError("Not enough stock.")
        self.sweets[id]["quantity"] -= qty

    # To Restock Sweets
    def restock_sweet(self, id, qty):
        if id not in self.sweets:
            raise KeyError("Sweet not found.")
        self.sweets[id]["quantity"] += qty


