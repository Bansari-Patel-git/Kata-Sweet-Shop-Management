from sweet_shop import SweetShop

def main():
    shop = SweetShop()

    while True:
        print("\n====== Sweet Shop Management System ======")
        print("1. Add Sweet")
        print("2. Delete Sweet")
        print("3. View Sweets")
        print("4. Search Sweets")
        print("5. Sort Sweets")
        print("6. Purchase Sweet")
        print("7. Restock Sweet")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter sweet ID: ")
            name = input("Enter sweet name: ")
            category = input("Enter category (sweets/pastry/chocolate): ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            try:
                shop.add_sweet(id, name, category, price, quantity)
                print("Sweet added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            id = input("Enter sweet ID to delete: ")
            try:
                shop.delete_sweet(id)
                print("Sweet deleted successfully.")
            except KeyError:
                print("Sweet not found.")

        elif choice == '3':
            print("\n--- Available Sweets ---")
            sweets = shop.view_sweets()
            for sweet in sweets:
                print(sweet)

        elif choice == '4':
            name = input("Search by name (press Enter to skip): ") or None
            category = input("Search by category (press Enter to skip): ") or None
            min_price = input("Minimum price (press Enter to skip): ")
            max_price = input("Maximum price (press Enter to skip): ")
            min_price = float(min_price) if min_price else None
            max_price = float(max_price) if max_price else None
            results = shop.search_sweets(name, category, min_price, max_price)
            print(f"\nFound {len(results)} sweet(s):")
            for r in results:
                print(r)

        elif choice == '5':
            key = input("Sort by (name/price/quantity): ")
            sorted_list = shop.sort_sweets(key)
            for sweet in sorted_list:
                print(sweet)

        elif choice == '6':
            id = input("Enter sweet ID to purchase: ")
            qty = int(input("Enter quantity: "))
            try:
                shop.purchase_sweet(id, qty)
                print("Purchase successful.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '7':
            id = input("Enter sweet ID to restock: ")
            qty = int(input("Enter quantity: "))
            try:
                shop.restock_sweet(id, qty)
                print("Restocked successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '8':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
