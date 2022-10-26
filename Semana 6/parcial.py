def is_primo(rif):
    number = int(rif[-1])
    aux = number - 1
    while aux > 1:
        if number% aux ==0:
            return False
        aux -=1
    return True 

def main():
    products = {
            "F": {
                "description":"Farmacéutico",
                "price": 2500
            },
            "Q": {
                "description":"Químico",
                "price": 1000
            },
            "B": {
                "description":"Biológicos",
                "price": 4000
            }
        }
    client_f = 0
    client_q = 0
    client_b = 0
    discount_f = 0
    discount_q = 0
    discount_b = 0
    max_purchase = 0
    rif_max_purchase =0 
    total_day = 0
    while True:
        rif = input("Please enter your rif: ")
        product_code = input("Please enter the product Code \nF - Farmacéutico\n Q-Químico\nB-Biológicos\n-->")
        payment_method = input("Please enter your payment method \nC- One Time\n R - Credit\n-->")
        gross_amount = products.get(product_code).get("price")
        discount = 0
        recharge = 0
        tax = 0
        # Discounts
        if payment_method == "C":
            discount += gross_amount * 0.03
        elif payment_method == "R":
            recharge += gross_amount * 0.1 
        if gross_amount %2 == 0:
            discount += gross_amount * 0.02
        if is_primo(rif):
            discount += gross_amount * 0.05

        #Taxes
        if product_code != "F":
            tax += gross_amount * 0.12

        #Total
        total = gross_amount + recharge - discount + tax

        # End of day data   
        total_day += total
        if product_code == "F":
            client_f +=1
            discount_f += discount
        elif product_code == "Q":
            client_q +=1
            discount_q += discount
        elif product_code == "B":
            client_b +=1
            discount_b += discount
        
        if total > max_purchase:
            rif_max_purchase = rif
            max_purchase = total

        #Factura
        print("**** RECEIPT ****")
        print("RIF", rif)
        print("Product",products.get(product_code).get("description"))
        print("Payent Method:",payment_method)
        print("Discount:",discount)
        print("Tax:",tax)
        print("Total:",total)
        if input("Do you want to continue Y-Yes or N-No") == "Y":
            break
    print("**** END OF DAY ****")
    print("Client F:",client_f)
    print("Client Q:",client_q)
    print("Client B:",client_b)
    print("Discounts F:",discount_f)
    print("Discounts Q:",discount_q)
    print("Discounts B:",discount_b)
    print("Rif Maximum Purchase",rif_max_purchase)
    print("Total:",total_day)





main()