class Procura_Valor():

    def encontrar(self, elemento, lista):
        self.lista = lista
        self.elemento = elemento
        return [dado for dado in self.lista if self.elemento in dado]


    def print_valores_encontrados(self):
        for i in self.encontrar(self.elemento, self.lista):
            print(f'Nome: {i[0]}')
            print(f'Idade: {i[1]}')
            print(f'CPF: {i[2]}')
            print(f'CEP: {i[3]}')
            print(f'Rua: {i[4]}')
            print(f'Numero: {i[5]}')
            print(f'Bairro: {i[6]}')
            print(f'Cidade: {i[7]}')
            print(f'Estado: {i[8]}')
            print(f'Pais: {i[9]}')
            print(f'Profissão: {i[10]}')
            print(f'Data: {i[11]}')


class Filtra():

    def encontrar(elemento, lista):
        pos_i = 0 # variável provisória de índice
        pos_j = 0 # idem

        for i in range (len(lista)): # procurar em todas as listas internas
            for j in range (i): # procurar em todos os elementos nessa lista
                if elemento in lista[i][j]: # se encontrarmos elemento ('ana')
                    pos_i = i # guardamos o índice i
                    pos_j = j # e o índice j
                    break # saímos do loop interno
                break # e do externo
        return (pos_i, pos_j) # e retornamos os índices


    #Filtra a Lista para os encapsulamentos
    def filtro_lista(self, itens):
        obj = {}
        for i in itens:
            if i[0] in obj.keys():
                obj[i[0]].append(i[1])
            else:
                obj[i[0]] = [i[1]]
        return obj


    #mudar modo que é feito
    #Cria um range da lista
    def lista(self, valor, lista):
        menor = valor/2
        maior = valor*2
        resistorLista = list(filter(lambda r: r >= menor and r <= maior, lista))
        return resistorLista


    #Escolha do encap
    def escolhe_encap(self, escolha, resistorValor, lista_planilha):
        resistores = lista_planilha
        filtro  = self.filtro_lista(resistores)
        f = filtro["R"+escolha]
        resistores = self.lista(resistorValor, f)
        return resistores


class Adiciona_Valores():

    def add_valor(self):
        pass
    
    def atualiza_valores(self):
        pass


