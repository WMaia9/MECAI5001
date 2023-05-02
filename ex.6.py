valor = int(input())

cedulas = [100, 50, 10, 5, 1]  # lista com as cédulas disponíveis
qtd_cedulas = [0, 0, 0, 0, 0]  # lista para armazenar a quantidade de cada cédula

for i in range(len(cedulas)):
    qtd_cedulas[i] = valor // cedulas[i]  # divide o valor pelas cédulas para obter a quantidade
    valor = valor % cedulas[i]  # calcula o resto da divisão para usar na próxima iteração

print(f"Valor lido: R${valor:.2f}")
for i in range(len(cedulas)):
    print(f"{qtd_cedulas[i]} de R${cedulas[i]:.2f}")
