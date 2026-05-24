# Username Recon Tool
Ferramenta que busca usernames automaticamente, verifica se o username existe em várias plataformas ao mesmo tempo.

## Sobre
Sabe quando você quer saber se alguém usa o mesmo username em vários sites? Essa ferramenta faz isso automaticamente, em vez de abrir cada site na mão, ela verifica tudo de uma vez e te diz onde encontrou.

Criei isso por curiosidade mesmo, depois de começar a estudar como reconhecimento funciona na prática.

## Como usar?
```bash
python3 username_recon_tool.py
```
Roda o script, digita o username e ele vai verificando plataforma por plataforma.
Digite o username do alvo que gostaria de localizar e em quais sites.

## Por que usar essa ferramenta?
Ela é extremamente útil para verificar se o nickname que você deseja utilizar em determinada plataforma já existe, além do que permite alteração para outro site, se você assim preferir, tal como Instagram e outros. Ela permite também o reconhecimento de "alvos", como buscar o nickname do seu alvo em diversos sites de forma automática e eficiente, economizando horas de busca ou scrapping manual. 

## O que eu aprendi construindo a ferramenta?
O status HTTP não é apenas backend, e sim informação. O "200", por exemplo, significa que tal user existe em determinada página, o "404" significa que não existe e o "301" que o site está redirecionando, ou seja, cada número tem de fato uma história. Entendi também que sites dificultam scraping de formas diferentes, e "contornar" isso me deu uma satisfação enorme. 

## Contexto
Esse projeto se deu, na verdade, porque também estava cansado de sempre tentar criar uma conta e aparecer a famosa mensagem "The username already exists". 

Estou aprendendo cibersegurança e programação de forma autônoma, construindo ferramentas e programando elas desde o zero para fixar os conceitos, claro que tenho muito o que aprender, afinal, faço as coisas na hora que dá, pois trabalho o dia inteiro em logística, chego em casa e tento aprimorar meus conhecimentos de forma autônoma (o código está em constante evolução, e, a cada atualização trago o que aprendi de novo).

Tenho 23 anos, trabalho até às 22:00hrs de segunda a sábado e aprendo cibersegurança e programação de noite, essa é minha história!
