def print_welcome():
    print("*** Welcome ***")

def get_option(studies):
    for key,value in studies.items():
        for key_interno, value_interno in value.items():
            print(f"{key} - {value_interno}", end = "")
        print("")
    return input("Please enter a option: ")

def get_client_data(study):
    client = {
        "id":input("Please enter the client id: "),
        "age":input("Please enter the client age M or F: "),
        "gender":input("Please enter the client gender: "),
        "study": study
    }
    return client
    
def get_discounts(client, studies,client_number):
    discount = 0
    if client.get("gender") == "F" and int(client.get("age")) > 55:
        discount += studies.get(client.get("study")).get("price") * 0.25
    elif client.get("gender") == "M" and int(client.get("age")) > 65:
        discount += studies.get(client.get("study")).get("price") * 0.25
    
    if client_number % 2 != 0:
        discount += studies.get(client.get("study")).get("price") * 0.02

    return discount

def get_net_amount(client, discount, studies):
    return studies.get(client.get("study")).get("price") - discount


def print_invoice(client, studies, net_amount):
    print('*** RECEIPT ***')
    print("Id card:",client.get("id"))
    print("Age:",client.get("age"))
    print("Gender:",client.get("gender"))
    print("Study:",studies.get(client.get("study")).get("description"))
    client["total"] = net_amount
    print("Net Amout:",net_amount)


def main():
    studies_dict = {
        "U": {
            "description":"Ultrasonido",
            "price": 8900
        },
        "T": {
            "description":"Tomografia",
            "price": 12640
        },
        "R": {
            "description":"Resonancia",
            "price": 15600
        }
    }
    clients = []
    total_discounts = 0
    total_net_amount = 0
    total_net_amountU = 0
    total_net_amountR = 0
    total_net_amountT = 0
    print_welcome()
    while True:
        option=get_option(studies_dict)
        client = get_client_data(option)
        clients.append(client)
        discount = get_discounts(client,studies_dict,len(clients))
        total_discounts += discount
        total = get_net_amount(client,discount,studies_dict)
        total_net_amount += total
        print_invoice(client, studies_dict, total)
        print(client)
        if input("Do you want to continue Y-Yes or N-No") == "Y":
            break
    #print_final_day(clients)

main()