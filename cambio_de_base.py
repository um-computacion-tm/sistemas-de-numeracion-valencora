import unittest

def decimal2binario(numero):
    resultado = ""
    while numero > 2:
        resto = numero % 2
        if resto == 0:
            resultado = "0" + resultado
        else:
            resultado = "1" +resultado
        numero = numero // 2
        if numero == 2:
            resultado = "1" +"0" + resultado
    return resultado

def binario2decimal(numero):
    numero = numero[::-1]
    result = 0
    for i in range(len(numero)):
        result += (int(numero[i]) * 2**i)
    return result

def decimal2octal(numero):
    result = ""
    while numero >= 8:
        resto = numero % 8
        numero = numero // 8
        result = str(resto) + result

    result = str(numero) + result
    return result

def octal2decimal(numero):
    numero = numero[::-1]
    result = 0
    for i in range(len(numero)):
        result += (int(numero[i]) * 8**i)
    return result

def decimal2hexa(numero):
    result = ""
    while numero >= 16:
        resto = str(numero % 16)
        numero = numero // 16 
        result = switch(resto) + result
          
    result = switch(str(numero)) + result
    return result
    

def switch(resto):
    if resto == "10":
        resto = "A" 
    elif resto == "11":
        resto = "B" 
    elif resto == "12":
        resto = "C"
    elif resto == "13":
        resto = "D" 
    elif resto == "14":
        resto = "E"
    elif resto == "15":
        resto = "F"
    return resto

def hexa2decimal(numero):
    numero = numero[::-1]
    result = 0
    for i in range(len(numero)):
        if numero[i] == "A":
            result += (10 * 16**i)
        elif numero[i] == "B":
            result += (11 * 16**i)
        elif numero[i] == "C":
            result += (12 * 16**i)
        elif numero[i] == "D":
            result += (13 * 16**i)
        elif numero[i] == "E":
            result += (14 * 16**i)
        elif numero[i] == "F":
            result += (15 * 16**i)
        else:
            result += (int(numero[i]) * 16**i)
    return result

def binario2octal(numero):
    aux = binario2decimal(numero)
    aux2 = decimal2octal(aux)
    return int(aux2)

def binario2hexa(numero):
    aux = binario2decimal(numero)
    aux2 = decimal2hexa(aux)
    return aux2

def octal2binario(numero):
    aux = octal2decimal(str(numero))
    aux2 = decimal2binario(aux)
    return aux2 

def octal2hexa(numero):
    aux = octal2decimal(str(numero))
    aux2 = decimal2hexa(aux)
    return aux2 

def hexa2binario(numero):
    aux = hexa2decimal(str(numero))
    aux2 = decimal2binario(aux)
    return aux2 

def hexa2octal(numero):
    aux = hexa2decimal(numero)
    aux2 = decimal2octal(aux)
    return aux2


if __name__=="__main__":
    unittest.main()