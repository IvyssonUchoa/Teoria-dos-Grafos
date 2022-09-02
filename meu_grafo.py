import math

from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from math import inf

class MeuGrafo(GrafoListaAdjacencia):
    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um set com os pares de vértices não adjacentes
        '''
        l = set()
        for v1 in self.N:
            for v2 in self.N:
                duplaV1 = "{}-{}".format(v1, v2)
                duplaV2 = "{}-{}".format(v2, v1)

                if (duplaV1 not in l) and (duplaV2 not in l):
                    chave = False

                    for a in self.A:
                        if v1 != v2:
                            if v1 == self.A[a].getV1(
                            ) and v2 == self.A[a].getV2():
                                chave = True
                            elif v1 == self.A[a].getV2(
                            ) and v2 == self.A[a].getV1():
                                chave = True

                    if (chave == False) and (v1 != v2):
                        l.add("{}-{}".format(v1, v2))
        return l

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True

        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V in self.N:
            grau_vertice = 0

            for a in self.A:

                if self.A[a].getV1() == V:
                    grau_vertice += 1
                if self.A[a].getV2() == V:
                    grau_vertice += 1
            return grau_vertice

        else:
            raise VerticeInvalidoException

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a1 in self.A:
            for a2 in self.A:
                if self.A[a1] != self.A[a2]:
                    if (self.A[a1].getV1()
                        == self.A[a2].getV1()) and (self.A[a1].getV2()
                                                    == self.A[a2].getV2()):
                        return True
                    elif (self.A[a1].getV1()
                          == self.A[a2].getV2()) and (self.A[a1].getV2()
                                                      == self.A[a2].getV1()):
                        return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException

        l = set()
        for a in self.A:
            if V == self.A[a].getV1() or V == self.A[a].getV2():
                l.add(a)
        return l

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if (self.vertices_nao_adjacentes()
            == set()) and (self.ha_laco()
                           == False) and (self.ha_paralelas() == False):
            return True
        else:
            return False

    def vertice_oposto(self, aresta='', vertice=''):
        """
        Retorna a segunda extremidade de uma aresta, na qual o primeiro vértice já é conhecido.
        :param aresta: rótulo da aresta que será analisada
        :param vertice: rótulo do vértice conhecido
        :return: um rótulo de vértice
        :return: Vertice oposto inexistente se não existir correspondência entre os parâmetros aresta e vertice
        """
        vertice_oposto = ''

        if self.A[aresta].getV1() == vertice:
            vertice_oposto = self.A[aresta].getV2()
        elif self.A[aresta].getV2() == vertice:
            vertice_oposto = self.A[aresta].getV1()
        else:
            return "Vertice oposto inexistente"

        return vertice_oposto

    def dfs(self, V=''):
        """
        Realiza a busca em profundidade (Depth-first search).
        :param V: rótulo do vértice que será o nó raiz do árvore.
        :return: Uma árvore com os vértices e arestas organizados pela busca em profundidade.
        """
        lista_de_chamada = list()
        vertices_analisados = list()
        arestas_analisadas = list()
        arvore_dfs = MeuGrafo()

        while True:
            arestas_do_vertice = list(self.arestas_sobre_vertice(V))
            arestas_do_vertice.sort(reverse=True)

            for i in arestas_do_vertice:
                if (i not in arvore_dfs.A) and (i
                                                not in lista_de_chamada) and (
                        i
                        not in arestas_analisadas):
                    lista_de_chamada.append(i)

            if len(lista_de_chamada) == 0:
                if len(vertices_analisados) == 0:
                    break
                else:
                    V = vertices_analisados[len(vertices_analisados) - 1]
                    vertices_analisados.pop()

            else:
                aresta_topo = lista_de_chamada[len(lista_de_chamada) - 1]
                V_oposto = self.vertice_oposto(aresta_topo, V)

                if V_oposto == "Vertice oposto inexistente":
                    V = vertices_analisados[len(vertices_analisados) - 1]
                    vertices_analisados.pop()
                else:

                    if V in arvore_dfs.N and V_oposto in arvore_dfs.N:
                        arestas_analisadas.append(aresta_topo)

                    else:
                        if V not in arvore_dfs.N:
                            arvore_dfs.adicionaVertice(V)

                        if V_oposto not in arvore_dfs.N:
                            arvore_dfs.adicionaVertice(V_oposto)

                        arvore_dfs.adicionaAresta(str(aresta_topo), V,
                                                  V_oposto)

                        vertices_analisados.append(V)
                        V = V_oposto

                    lista_de_chamada.pop()
        return arvore_dfs

    def bfs(self, V=''):
        """
        Realiza a busca em largura (Breadth-first search)
        :param V: rótulo de vértice que será o nó raiz do árvore.
        :return: Uma árvore com os vértices e arestas organizados pela busca em largura.
        """
        lista_de_chamada = list()
        vertices_visitados = list()
        arestas_visitadas = list()
        indice_V = 0
        arvore_bfs = MeuGrafo()

        while True:
            arestas_do_vertice = list(self.arestas_sobre_vertice(V))
            arestas_do_vertice.sort(reverse=True)

            for i in arestas_do_vertice:
                if (i not in arvore_bfs.A) and (i
                                                not in lista_de_chamada) and (
                        i
                        not in arestas_visitadas):
                    lista_de_chamada.append(i)

            if len(lista_de_chamada) == 0:

                if len(vertices_visitados) == (indice_V + 1):
                    break
                else:
                    indice_V += 1
                    V = vertices_visitados[indice_V]

            else:
                aresta_topo = lista_de_chamada[len(lista_de_chamada) - 1]  # a9
                V_oposto = self.vertice_oposto(aresta_topo, V)  # Z

                if (V in arvore_bfs.N) and (V_oposto in arvore_bfs.N):
                    arestas_visitadas.append(aresta_topo)

                else:
                    if V not in arvore_bfs.N:
                        arvore_bfs.adicionaVertice(V)
                        vertices_visitados.append(V)

                    if V_oposto not in arvore_bfs.N:
                        arvore_bfs.adicionaVertice(V_oposto)
                        vertices_visitados.append(V_oposto)

                    arvore_bfs.adicionaAresta(str(aresta_topo), V, V_oposto)

                lista_de_chamada.pop()
        return arvore_bfs

    def conexo(self):
        """
        Verifica se o grafo é conexo.
        :return: Um valor booleano que indica se o grafo é conexo.
        """
        arvore_bfs = MeuGrafo()
        V = self.N[0]
        arvore_bfs = self.bfs(V)

        vertices1 = set(arvore_bfs.N)
        vertices2 = set(self.N)

        if vertices1 == vertices2:
            return True
        return False

    def ha_ciclo(self):
        """
        Verifica se existe ciclos dentro do grafo
        :return: uma lista com um caminho que forma um ciclo
        :return: Um valor booleano se não existir um ciclo no grafo
        """
        lista_de_chamada = list()
        vertices_analisados = list()
        arestas_analisadas = list()
        resultado_dfs = list()
        V = self.N[0]

        while True:
            arestas_do_vertice = list(self.arestas_sobre_vertice(V))
            arestas_do_vertice.sort(reverse=True)

            for i in arestas_do_vertice:
                if (i not in resultado_dfs) and (i not in lista_de_chamada) and (i not in arestas_analisadas):
                    lista_de_chamada.append(i)

            if len(lista_de_chamada) == 0:
                if len(vertices_analisados) == 0:
                    return False
                else:
                    V = vertices_analisados[len(vertices_analisados) - 1]
                    vertices_analisados.pop()
                    resultado_dfs.append(V)

            else:
                aresta_topo = lista_de_chamada[len(lista_de_chamada) - 1]
                V_oposto = self.vertice_oposto(aresta_topo, V)

                if V_oposto == "Vertice oposto inexistente":
                    V = vertices_analisados[len(vertices_analisados) - 1]
                    vertices_analisados.pop()
                    resultado_dfs.pop()
                    resultado_dfs.pop()
                else:
                    if V in resultado_dfs and V_oposto in resultado_dfs:
                        if V not in resultado_dfs:
                            resultado_dfs.append(V)

                        resultado_dfs.append(aresta_topo)
                        arestas_analisadas.append(aresta_topo)
                        resultado_dfs.append(V_oposto)
                        break
                    else:
                        if V not in resultado_dfs:
                            resultado_dfs.append(V)

                        resultado_dfs.append(aresta_topo)
                        arestas_analisadas.append(aresta_topo)

                        if V_oposto not in resultado_dfs:
                            resultado_dfs.append(V_oposto)

                        vertices_analisados.append(V)
                        V = V_oposto

                    lista_de_chamada.pop()

        saida = list()
        for i in range(len(resultado_dfs)):
            if resultado_dfs[len(resultado_dfs) - 1] not in saida:
                saida.append(resultado_dfs[len(resultado_dfs) - 1])
                resultado_dfs.pop()

            else:
                saida.append(resultado_dfs[len(resultado_dfs) - 1])
                return saida

    def caminho_dois_vertices(self, x, y):  # x = vertice inicial; y = vertice final
        """
        Percorre o grafo em busca de todos os caminhos simples entre dois vértices
        :param x: vértice de início do caminho
        :param y: vértice final do caminho
        :return: Uma matriz contendo os caminhos simples possíveis entre dois vértices.
        """
        visitado = []
        caminho_atual = []
        caminhos_simples = []
        aresta_atual = [""]

        def cdv_recurssivo(u, v):
            if u in visitado:
                return

            visitado.append(u)
            caminho_atual.append(aresta_atual[0])
            caminho_atual.append(u)

            if u == v:
                copia = deepcopy(caminho_atual[1:])
                caminhos_simples.append(copia)

                visitado.pop()
                caminho_atual.pop()
                caminho_atual.pop()
                return

            arestas_do_vertice = list(self.arestas_sobre_vertice(u))
            arestas_do_vertice.sort()

            for i in arestas_do_vertice:
                aresta_atual[0] = i
                u_oposto = self.vertice_oposto(i, u)
                cdv_recurssivo(u_oposto, v)

            caminho_atual.pop()
            caminho_atual.pop()
            visitado.pop()

        cdv_recurssivo(x, y)
        return caminhos_simples

    def caminho(self,n):
        """
        Provê um caminho no grafo do tamanho desejado.
        :param n: tamanho desejado do caminho
        :return: um caminho do tamanho desejado no formato de lista
        :return: Um valor booleano se o caminho de tamanho desejado não existir.
        """
        for inicio in self.N:
            for fim in self.N:
                matriz_caminhos = self.caminho_dois_vertices(inicio, fim)
                for caminho in matriz_caminhos:
                    if len(caminho) == (n * 2)+1:
                        return caminho
        return False

    def dijkstra_drone(self, vi, vf, carga: int, carga_max: int, pontos_recarga: list()):
        pass

    def falso_dijkstra(self, vi, vf):
        """
        Encontra o caminho de menor peso em um grafo analisando todos os caminhos possíveis
        :param vi: Vértice inicial
        :param vf: Vértice final
        :return: O caminho de menor peso no formato de lista
        """
        """Criado apenas para testes"""
        soma_pesos = 0
        menor_peso = inf
        melhor_caminho = []
        matriz_caminho = self.caminho_dois_vertices(vi, vf)

        for caminho in matriz_caminho:
            for i in range(1, len(caminho), 2):
                aresta = self.getAresta(caminho[i])
                soma_pesos += aresta.getPeso()

            if soma_pesos < menor_peso:
                melhor_caminho = deepcopy(caminho)
                menor_peso = soma_pesos

            soma_pesos = 0
        return melhor_caminho

    def algoritmo_dijkstra(self, vi, vf):
        """
        Encontra o caminho de menor peso entre dois vértices usando o algoritmo de Dijkstra.
        :param vi: vértice de início do caminho
        :param vf: vértice final do caminho
        :return: O caminho de menor peso no formato de lista
        """
        visitados = [vi]
        V_atual = vi # W
        beta = {} #menor caminho do vertice de inicio e o vertice atual
        omega = {} #predecessor do vertice

        for V in self.N:
            beta[V] = 0 if V == vi else math.inf  # beta de vi é zero e dos demais é infinito
            omega[V] = ''

        try:
            while V_atual != vf:
                lista_arestas = self.arestas_sobre_vertice(V_atual)
                for arco in lista_arestas:
                    V_oposto = self.vertice_oposto(arco, V_atual)
                    if V_oposto not in visitados:
                        if beta[V_oposto] > (beta[V_atual] + self.A[arco].getPeso()):
                            beta[V_oposto] = (beta[V_atual] + self.A[arco].getPeso())
                            omega[V_oposto] = V_atual
                menor_beta = ""
                menor_peso = math.inf

                for V in self.N:
                    if beta[V] < menor_peso and V not in visitados:
                        menor_beta = V
                        menor_peso = beta[V]
                visitados.append(menor_beta)
                V_atual = menor_beta
            v_atual = vf
            melhor_caminho = [v_atual]

            for i in range(len(self.N)):
                v_anterior = omega[v_atual]
                melhor_caminho.append(v_anterior)

                if(v_anterior == vi):
                    break
                else:
                    v_atual = v_anterior
            return list(reversed(melhor_caminho))
        except:
            return False

    def aresta_entre_vertices(self, v1, v2):
        """
        Provê a aresta que liga dois vértices
        :param v1: rótulo do primeiro vértice
        :param v2: rótulo do segundo vértice
        :return: o rótulo de uma aresta
        :return Valor booleano caso não exista aresta ligando os vértices.
        """
        for a in self.A:
            aresta = self.A[a]
            if aresta.getV1() == v1 and aresta.getV2() == v2:
                return a

            if aresta.getV1() == v2 and aresta.getV2() == v1:
                return a
        return False

    def algoritmo_prim_modificado(self):
        """
        Gera a Minimum Spanning Tree do grafo pelo algoritimo de Prim.
        :return: uma árvore de MST.
        """
        Jet = {}
        P = {}
        MST = MeuGrafo()

        for v in self.N:
            Jet[v] = inf
            P[v] = None

        menor_peso = inf
        menor_vertice = ""
        for a in self.A:
            if self.A[a].getPeso() < menor_peso:
                menor_peso = self.A[a].getPeso()
                menor_vertice = a

        raiz = self.A[menor_vertice].getV1()
        Jet[raiz] = 0

        Q = deepcopy(self.N)

        while(len(Q) > 0):
            menor_peso = inf
            menor_vertice = ""
            for v in Q:
                if Jet[v] < menor_peso:
                    menor_vertice = v
                    menor_peso = Jet[v]

            x = menor_vertice
            Q.remove(x)

            arestas_adjacentes = self.arestas_sobre_vertice(x)
            for a in arestas_adjacentes:
                y = self.vertice_oposto(a, x)

                if y in Q and self.A[a].getPeso() < Jet[y]:
                    P[y] = x
                    Jet[y] = self.A[a].getPeso()

        for v1 in P:
            if P[v1]:
                v2 = P[v1]

                if v1 not in MST.N:
                    MST.adicionaVertice(v1)

                if v2 not in MST.N:
                    MST.adicionaVertice(v2)

                aresta = self.aresta_entre_vertices(v1,v2)

                if aresta not in MST.A:
                    MST.adicionaAresta(aresta, v2, v1, self.A[aresta].getPeso())

        return MST