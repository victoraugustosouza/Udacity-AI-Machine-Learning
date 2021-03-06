# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
data_list=[]
with open("chicago.csv", "r") as file_read:
    for row in csv.DictReader(file_read): #DictReader rotorna um iterable das linhas, mapeados para dicionarios ordenado.
        data_list.append(row)

print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for entrada in range(0,20):
    print("Linha {}:\n".format(entrada+1))
    for key in data_list[entrada].keys(): #Usar a lista de chaves para imprimir todos os pares chaves:valores.
        print("{}:{}".format(key,data_list[entrada][str(key)]))
    print('\n')
# Vamos mudar o data_list para remover o cabeçalho dele.
#data_list = data_list[1:] desnecessário

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for entrada in range(0,20):
    print("Linha {}:".format(entrada+1))
    if(data_list[entrada]['Gender']):
        print("Gender:{}\n".format(data_list[entrada]['Gender']))
    else:
        print("Sem informação disponível\n")



# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """Coloca todos os valores de umca coluna em uma lista

    ENTRADA:
    data: todas as entradas(ou linhas) no formato lista de dicionarios
    index: especifica a coluna que se deseja pegar os valores

    SAÍDA:
    column_list: lista com todos os valores da coluna.
    """
    column_list = []
    column_name = []
    for key in data[0].keys():
        column_name.append(str(key))
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for i in range(len(data)):
            column_list.append(data[i][column_name[index]])

    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
gender_list = column_to_list(data_list, -2)
for genero in gender_list:
    if(genero == 'Male'):
        male+=1
    elif(genero =='Female'):
        female+=1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """Conta a quantidade de cada gênero.

    ENTRADA:
    data_list: todas as entradas(ou linhas) no formato lista de dicionarios

    SAÍDA:
    [male,female]: lista com dois items,o primeiro sendo a quantidade de homens e
    o segundo a quantidade de mulheres.

    """
    male = 0
    female = 0
    for registro in range(len(data_list)):
            if(data_list[registro]['Gender'] == 'Male'):
                male+=1
            elif(data_list[registro]['Gender'] == 'Female'):
                female+=1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """Calcula o gênero mais popular

    ENTRADA:
    data_list: todas as entradas(ou linhas) no formato lista de dicionarios

    SAÍDA:
    answer: string contendo o gênero mais popular ou 'equal' se os gêneros são
    igualmente populares.

    """
    totais = count_gender(data_list)
    if totais[0] > totais[1]:
        answer = 'Male'
    elif(totais[0] < totais[1]):
        answer = 'Female'
    else:
        answer = 'Equal'

    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
quantity=[]
user_list = column_to_list(data_list, -3)
types = ["Subscriber", "Customer","Dependent"]
quantity.append(user_list.count('Subscriber'))
quantity.append(user_list.count('Customer'))
quantity.append(user_list.count('Dependent'))
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

print("\nTAREFA 7: Verifique o gráfico!")


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = """\nO somatorio do número de usuarios homens com o número de usuários mulheres é menor que o total de
usuários. Isso ocorre porque alguns usuários estão sem essa informação na base de dados, possivelmente
os usuários optaram por não informar"""
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

trip_duration_list = column_to_list(data_list, 2)
min_trip =float(trip_duration_list[0])
max_trip = float(trip_duration_list[0])
soma=0.0
for tempo_viagem in trip_duration_list:
    tempo_viagem = float(tempo_viagem)
    if tempo_viagem < min_trip:
        min_trip = tempo_viagem
    if tempo_viagem > max_trip:
        max_trip = tempo_viagem
    soma+=tempo_viagem

mean_trip = soma/len(trip_duration_list)

lista_int =list(map(int,trip_duration_list)) #retorna uma cópia com itens da list com tipo int
lista_ordenada=sorted(lista_int)

if(~len(lista_ordenada)%2): #se numero de usuarios é par entra no if
    temp = int(len(lista_ordenada)/2)
    median_trip = (float(lista_ordenada[temp]) + float(lista_ordenada[temp-1]))/2

else: #se é impar entra no else
    temp = int((len(lista_ordenada) + 1)/2) #calculo do indice da mediana caso a lista/indice se iniciasse em um
    median_trip = float(lista_ordenada[temp-1]) #como se inicia em zero é necessário diminuir o indice em 1

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set()
for station in column_to_list(data_list, 3):
    start_stations.add(station)


print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:


input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """Conta os tipos de usuários ou outra categotia de dados

    ENTRADA:
    column_list: lista de todas as entradas em uma determinada coluna

    SAÍDA:
    item_types: tipos de usuários diferentes
    count_items: quantidade de cada tipo de usuário
    """
    item_types = []
    count_items = []

    for item in column_list:
        if item not in item_types:
            item_types.append(item)
            count_items.append(int(0))
        index_in_items = item_types.index(item)
        count_items[index_in_items]+=1

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
