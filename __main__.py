# Este é o arquivo o principal
# "index.html"
# Aqui eu vou chamar o  pet_shop ("css") e o terreno ("javascript")

#Como fazer importação do código para fazer chamada.
from pet_shop import pet_shop

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
print("Raca do pet: ", objeto_pet.raca_petbo)
print("tamanho do pet:", objeto_pet.tamanho_pet)