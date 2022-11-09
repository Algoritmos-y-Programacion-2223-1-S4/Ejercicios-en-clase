import requests

def main():
    #url = "http://httpbin.org/get?nombre=Maria&curso=Algoritmos&horas=4"
    url = "http://httpbin.org/get"
    args = { "nombre" : "Maria", "curso" : "Algoritmos", "horas": "4"}
    response = requests.get(url=url, params= args)
    print(response)

    if response.status_code == 200:
        content = response.content
        print(content.decode())
        

main()