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
    print(valorFinal)
Conversor(valorAConverter,unidadeConvertida,unidadeDesejada)












