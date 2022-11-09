import requests

def main():
    url = "http://httpbin.org/get"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        content = response.content
        print(content.decode())
        

main()