import requests
import json

def main():
    url = "http://httpbin.org/get"
    args = { "nombre" : "Antonio", "curso" : "Algoritmos"}
    response = requests.get(url, params= args)
    print(response)

    if response.status_code == 200:
        # FORMA 1
        """
        response_json = response.json()
        print(response_json)
        print(response_json.get("origin"))
        """
        

        # FORMA 2"
        response_json = json.loads(response.text)
        print(response_json)
        print(response_json.get("origin"))
      
        

main()