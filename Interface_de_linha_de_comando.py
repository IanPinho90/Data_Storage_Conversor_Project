from Calculadora_Unidades_Armazenamento import converterStringParaFloat, bitParaByte, byteParaBit

print(' -Escreva 1 para bit para byte \n -Escreva 2 para byte para bit \n -Escreva 3 para KB para B \n -Escreva 4 para B para KB \n -Escreva 5 para MB para KB \n -Escreva 6 para KB para MB')
funcEscolha = input()
if(funcEscolha == '1'):
    print('vc escolheu 1, indique o valor a ser alterado:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    print('vc escolheu 2 indique o valor a ser alterado:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)