import requests
import json

def main():
    url = "http://httpbin.org/get"
    args = { "nombre" : "Antonio", "curso" : "Algoritmos"}
    headers = { "Content-Type" : "application/json" }
    response = requests.get(url, params= args, headers= headers)
    print(response)

    if response.status_code == 200:
        # FORMA 1
        response_json = response.json()
        print(response_json)
        print(response_json.get("origin"))
        Response

main()