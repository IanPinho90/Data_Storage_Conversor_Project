ValorComumByteBit=8
ValorComumByte=1024

def converterStringParaFloat(value):
    ('Valor convertido de str para float')
    return float(value)

# bit-Byte byte-Bit

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / ValorComumByteBit
    print(bytesCalculado)
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * ValorComumByteBit
    print(bitsCalculado)
    return bitsCalculado

# KB-Byte byte-KB

def kilobyteParaByte(valorASerConvertido):
    print('Valor convertido de kilobyte para byte')
    byteCalculado = valorASerConvertido * ValorComumByte
    print(byteCalculado)
    return byteCalculado

def byteParaKilobyte(valorASerConvertido):
    print('Valor convertido de byte para kilobyte')
    kilobyteCalculado = valorASerConvertido / ValorComumByte
    print(kilobyteCalculado)
    return kilobyteCalculado

# MB-KB KB-MB

def MBParaKB(valorASerConvertido):
    print('Valor convertido de MB para KB')
    KBCalculado = valorASerConvertido * ValorComumByte
    print(KBCalculado)
    return KBCalculado

def KBParaMB(valorASerConvertido):
    print('Valor convertido de KB para MB')
    MBCalculado = valorASerConvertido / ValorComumByte
    print(MBCalculado)
    return MBCalculado

# GB-MB MB-GB

def GBParaMB(valorASerConvertido):
    print('Valor convertido de GB para MB')
    MBCalculado = valorASerConvertido * ValorComumByte
    print(MBCalculado)
    return MBCalculado

def MBParaGB(valorASerConvertido):
    print('Valor convertido de MB para GB')
    GBCalculado = valorASerConvertido / ValorComumByte
    print(GBCalculado)
    return GBCalculado

# TB-GB GB-TB

def TBParaGB(valorASerConvertido):
    print('Valor convertido de TB para GB')
    GBCalculado = valorASerConvertido * ValorComumByte
    print(GBCalculado)
    return GBCalculado

def GBParaTB(valorASerConvertido):
    print('Valor convertido de GB para TB')
    TBCalculado = valorASerConvertido / ValorComumByte
    print(TBCalculado)
    return TBCalculado

# PB-TB TB-PB

def PBParaTB(valorASerConvertido):
    print('Valor convertido de PB para TB')
    TBCalculado = valorASerConvertido * ValorComumByte
    print(TBCalculado)
    return TBCalculado

def TBParaPB(valorASerConvertido):
    print('Valor convertido de TB para PB')
    PBCalculado = valorASerConvertido / ValorComumByte
    print(PBCalculado)
    return PBCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
byteParaBit(entradaDoTecladoValorASerConvertido)
bitParaByte(entradaDoTecladoValorASerConvertido)
kilobyteParaByte(entradaDoTecladoValorASerConvertido)
byteParaKilobyte(entradaDoTecladoValorASerConvertido)
MBParaKB(entradaDoTecladoValorASerConvertido)
KBParaMB(entradaDoTecladoValorASerConvertido)
GBParaMB(entradaDoTecladoValorASerConvertido)
MBParaGB(entradaDoTecladoValorASerConvertido)
TBParaGB(entradaDoTecladoValorASerConvertido)
GBParaTB(entradaDoTecladoValorASerConvertido)
PBParaTB(entradaDoTecladoValorASerConvertido)
TBParaPB(entradaDoTecladoValorASerConvertido)