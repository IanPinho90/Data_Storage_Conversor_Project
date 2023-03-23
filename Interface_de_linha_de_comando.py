from Calculadora_Unidades_Armazenamento import converterStringParaFloat, bitParaByte, byteParaBit, kilobyteParaByte, byteParaKilobyte, MBParaKB, KBParaMB, GBParaMB, MBParaGB, TBParaGB, GBParaTB, PBParaTB, TBParaPB

print(' -Escreva 1 para bit para byte \n -Escreva 2 para byte para bit \n -Escreva 3 para KB para B \n -Escreva 4 para B para KB \n -Escreva 5 para MB para KB \n -Escreva 6 para KB para MB')
funcEscolha = input()
if(funcEscolha == '1'):
    print('vc escolheu 1, indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    print('vc escolheu 2 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '3'):
    print('vc escolheu 3 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = kilobyteParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '4'):
    print('vc escolheu 4 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaKilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '5'):
    print('vc escolheu 5 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MBParaKB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '6'):
    print('vc escolheu 6 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KBParaMB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '7'):
    print('vc escolheu 7 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GBParaMB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '8'):
    print('vc escolheu 8 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MBParaGB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '9'):
    print('vc escolheu 9 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TBParaGB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '10'):
    print('vc escolheu 10 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GBParaTB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '11'):
    print('vc escolheu 11 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = PBParaTB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '12'):
    print('vc escolheu 12 indique o valor a ser convertido:')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TBParaPB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)
