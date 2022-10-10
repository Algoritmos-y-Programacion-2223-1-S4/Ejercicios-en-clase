def main():
    products = {
        "mobiles": {
            "Apple": [
                {
                    "id": 1,
                    "name": "iPhone 7",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "iPhone 8",
                    "price": 350
                },
                {
                    "id": 3,
                    "name": "iPhone Xr",
                    "price": 450
                },
                {
                    "id": 4,
                    "name": "iPhone Xs",
                    "price": 460
                },
                {
                    "id": 5,
                    "name": "iPhone 11",
                    "price": 900
                },
                {
                    "id": 6,
                    "name": "iPhone 12",
                    "price": 1100
                },
                {
                    "id": 7,
                    "name": "iPhone 13",
                    "price": 1300
                },
            ],
            "Samsung": [
                {
                    "id": 8,
                    "name": "Samsung Galaxy Beam",
                    "price": 150
                },
                {
                    "id": 9,
                    "name": "Samsung Galaxy S6",
                    "price": 200
                },
                {
                    "id": 10,
                    "name": "Samsung Galaxy S7",
                    "price": 300
                },
            ],
            "Xiaomi": [
                {
                    "id": 11,
                    "name": "Xiaomi Redmi Note 8",
                    "price": 250
                },
                {
                    "id": 12,
                    "name": "Xiaomi Redmi Note 8 Pro",
                    "price": 300
                },
            ]
        },
        "laptops": {
            "DELL": [
                {
                    "id": 13,
                    "name": "Dell Inspiron 15",
                    "price": 600
                },
                {
                    "id": 14,
                    "name": "Dell Latitude 14",
                    "price": 650
                },
            ],
            "MAC": [
                {
                    "id": 15,
                    "name": "MacBook Pro 13",
                    "price": 900
                },
                {
                    "id": 16,
                    "name": "MacBook M1",
                    "price": 1500
                },
            ]
        },
    }

    while True:
        option= int(input("\nPlease enter a valid \n1- Show Inventory\n2- Make a purchase\n3- Exit\n->"))
        if option == 1:
            categories= {1:"mobiles",2:"laptops"}
            category= int(input("Please enter a category: \n1-Mobiles\n2-Laptops\n->"))
            for types, brands in products.items():
                if types == categories.get(category):
                    for brand, list_of_products in brands.items():
                        print(brand)
                        for product in list_of_products:
                            id = product.get("id")
                            name = product.get("name")
                            price = product.get("price")
                            print(f"{id} - {name} - {price}")
        elif option == 2:
            product_id = int(input("Please enter the product id that you want: "))
            product_selected = None
            for types, brands in products.items():
                for brand, list_of_products in brands.items():
                    for product in list_of_products:
                        if product.get("id") == product_id:
                            product_selected = product
                            break
            
            if product_selected:
                client = {
                    "name":input("Please enter your name: "),
                    "id_card":input("Please enter your id card:"),
                    "product_id": product_id
                }
                print("***** RECEIPT ******")
                for key,value in client.items():
                    if key != "product_id":
                        print(key,value)
                for key,value in product_selected.items():
                    print(key,value)
            else: 
                print("Product not found")



        elif option == 3:
            break
        else:
            continue


main()