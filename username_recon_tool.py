import requests

username=(input("Digite o username: "))
sites= {
    "Steam": "https://steamcommunity.com/id/{}",
    "Github": "https://github.com/{}"
   
}


for nome, url in sites.items():
    url = url.format(username)
    response = requests.get(url)
    response.status_code
    if response.status_code==200 and "Error" not in response.text:
        print(f"[+] {nome}: encontrado!")
    elif response.status_code==404:
        print(f"[-] {nome}: não encontrado!")
    else:
        print(f"[-] {nome}: não encontrado! ")   