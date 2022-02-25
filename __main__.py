# Este é o arquivo o principal
# "index.html"
# Aqui eu vou chamar o  pet_shop ("css") e o terreno ("javascript")

#Como fazer importação do código para fazer chamada.
from pet_shop import calcula_nota, pet_shop


print("main funcinando\n")

## 1 inserindo dados na classe petshop

nome_do_pet=input("Qual o nome do pet? \n")
nome_do_dono=input("Qual o seu nome? \n")
raca_do_pet=input("Qual e raça do seu pet? \n")
tamanho_do_pet=input("Qual é o tamanho de seu pet? \n")

# criando variável que vai herdar as características da classe pet_shop
objeto_pet=pet_shop()

objeto_pet.nome_dono=nome_do_dono
objeto_pet.nome_pet=nome_do_pet
objeto_pet.raca_pet=raca_do_pet
objeto_pet.tamanho_pet=tamanho_do_pet

print("Nome do pet: ", objeto_pet.nome_dono)
print("Nome do dono: ", objeto_pet.nome_pet)
print("Raca do pet: ", objeto_pet.raca_pet)
print("tamanho do pet:", objeto_pet.tamanho_pet)

print("main funcinando\n")

Nota_1=input("Qual é sua primeira nota? \n")
Nota_2=input("Qual é a sua segunda nota? \n")
Nota_3=input("Qual é a sua terceira nota? \n")
Nota_4=input("Qual é a sua Quarta nota? \n")

objeto_nota=calcula_nota()

objeto_nota.Nota_1=Nota_1
objeto_nota.Nota_2=Nota_2
objeto_nota.Nota_3=Nota_3
objeto_nota.Nota_4=Nota_4


print("Nota 1:", objeto_nota.Nota_1)
print("Nota 2:", objeto_nota.Nota_2)
print("Nota 3:", objeto_nota.Nota_3)
print("Nota 4:", objeto_nota.Nota_4)


