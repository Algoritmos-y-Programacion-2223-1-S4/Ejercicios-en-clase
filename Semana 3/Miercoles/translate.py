translate_dict = {}
translate_input = input("Please enter the dictionary in this format <palabra>:<traducción> and divided by commas: ")
translations_list = translate_input.split(",")
#['Hola:Hello', 'Adios:Bye']
for translation in translations_list:
    list_of_values = translation.split(":")
    #['Hola','Hello'] 
    #['Adios','Bye'] 
    translate_key = list_of_values[0]
    translate_value = list_of_values[1]
    translate_dict[translate_key] = translate_value
print(translate_dict)