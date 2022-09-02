from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        l = set()
        for v1 in range(len(self.N)):
            for v2 in range(v1, len(self.N)):
                if v1 != v2:
                    if not self.M[v1][v2]:
                        l.add("{}-{}".format(self.N[v1], self.N[v2]))
        return l

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for v in range(len(self.N)):
            if self.M[v][v]:
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
            grau = 0
            vertice = self.N.index(V)

            for v1 in range(len(self.N)):
                for v2 in range(v1, len(self.N)):

                    dic_arestas = self.M[v1][v2]
                    if dic_arestas:
                        if v1 == vertice:
                            grau += len(dic_arestas)

                        if v2 == vertice:
                            grau += len(dic_arestas)

            return grau
        else:
            raise VerticeInvalidoException

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for v1 in range(len(self.N)):
            for v2 in range(v1, len(self.N)):
                dicionario_arestas = self.M[v1][v2]
                if len(dicionario_arestas) > 1:
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
        vertice = self.N.index(V)

        for v1 in range(len(self.N)):
            for v2 in range(v1, len(self.N)):
                if (v1 == vertice or v2 == vertice) and (self.M[v1][v2]):
                    for aresta in self.M[v1][v2]:
                        l.add(aresta)
        return l


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if (self.vertices_nao_adjacentes() == set()) and (self.ha_laco() == False) and (self.ha_paralelas() == False):
            return True
        else:
            return False