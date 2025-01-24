try:
    nome = int(input("Olá, qual a sua idade? \n"))
    print (f"Sua idade é: {nome}.")
except ValueError:
    print("Somente números são aceitos. Tente novamente.")