class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def inserirEsquerda(self, filhoesquerda):            #O(n)
        noEsquerda = Node(filhoesquerda)
        self.esquerda = noEsquerda

    def inserirDireita(self, filhodireita):            #O(n)
        noDireita = Node(filhodireita)
        self.direita = noDireita

class BinaryTree:
    def __init__(self, raiz):            #O(n)
        self.raiz = raiz

    def getValorraiz(self):            #O(n)
        return self.raiz.valor
    
    def setvalorraiz(self, valor):            #O(n)
        self.raiz = valor

    def inserirFilho(self, noPai, valor):            #O(n) e 2 paradas
        if valor < noPai.valor:
           if noPai.esquerda is None:
                novoFilho = Node(valor)
                noPai.esquerda = novoFilho
           else:
               self.inserirFilho(noPai.esquerda, valor)
        else:
            if noPai.direita is None:
                novoFilho = Node(valor)
                noPai.direita = novoFilho
            else:
                self.inserirFilho(noPai.direita, valor)

    def printInorder(self, noPai):            #O(n)
        if noPai:
            self.printInorder(noPai.esquerda)
            print(noPai.valor)
            self.printInorder(noPai.direita)

    def printPreorder(self, noPai):            #O(n)
        if noPai:
            print(noPai.valor)
            self.printPreorder(noPai.esquerda)
            self.printPreorder(noPai.direita)

    def printPosorder(self, noPai):            #O(n)
        if noPai:
            self.printPosorder(noPai.esquerda)
            self.printPosorder(noPai.direita)
            print(noPai.valor)

    def simetrica(self, noPai):            #O(n) e 1 parada
        listacombianda = []
        self.listInorder(noPai, listacombianda)
        tamanho = len(listacombianda)
        for i in range(tamanho // 2):
            if listacombianda[i] != listacombianda[tamanho - i - 1]:
                return "Não é simetrica"
                break
            return "É simetrica"

    def listInorder(self, noPai, lista):            #O(n)
        if noPai:
            self.listInorder(noPai.esquerda, lista)
            lista.append(noPai.valor)
            self.listInorder(noPai.direita, lista)

    def balanco(self):            #O(n)
        return self.profundidade(self.raiz.esquerda) - self.profundidade(self.raiz.direita)
    
    def profundidade(self, no):            #O(n) e 1 parada
        if no is None:
            return 0
        return 1 + max(self.profundidade(no.esquerda), self.profundidade(no.direita))
    
    def balancear(self):            #O(n) e 1 parada
        if arvore.balanco() <= 1:
            return "É balanceada"
        else:
            return "Não está balanceada"
        
#----------------------------------------------------------------------------------------
def bubble_sort(lista):                      #Complexidade espacial: O(n^2)
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def busca_binaria(lista, item):             #complexidade: O(log n) e 1 parada
    tamanho = len(lista)
    limit_inf = 0
    limit_sup = tamanho - 1

    while limit_inf <= limit_sup:
        indice = (limit_inf + limit_sup) // 2
        if lista[indice] == item:
            return True
        elif lista[indice] < item:
            limit_inf = indice + 1
        else:
            limit_inf = indice - 1
    return False

def busca_sequencial(lista, item):
    tamanho = len(lista)
    for i in range(tamanho):
        if lista[i] == item:
            return True
    return False

#----------------------------------------------------------------------------------------
class Vertice:

    def __init__(self, id):
        self.id = id
        self.adjacentes = {}

    def getId(self):
        return self.id

    def getVizinhos(self):
        return self.adjacentes.keys()

    def imprimeVizinhos(self):
        for key in self.adjacentes.keys():
            print(f"{self.id} -- {self.adjacentes[key]} --> {key}")

    def adicionaVizinho(self, chave, peso):
        self.adjacentes[chave] = peso

    def getPeso(self, vizinho):
        return self.adjacentes[vizinho]


class Grafo:

    def __init__(self):
        self.vertices = []

    def criaVertice(self, id):
        vertice = Vertice(id)
        self.vertices.append(vertice)
        return vertice

    def adicionaAresta(self, verticeOrigem, verticeDestino, peso):
        verticeOrigem.adicionaVizinho(verticeDestino.getId(), peso)

#----------------------------------------------------------------------------------------
def encontrar_juiz(num_pessoas, arestas):
    confianca = [0] * (num_pessoas + 1)
    desconfianca = set()

    # Conta a confiança e desconfiança de cada pessoa
    for a, b in arestas:
        desconfianca.add(a)
        confianca[b] += 1

    # Verifica se há uma pessoa confiada por todos e que não confia em ninguém
    for i in range(1, num_pessoas + 1):
        if i not in desconfianca and confianca[i] == num_pessoas - 1:
            return i

    return -1