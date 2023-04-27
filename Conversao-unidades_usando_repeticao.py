unidades = ["bit", "byte", "KB", "MB", "GB", "TB", "PB"]

valorAConverter=int(input('Insira o valor a ser convertido: '))

unidadeConvertida=input('Insira a unidade de medida a ser convertida: ')
while not unidadeConvertida in unidades:
    unidadeConvertida=input('Insira a unidade de medida a ser convertida: ')
unidadeDesejada=input('Insira a unidade desejada: ')
while not unidadeDesejada in unidades:
    unidadeDesejada=input('Insira a unidade desejada: ')

def Conversor (valorAConverter,unidadeConvertida,unidadeDesejada,):
    valorFinal = valorAConverter
    if unidadeConvertida=='bit':
        valorFinal=valorFinal/8
        unidadeConvertida='byte'
    if unidades.index(unidadeConvertida)<unidades.index(unidadeDesejada):
        for distancia in range(unidades.index(unidadeConvertida),unidades.index(unidadeDesejada)):
            valorFinal=valorFinal/1024
    else:
        for distancia in range(unidades.index(unidadeConvertida),unidades.index(unidadeDesejada),-1):
            valorFinal=valorFinal*1024
        if unidadeDesejada=='bit':
            valorFinal=(valorFinal/1024)*8
        
    print(valorFinal)
Conversor(valorAConverter,unidadeConvertida,unidadeDesejada)














# def converter(quantidade, unidade_origem, unidade_destino):
#     indice_origem = unidades.index(unidade_origem)
#     indice_destino = unidades.index(unidade_destino)

#     if indice_origem > indice_destino:
#         quantidade = converter(quantidade, unidade_origem, unidades[indice_destino + 1])
#         indice_origem = indice_destino + 1

#     fator = 1024 ** (indice_destino - indice_origem)

#     return quantidade * fator

# def conversao_multipla(quantidade, unidade_origem, unidade_destino):
#     if unidades.index(unidade_destino) < unidades.index(unidade_origem):
#         unidade_origem, unidade_destino = unidade_destino, unidade_origem
#     resultado = quantidade
#     while unidade_origem != unidade_destino:
#         proxima_unidade = unidades[unidades.index(unidade_origem) + 1]
#         resultado = converter(resultado, unidade_origem, proxima_unidade)
#         unidade_origem = proxima_unidade
#     return resultado
# print("Insira o valor a ser convertido, em seguida a unidade desejada e por ultimo a unidade a ser convertida:")

# result=conversao_multipla(int(input()), input(), input())

# print(result)