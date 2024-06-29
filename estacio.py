vagas_livre = []
estacionamento_carros = 0
N = int(input("digite o numero de vagas: "))
if 1 > N < 100000:
    print('Valor muito acima ou abaixo do permitido!')
    N = int(input("digite o numero de vagas: "))
M = int(input("digite quantos clientes estão esperando: "))
if 1 > M < 100000:
    print('Valor muito acima ou abaixo do permitido!')
    M = int(input("digite quantos clientes estão esperando: "))
for c in range(M):
    V_i = int(input("digite sua posição: "))
    while V_i > N or V_i < 1:
        print("Nao Existe essa vaga!")
        V_i = int(input("digite sua posição: "))
    if V_i in vagas_livre:
        while V_i in vagas_livre:
            V_i -=1
        vagas_livre.append(V_i)
        estacionamento_carros += 1
        if V_i == 0:
                del(vagas_livre[c])
                estacionamento_carros -= 1
                print(f"Carros que estão estacionados: {estacionamento_carros}")
                exit()
                print()
    else:
        vagas_livre.append(V_i)
        estacionamento_carros += 1
print(f"Carros que estão estacionados: {estacionamento_carros}")