"""
Universidade Federal de Pernambuco
IF 969 - ALgoritmos e estrutura de dados
Aluno: Pedro Henrique Roseno Bastos Silva
"""


class GrafoLista:
    def __init__(self, teste, direcionado=False):
        self.vertices = []
        self.grafo = {}
        self.direcionado = direcionado
        self.recuperaGrafo(teste)
 
    #O vértice é dado por um inteiro
    def addVertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
        else:
            raise IndexError("Vertice já se encontra no grafo")
 
    def addAresta(self, vertice1, vertice2):
        print(self.direcionado)
        if self.direcionado is False:
            #se for direcionado ele adiciona uma aresta que vai nas duas direções
            if vertice1 in self.grafo and vertice2 in self.grafo:
                self.grafo[vertice1].append(vertice2)
                self.grafo[vertice2].append(vertice1)
            else:
                raise IndexError("Algum dos vértices não foi encontrado!")
        else:
            #Caso não, apenas do vértice 1 ao 2
            if vertice1 in self.grafo and vertice2 in self.grafo:
                self.grafo[vertice1].append(vertice2)
            else:
                raise IndexError("Algum dos vértices não foi encontrado!")
 
    def __getitem__(self, indice):
        if self.direcionado is False:
            a = self.grafo[indice]
            return a
        else:
            lista = []
            for elemento in self.grafo:
                for tupla in self.grafo[elemento]:
                    if tupla[0] == indice:
                        lista.append(tupla)
            return lista
 
    def __str__(self):
        string = ""
        for elemento in self.grafo:
            string += "\n" + str(elemento) + ":"
            for tupla in self.grafo[elemento]:
                string += str(tupla) + " "
        return string
 
    def removeVertice(self, indice):
        for elemento in self.grafo:
            cont = 0
            for tupla in self.grafo[elemento]:
                if tupla[0] == indice:
                    self.grafo[elemento].pop(cont)
                cont += 1
        return self.grafo
 
    def removeAresta(self, a, b):
        cont = 0
        for elemento in self.grafo[a]:
            if elemento[0] == b:
                self.grafo[a].pop(cont)
            cont += 1
        return self.grafo
 
    def verticeLigado(self, a, b):
        ligacao = False
        for elemento in self.grafo[a]:
            if elemento[0] == b:
                ligacao = True
        for elemento in self.grafo[b]:
            if elemento[0] == a:
                ligacao = True
 
        return ligacao
 
    def grauDeSaida(self, vertice):
        return len(self.grafo[vertice])
 
    def grauDeEntrada(self, vertice):
        contagem = 0
        for elemento in self.grafo:
            for tupla in self.grafo[elemento]:
                if tupla[0] == vertice:
                    contagem += 1
        return contagem
 
    def adjacente(self, vertice):
        listaAdjacentes = []
        for elemento in self.grafo:
            for tupla in self.grafo[elemento]:
                if tupla[0] == vertice:
                    listaAdjacentes.append(elemento)
        for elemento in self.grafo[vertice]:
            if elemento[0] not in listaAdjacentes:
                listaAdjacentes.append(elemento[0])
        return listaAdjacentes
 
    def maiorAresta(self):
        #VérticeO guarda a informação do vértice
        verticeO = None
        maior = None
        for elemento in self.grafo:
            for tupla in self.grafo[elemento]:
                if maior is None:
                    maior = tupla
                else:
                    if tupla[1] > maior[1]:
                        maior =  tupla
                        verticeO = elemento
        return "A maior aresta é ({}) ----- ({}) com peso {}".format(verticeO, maior[0], maior[1])
 
    def menorAresta(self):
      #VérticeO guarda a informação do vértice
        verticeO = None
        menor = None
        for elemento in self.grafo:
            for tupla in self.grafo[elemento]:
                if menor is None:
                    menor = tupla
                else:
                    if tupla[1] < menor[1]:
                        menor =  tupla
                        verticeO = elemento
        return "A menor aresta é ({}) ----- ({}) com peso {}".format(verticeO, menor[0], menor[1])
    
    def listaPmatriz(self):
        listaGrafo = []
        for elemento in self.grafo:
            for tupla in self.grafo[elemento]:
                listaGrafo.append(tupla)
        grafoMatriz = GrafoMatriz(listaGrafo)
        return grafoMatriz

    def recuperaGrafo(self, grafo):
        #adicionando vértices
        for elemento in grafo:
            if elemento[0] not in self.grafo:
                self.grafo[elemento[0]] = []
            if elemento[1] not in self.grafo:
                self.grafo[elemento[1]] = []
        #adicionando arestas  
        for elemento in grafo:
            if len(elemento) == 3:
                self.grafo[elemento[0]].append((elemento[1], elemento[2]))
            else:
                self.grafo[elemento[0]].append(elemento[1])
 
    def printaGrafo(self):
        return self.grafo
 
    def dfs_x(self,graph, node, visited):
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                self.dfs_x(graph,n, visited)
        return visited

    def dfs(self,node):
      graph = self.grafo
      try:
        if len(self.grafo[start][0]) == 2:
          graph = self.transform()
          visited = []
          return self.dfs_x(graph,node,visited)
      except:
        visited = []
        return self.dfs_x(graph,node,visited)

    def bfs_x(self,graph, start):
        explored = []
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in explored:
                explored.append(node)
                neighbours = graph[node]
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored
    
    def bfs(self,start):
      graph = self.grafo
      try:
        if len(self.grafo[start][0]) == 2:
          graph = self.transform()
          visited = []
          return self.bfs_x(graph,start)
      except:
        visited = []
        return self.bfs_x(graph,start)
  
    def transform(self):
      graph = self.grafo
      for x in graph:
        lista = []
        for y  in graph[x]:
          lista.append(y[0])
        graph[x] = lista
      return graph
    

def findIndex(index,lista):
  cont = 0
  for elemento in lista:
    if elemento == index:
      return cont
    cont += 1
  return None

class GrafoMatriz:
 
    def __init__(self, teste, direcionado=False):
        self.grafo = []
        self.vertices = []
        self.direcionado = direcionado
        self.recuperaGrafo(teste)
    
    def addVertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            for elemento in self.grafo:
                elemento.append(0)
            self.grafo.append([0]* len(self.vertices))
        else:
            print("elemento já se encontra no grafo")
    
    def addAresta(self, vertice1, vertice2, peso=None):
        a = findIndex(vertice1, self.vertices)
        b = findIndex(vertice2, self.vertices)
        if peso == None:
            if direcionado:
                self.grafo[a][b] = 1
                self.grafo[b][a] = 1
            else:
                self.grafo[a][b] = 1
        else:
            if direcionado:
                self.grafo[a][b] = peso
                self.grafo[b][a] = peso
            else:
                self.grafo[a][b] = peso
                
    def removerAresta(self, vertice1, vertice2):
        a = findIndex(vertice1, self.vertices)
        b = findIndex(vertice2, self.vertices)
        if direcionado:
            self.grafo[a][b] = 0
            self.grafo[b][a] = 1
        else:
            self.grafo[a][b] = 1


    def recuperaGrafo(self, grafo):
        for elemento in grafo:
            if elemento[0] not in self.vertices:
                    self.vertices.append(elemento[0])
            if elemento[1] not in self.vertices:
                    self.vertices.append(elemento[1])
        for elemento in self.vertices:
            self.grafo.append([0] * len(self.vertices))
        for tupla in grafo:
          if len(tupla) == 2:
            v = findIndex(tupla[0],self.vertices)
            v1 = findIndex(tupla[1],self.vertices)
            self.grafo[v][v1] = 1
          elif len(tupla) == 3:
            v = findIndex(tupla[0],self.vertices)
            v1 = findIndex(tupla[1],self.vertices)
            self.grafo[v][v1] = tupla[2]
    
    
    def __getitem__(self, vertice):
        listaTuplas = []
        indice2 = findIndex(vertice, self.vertices)
        cont = 0
        for elemento in self.grafo:
            if cont != indice2:
                if elemento[indice2] != 0:
                  listaTuplas.append((self.vertices[cont],self.vertices[indice2]))
            if cont == indice2:
              cont2 = 0
              for x in elemento:
                if x != 0:
                  listaTuplas.append((self.vertices[indice2],self.vertices[cont2]))
                cont2 += 1
            cont += 1
        return listaTuplas
    
    def __str__(self):
        return str(self.grafo)

    def transform(self,grafo):
      vertices = self.vertices
      lista = []
      cont = 0
      for listas in grafo:
        cont2 = 0
        for elemento in listas:
          if elemento != 0:
            lista.append((vertices[cont],vertices[cont2]))
          cont2 += 1
        cont += 1
      return lista
    
    def grauDeEntrada(self, vertice):
        contador = 0
        indice = findIndex(vertice, self.vertices)
        for elemento in self.grafo:
            if elemento[indice] != 0:
                contador += 1
        return contador 
    
    def grauDeSaida(self, vertice):
        contador = 0
        indice = finxIndex(vertice, self.vertices)
        for elemento in self.grafo[indice]:
            if elemento != 0:
                contador += 1
        return contador
    
    def verticesLigados(self, vertice1, vertice2):
        a = findIndex(vertice1, self.vertices)
        b = findIndex(vertice2, self.vertices)
        if self.grafo[a][b] != 0:
            return True
        elif self.grafo[b][a] != 0:
            return True
        else:
            return False
    
    def maiorAresta(self):
        vertices = self.vertices
        vertice1 = None
        vertice2 = None
        maior = 0
        cont = 0
        for elemento in self.grafo:
          cont2 = 0
          for indice in elemento:
              if indice > maior:
                  maior = indice
                  vertice1 = self.vertices[cont]
                  vertice2 = self.vertices[cont2]
              cont2 += 1
          cont += 1
        
        print('({})---({}) com peso'.format(vertice1, vertice2, maior))
    
    def menorAresta(self):
        vertices = self.vertices
        vertice1 = None
        vertice2 = None
        menor = None
        cont = 0
        flag = True
        for elemento in self.grafo:
            cont2 = 0
            for indice in elemento:
                if indice != 0:
                    if flag == True:
                        menor = indice
                        vertice1 = self.vertices[cont]
                        vertice2 = self.vertices[cont2]
                        menor = indice
                    else:
                        if indice < menor:
                            menor = indice
                            vertice1 = self.vertices[cont]
                            vertice2 = self.vertices[cont2]
                    cont2 += 1
            cont += 1
        if vertice1 == None or vertice2 == None:
            raise IndexError('')
        print('({})---({}) com peso'.format(vertice1, vertice2, menor))
    
    def verticesAdjascentes(self,vertice):
      cont = findIndex(vertice,self.vertices)
      if cont == None:
        raise IndexError('Esse vertice não existe no grafo')
      v1 = self.vertices[cont]
      listaAdjascencia = []
      cont2 = 0
      for vertice in self.grafo[cont]:
        if vertice != 0:
          listaAdjascencia.append(self.vertices[cont2])
        cont2 += 1
      return listaAdjascencia

    def dfs_x(self,graph, node, visited):
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                self.dfs_x(graph,n, visited)
        return visited

    def dfs(self,node):
      graph = GrafoLista(self.transform(self.grafo)).grafo
      print(graph)
      visited = []
      return self.dfs_x(graph,node,visited)

    def bfs_x(self,graph, start):
        explored = []
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in explored:
                explored.append(node)
                neighbours = graph[node]
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored
    
    def bfs(self,start):
      graph = GrafoLista(self.transform(self.grafo)).grafo
      print(graph)
      return self.bfs_x(graph,start)
    
    def matrizPlista(self):
        grafo = self.grafo
        vertices = self.vertices
        cont = 0
        lista = []
        for elemento in grafo:
            cont2 = 0
            for indice in elemento:
                if indice != 0:
                    lista.append((vertices[cont],vertices[cont2], indice))
                cont2 += 1
            cont += 1
        grafo = GrafoLista(lista)
        return grafo
      
teste = ((0, 1,4), (1, 2,2), (2,1,1),(2, 6,9), (2, 4,3), (4,2,5),(2,3,11),(3,2,2),(4,5,4),(5,4,7),(3,5,4),(7,6,1),(6,7,7),(6,3,8))
grafo = GrafoLista(teste)
print(grafo.grafo)
grafo2 = grafo.listaPmatriz()
print(grafo2)
grafo3 = grafo2.matrizPlista()
print(grafo3)

















""""   
teste = ((0, 1), (1, 2), (2, 1),(2, 6), (2, 4), (4,2),(2,3),(3,2),(4,5),(5,4),(3,5),(7,6),(6,7),(6,3))
teste2 = ((0,1),(0,2),(1,2),(2,3),(3,1),(3,2))
g = GrafoLista(teste)
a = g.grafo
print(a)
x = dfs(a,2,[])
print(x)
z = bfs(a,2)
print(z)
"""
