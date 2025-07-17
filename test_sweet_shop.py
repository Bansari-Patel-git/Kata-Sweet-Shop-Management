from sweet_shop import SweetShop

def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet("001", "Ladoo", "Candy", 10, 100)
    assert "001" in shop.sweets

def test_delete_sweet():
    shop = SweetShop()
    shop.add_sweet("001", "Ladoo", "Candy", 10, 100)
    shop.delete_sweet("001")
    assert "001" not in shop.sweets

def test_view_sweets():
    shop = SweetShop()
    shop.add_sweet("001", "Ladoo", "Candy", 10, 100)
    shop.add_sweet("002", "Barfi", "Candy", 15, 50)
    sweets = shop.view_sweets()
    assert len(sweets) == 2

def test_search_by_category():
    shop = SweetShop()
    shop.add_sweet("001", "Ladoo", "Candy", 10, 100)
    shop.add_sweet("002", "Brownie", "Pastry", 25, 20)
    results = shop.search_sweets(category="Candy")
    assert len(results) == 1
    assert results[0]["name"] == "Ladoo"

def test_sort_by_price():
    shop = SweetShop()
    shop.add_sweet("001", "Ladoo", "Candy", 20, 50)
    shop.add_sweet("002", "Barfi", "Candy", 10, 100)
    sorted_sweets = shop.sort_sweets("price")
    assert sorted_sweets[0]["name"] == "Barfi"

def test_purchase_sweet():
    shop = SweetShop()
    shop.add_sweet("001", "Ladoo", "Candy", 10, 100)
    shop.purchase_sweet("001", 20)
    assert shop.sweets["001"]["quantity"] == 80

def test_restock_sweet():
    shop = SweetShop()
    shop.add_sweet("001", "Ladoo", "Candy", 10, 50)
    shop.restock_sweet("001", 50)
    assert shop.sweets["001"]["quantity"] == 100
