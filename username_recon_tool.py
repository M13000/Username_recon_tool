import requests

plataformas = {
    "Github": "https://github.com/{}",
    "Reddit": "https://reddit.com/user/{}",
    "Twitter": "https://twitter.com/{}",
}

username = input("Digite um username: ")

for nome, url in plataformas.items():
    url = url.format(username)
    response = requests.get(url, allow_redirects=True)
    
    if response.status_code == 200:
        print(f"[+] {nome}: Encontrado: {url}")
    
    elif response.status_code == 404:
        print(f"[-] {nome}: Perfil não encontrado: {url}")
    
    else:
        print(f"[?] {nome}: Status inesperado: {response.status_code}")
