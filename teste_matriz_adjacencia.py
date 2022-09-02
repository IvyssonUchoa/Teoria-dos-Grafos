from meu_grafo_matriz_adjacencia_nao_dir import *
from bibgrafo.grafo_exceptions import *

grafo_paraiba = MeuGrafo()
grafo_paraiba.adicionaVertice("J")
grafo_paraiba.adicionaVertice("C")
grafo_paraiba.adicionaVertice("E")
grafo_paraiba.adicionaVertice("P")
grafo_paraiba.adicionaVertice("M")
grafo_paraiba.adicionaVertice("T")
grafo_paraiba.adicionaVertice("Z")
grafo_paraiba.adicionaAresta('a1', 'J', 'C')
grafo_paraiba.adicionaAresta('a2', 'C', 'E')
grafo_paraiba.adicionaAresta('a3', 'C', 'E')
grafo_paraiba.adicionaAresta('a4', 'P', 'C')
grafo_paraiba.adicionaAresta('a5', 'P', 'C')
grafo_paraiba.adicionaAresta('a6', 'T', 'C')
grafo_paraiba.adicionaAresta('a7', 'M', 'C')
grafo_paraiba.adicionaAresta('a8', 'M', 'T')
grafo_paraiba.adicionaAresta('a9', 'T', 'Z')
grafo_paraiba.adicionaAresta('a10', 'J', 'J')

g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'C', 'E')
g_p.adicionaAresta('a4', 'P', 'C')
g_p.adicionaAresta('a5', 'P', 'C')
g_p.adicionaAresta('a6', 'T', 'C')
g_p.adicionaAresta('a7', 'M', 'C')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z')

g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('a1', 'A', 'A')
g_l1.adicionaAresta('a2', 'A', 'B')
#g_l1.adicionaAresta('a3', 'A', 'A')

dic_vertice = {"J": 0, "C": 1, "E": 2, "P": 3, "M": 4, "T": 5, "Z": 6}
dic2_vertice = {0: "J", 1: "C", 2: "E", 3: "P", 4: "M", 5: "T", 6: "Z"}

print(g_p.arestas_sobre_vertice("J"))