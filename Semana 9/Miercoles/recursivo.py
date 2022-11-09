def exponential(base, exp):
    if exp == 0:
        return 1
    return base * exponential(base,exp-1)

def search_in_list(lista,letter,index = 0):
    if letter == lista[index]:
        return letter
    else:
        if index == len(lista)-1:
            if letter == lista[index]:
                return letter
            else: 
                return None
        return search_in_list(lista,letter,index+1)

def invert_word(word,index):
    if index == 0:
        return word[index]
    return word[index] + invert_word(word, index-1)

def fibo(max_num,num1= 0,num2=1):
    print(num1, end= " ")
    if num2 > max_num:
        return num2
    return fibo(max_num,num2,num1+num2)
    

def main():
    option = int(input("Please enter a option: \n 1- Exponential \n 2- Search in list \n 3- Invert word \n 4- Fibonacci\n -->"))
    if option == 1:
        print(exponential(int(input("Please enter the base: ")),int(input("Please enter the exponent: ")) ))
    elif option == 2:
        lista = ["A","B","C","D","E","F","G","H","I","J"]
        letter = input("Please enter a letter to search: ")
        print(search_in_list(lista,letter))
    elif option == 3:
        word = input("Please enter a word to invert: ")
        print(invert_word(word,len(word)-1))
    elif option == 4:
        max_num = int(input("Please enter the maximum number: "))
        fibo(max_num)
    else: 
        print("Invalid Option")

main()