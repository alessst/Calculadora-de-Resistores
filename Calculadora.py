class Calculador_Resitores:

    tolerancia = 0

    # Retorna se o valor esta na tolerancia
    @staticmethod
    def tolerancia_calculo(resistor, valor, tolerancia):
        #Calculo de tolerancia:
        tolerancia_acima = (1+(tolerancia/100))
        tolerancia_abaixo = (1-(tolerancia/100))

        toleAcima = (resistor * tolerancia_acima)
        toleAbaixo = (resistor * tolerancia_abaixo)
        return (valor <= toleAcima) and (valor >= toleAbaixo)       


    #Calculo da associação em serie
    @staticmethod
    def serie_calculo(res1, res2):
        return res1 + res2


    #Calculo da associação em Paralelo
    @staticmethod
    def paralelo_calculo(res1, res2):
        return ((res1 * res2)/(res1 + res2))


    #Define a Unidade
    @staticmethod
    def unidade(valor):
        unidade = ""
        resto   = 0
        v       = valor
        if valor < 1000: 
            unidade = ""

        elif valor >= 1000 and valor < 1000000:
            v     = int(valor/1000)
            resto = int(valor%1000/100)
            unidade = "K"

        else:   
            v = int(valor/1000000)
            resto = int((valor%1000000)/100000)
            unidade = "M"

        res = str(v) + unidade

        if (resto != 0):
            res += str(resto)

        return res
    
    
    #Filtro valores a serem calculados
    def calculo_erro(valorCalc, valorAssociado):
        return abs(((valorAssociado/valorCalc)-1)*100)


'''
#Filtro valores a serem calculados
def calcErro(valorCalc, valorAssociado):
    return abs(((valorAssociado/valorCalc)-1)*100)

def estaTolerancia(resistor, valor):
    global toleranciaValor

    #Calculo de tolerancia:
    tolerancia_acima = (1+(toleranciaValor/100))
    tolerancia_abaixo = (1-(toleranciaValor/100))

    toleAcima = (resistor * tolerancia_acima)
    toleAbaixo = (resistor * tolerancia_abaixo)
    return (valor <= toleAcima) and (valor >= toleAbaixo)


#Calculo da associação em serie
def serieCalculo(res1, res2):
    return res1 + res2

#Calculo da associação em Paralelo
def paraleloCalculo(res1, res2):
    return ((res1 * res2)/(res1 + res2))

#Define a Unidade
def unidade(valor):
    unidade = ""
    resto   = 0
    v       = valor
    if valor < 1000: 
        unidade = ""
                            
    elif valor >= 1000 and valor < 1000000:
        v     = int(valor/1000)
        resto = int(valor%1000/100)
        unidade = "K"
    else:
        v = int(valor/1000000)
        resto = int((valor%1000000)/100000)
        unidade = "M"
    
    res = str(v) + unidade
    if (resto != 0):
        res += str(resto)

    return res
'''