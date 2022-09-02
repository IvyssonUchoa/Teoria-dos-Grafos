import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Outro Grafo da Paraíba
        self.g_p2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p2.adicionaAresta('a1', 'J', 'C')
        self.g_p2.adicionaAresta('a2', 'C', 'E')
        self.g_p2.adicionaAresta('a3', 'C', 'E')
        self.g_p2.adicionaAresta('a4', 'P', 'J')
        self.g_p2.adicionaAresta('a5', 'P', 'C')
        self.g_p2.adicionaAresta('a6', 'T', 'C')
        self.g_p2.adicionaAresta('a7', 'M', 'P')
        self.g_p2.adicionaAresta('a8', 'M', 'T')
        self.g_p2.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        # Arvore 1 bfs de g_p
        self.arvore = MeuGrafo(['J', 'C', 'E', 'P', 'T', 'M', 'Z'])
        self.arvore.adicionaAresta('a1', 'J', 'C')
        self.arvore.adicionaAresta('a2', 'C', 'E')
        self.arvore.adicionaAresta('a4', 'C', 'P')
        self.arvore.adicionaAresta('a6', 'C', 'T')
        self.arvore.adicionaAresta('a7', 'M', 'C')
        self.arvore.adicionaAresta('a9', 'T', 'Z')

        #Arvore 2 bfs de g_p
        self.arvore2 = MeuGrafo(['J', 'C', 'E', 'P', 'T', 'Z', 'M'])
        self.arvore2.adicionaAresta('a6', 'T', 'C')
        self.arvore2.adicionaAresta('a8', 'T', 'M')
        self.arvore2.adicionaAresta('a9', 'T', 'Z')
        self.arvore2.adicionaAresta('a1', 'C', 'J')
        self.arvore2.adicionaAresta('a2', 'C', 'E')
        self.arvore2.adicionaAresta('a4', 'C', 'P')

        #Arvore 3 bfs de g_p2
        self.arvore3 = MeuGrafo(['J', 'C', 'E', 'P', 'T', 'M', 'Z'])
        self.arvore3.adicionaAresta('a4', 'P', 'J')
        self.arvore3.adicionaAresta('a5', 'P', 'C')
        self.arvore3.adicionaAresta('a7', 'P', 'M')
        self.arvore3.adicionaAresta('a2', 'C', 'E')
        self.arvore3.adicionaAresta('a6', 'C', 'T')
        self.arvore3.adicionaAresta('a9', 'T', 'Z')

        #Arvore 4 bfs de g_p2
        self.arvore4 = MeuGrafo(['J', 'C', 'E', 'P', 'T', 'M', 'Z'])
        self.arvore4.adicionaAresta('a1', 'J', 'C')
        self.arvore4.adicionaAresta('a4', 'J', 'P')
        self.arvore4.adicionaAresta('a2', 'C', 'E')
        self.arvore4.adicionaAresta('a6', 'C', 'T')
        self.arvore4.adicionaAresta('a7', 'P', 'M')
        self.arvore4.adicionaAresta('a9', 'T', 'Z')

        #Arvore 5 bfs de g_p sem paralelas
        self.arvore5 = MeuGrafo(['J', 'C', 'E', 'Z', 'T', 'P', 'M'])
        self.arvore5.adicionaAresta('a5', 'M', 'C')
        self.arvore5.adicionaAresta('a6', 'M', 'T')
        self.arvore5.adicionaAresta('a1', 'C', 'J')
        self.arvore5.adicionaAresta('a2', 'C', 'E')
        self.arvore5.adicionaAresta('a3', 'C', 'P')
        self.arvore5.adicionaAresta('a7', 'T', 'Z')

        #Arvore 6 bfs de g_c
        self.arvore6 = MeuGrafo(['J', 'E', 'C', 'P'])
        self.arvore6.adicionaAresta('a1', 'J', 'C')
        self.arvore6.adicionaAresta('a2', 'J', 'E')
        self.arvore6.adicionaAresta('a3', 'J', 'P')

        #Arvore 7 bfs de g_c
        self.arvore7 = MeuGrafo(['J', 'E', 'C', 'P'])
        self.arvore7.adicionaAresta('a1', 'C', 'J')
        self.arvore7.adicionaAresta('a4', 'C', 'E')
        self.arvore7.adicionaAresta('a5', 'C', 'P')

        #Arvore 8 bfs de g_c2
        self.arvore8 = MeuGrafo(['Nina', 'Maria'])
        self.arvore8.adicionaAresta('amiga', 'Nina', 'Maria')

    def teste_bfs(self):
        self.assertEqual(self.g_p.bfs('J'), self.arvore)
        self.assertEqual(self.g_p.bfs('T'), self.arvore2)
        self.assertEqual(self.g_p2.bfs('P'), self.arvore3)
        self.assertEqual(self.g_p2.bfs('J'), self.arvore4)
        self.assertEqual(self.g_p_sem_paralelas.bfs('M'), self.arvore5)
        self.assertEqual(self.g_c.bfs('J'), self.arvore6)
        self.assertEqual(self.g_c.bfs('C'), self.arvore7)
        self.assertEqual(self.g_c2.bfs('Nina'), self.arvore8)