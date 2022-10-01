personal_data_dict = {}
while True:
    key_name = input("What what data do you want to save?, eg: name, lastname: ")
    value= input("Please enter the data value: ")
    personal_data_dict[key_name]= value

    for key, value in personal_data_dict.items():
        print(f"Your {key} is {value}")
    
    if input("Do you want to exit: \nY-Yes\nN-No\n->") == "Y":
        break