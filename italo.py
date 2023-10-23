#Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
datnascimento = int(input("Digite o ano em que você nasceu: "))
anoatual = int(input("Digite o ano atual: "))
idade = anoatual - datnascimento
if idade < 18:
    print("Ainda não é a hora certa para se alistar no serviço militar!")
    print("Ainda falta(m)", 18 - idade, "ano(s) até você estar pronto!")
elif idade >= 18:
    print("Já está na hora de você se alistar no serviço militar!")
    if idade > 18:
        print("Já faz(em)", idade - 18, "ano(s) que você está pronto!")
        