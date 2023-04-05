"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""



def pregunta_01():
    x = open ('data.csv','r').readlines()
    x= [z.split('\t') for z in x]
    columna1 = [int(z[1]) for z in x]
    suma = sum(columna1)
    return suma 


def pregunta_02():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna0 = [z[0] for z in x]
    letras_unicas = sorted(list(set(columna0)))
    contar = [(letra,columna0.count(letra)) for letra in letras_unicas]
    return contar


def pregunta_03():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna0= [z[0] for z in x]
    columna1 = [z[1] for z in x]
    columna1= [int(numero) for numero in columna1]
    suma_letra = {}
    for letra,valor in zip(columna0, columna1):
        if letra in suma_letra:
            suma_letra[letra] += valor
        else:
           suma_letra[letra] = valor
    rpta = list(sorted(suma_letra.items()))
    return rpta


def pregunta_04():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna2 = [z[2] for z in x]
    mes = [t.split('-')[1] for t in columna2]
    #print(mes)
    dir= {}
    for n in mes:
        if n in dir:
            dir[n] +=1
        else:
            dir[n] = 1
    rpta= list(sorted(dir.items()))
    return rpta

def pregunta_05():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna0= [z[0] for z in x]
    columna1 = [z[1] for z in x]
    columna1 = [int(numero) for numero in columna1]
    diccionario = {}
    for letra,valor in zip(columna0, columna1):
        if letra in diccionario:
            diccionario[letra].append(valor)
        else:
            diccionario[letra] = [valor]
    max_min = []
    for letra,valor in diccionario.items():
        maximo= max(valor)
        minimo= min(valor)
        max_min.append((letra, maximo, minimo))
    rpta = sorted(max_min)
    return rpta


def pregunta_06():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna4= [z[4] for z in x]
    columna4= [z.replace('\n', '') for z in columna4]
    columna4= [z.split(',') for z in columna4]
    diccionario = {}
    for z in columna4:
        for i in z:
            clave, valor = i.split(':')
            if clave not in diccionario:
                diccionario[clave] = [int(valor)]
            else:
                diccionario[clave].append(int(valor))
    resultado = []
    for clave in diccionario:
        valores= diccionario[clave]
        maximo= max(valores)
        minimo= min(valores)
        resultado.append([clave, minimo, maximo])
    rpta = sorted(resultado)
    rpta = list(map(tuple, rpta))
    return rpta
    

def pregunta_07():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna0 = [z[0] for z in x]
    columna1 = [int(z[1]) for z in x]

    letras_numero = {}
    for num,let in zip(columna1, columna0):
        if num in letras_numero:
            letras_numero[num].append(let)
        else:
            letras_numero[num] = [let]

    letras_numero = sorted(letras_numero.items(), key= lambda x: x[0])
    return letras_numero


def pregunta_08():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna0 = [z[0] for z in x]
    columna1 = [int(z[1]) for z in x]

    letras_numero = {}
    for num,let in zip(columna1, columna0):
        if num in letras_numero:
            letras_numero[num].append(let)
        else:
            letras_numero[num] = [let]
    letras_numero = sorted(letras_numero.items(), key= lambda x: x[0])

    letras_unicas = []
    for z in letras_numero:
        unico= list(set(z[1]))
        ordenado = sorted(unico)
        nuevo = (z[0], ordenado)
        letras_unicas.append(nuevo)
    
    return letras_unicas

def pregunta_09():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna4 = [z[4] for z in x]
    columna4= [z.replace('\n', '') for z in columna4]
    columna4= [z.split(',') for z in columna4]
    lista =[]
    for z in columna4:
        lista.extend(z)
    diccionario = {}
    for elemento in lista:
        clave,valor = elemento.split(':')
        if clave in diccionario:
            diccionario[clave] += 1
        else:
            diccionario[clave] = 1
    rpta = dict(sorted(diccionario.items()))
    return rpta


def pregunta_10():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna0 = [z[0] for z in x]
    columna3 = [z[3] for z in x]
    columna4 = [z[4] for z in x]
    columna4= [z.replace('\n', '') for z in columna4]
    cant_columna3 = []
    cant_columna4 = []
    tuplas = []

    for letra in columna3:
        cant_columna3.append(len(letra.split(',')))
    for dato in columna4:
        cant_columna4.append(len(dato.split(',')))
    for z in range(len(columna0)):
        tuplas.append((columna0[z],cant_columna3[z],cant_columna4[z]))
    return tuplas


def pregunta_11():
    x = open ('data.csv','r').readlines()
    x = [z.split('\t') for z in x]
    columna1 = [int(z[1]) for z in x]
    columna3 = [z[3] for z in x]
    columna3 = [z.split(',') for z in columna3]
    diccionario = {}
    for i in range(len(columna3)):
        for j in range(len(columna3[i])):
            letra= columna3[i][j]
            suma= columna1[i]
            if letra not in diccionario:
                diccionario[letra] = suma
            else:
                diccionario[letra] += suma  
    rpta = dict(sorted(diccionario.items()))
    return rpta


def pregunta_12():
    x = open ('data.csv','r').readlines()
    x = [z.replace('\n','') for z in x]
    x = [z.split("\t") for z in x]
    columna0 = [z[0] for z in x]
    columna4 = [z[4] for z in x]
    columna4 = [z.split(',') for z in columna4]
    letras = []
    lista_2 = []
    lista_3 = []
    diccionario = {}
    diccionario_total = {}
    for i in columna0:
        if i not in letras:
            letras.append(i)
    for i in columna4:
        diccionario = {}
        for z in i:
            clave,valor = z.split(':')
            if clave not in diccionario:
                diccionario[clave] = int(valor)
            else:
                diccionario[clave].append(int(valor))
        lista = list(diccionario.values())
        lista_2.append(sum(lista))

    for z in range(len(letras)):
        listan = []
        for letra,num in zip(columna0,lista_2):
            if letra == letras[z]:
                listan.append(int(num))
        lista_3.append(sum(listan))

    diccionario_total_1 = dict(zip(letras,lista_3))
    lista_diccionario_total = sorted(diccionario_total_1.items())

    for key,valor in lista_diccionario_total:
        diccionario_total[key] = valor
    return diccionario_total
