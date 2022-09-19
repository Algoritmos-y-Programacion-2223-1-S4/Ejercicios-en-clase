option = int(input("Please enter a valid option: \n1- Vegetarian\n2- Non Vegetarian\n->"))
if option == 1:
    ingredient = input("Please enter the ingredient that you want: \n1- Pimiento\n2-Tofu\n->")
    if ingredient == "1":
        ingredient = "Pimiento"
    else:
        ingredient = "Tofu"
    print(f"The pizza is vegetarian and have these ingridients Tomato,Mozarella and {ingredient}")

elif option == 2:
    ingredient = input("Please enter the ingredient that you want: \n1- Pepperoni\n2-Jamon\n3-Salmon\n->")
    if ingredient == "1":
        ingredient = "Pepperoni"
    elif ingredient == "2":
        ingredient = "Jamon"
    else:
        ingredient = "Salmon"
    print(f"The pizza is non vegetarian and have these ingridients Tomato,Mozarella and {ingredient}")
    
else:
    print("Invalid option")
