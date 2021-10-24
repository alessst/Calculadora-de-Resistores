from Calculadora import Calculador_Resitores as cl

resistorValor = 2000
toleranciaValor = 5
associacao = 2
lista = [100, 250, 350, 450, 500, 550, 650, 800, 1000, 1500, 2500, 4700, 10000]
s = 1
p = 2
escolha = "0805"


resistorAssocCalc = []
for r1 in lista:
    for r2 in lista:
        serie = cl.serie_calculo(r1, r2)
        paralelo = cl.paralelo_calculo(r1, r2) 

       
        if associacao == s:       
            if serie == resistorValor:
                tamanho = len(resistorAssocCalc) 
                for x in range(0, 5):# 5 igual a tamanho da lista
                    if x == tamanho:
                        print(f"serie - {r1} + {r2} = {cl.unidade(serie)} Ohms |",
                        f"Encapsulamento: {escolha} |",
                        f"Tolerancia Error: {int(cl.calculo_erro(serie, resistorValor))}%")
        
        
        
        if associacao == p:   
            if cl.tolerancia_calculo(resistorValor, paralelo, toleranciaValor):
                resistorAssocCalc.append(paralelo)
                tamanho = len(resistorAssocCalc)  
                for x in range(0,5):# 5 igual a tamanho da lista
                    if x == tamanho:
                        print(f"paralelo - {r1} // {r2} = {cl.unidade(paralelo)} Ohms|",
                         f"Encapsulamento: {escolha} | ",
                         f"Tolerancia Error: {int(cl.calculo_erro(paralelo, resistorValor))}%")



