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
        self.g_p2.adicionaAresta('a3', 'P', 'J')
        self.g_p2.adicionaAresta('a4', 'P', 'C')
        self.g_p2.adicionaAresta('a5', 'T', 'C')
        self.g_p2.adicionaAresta('a6', 'M', 'P')
        self.g_p2.adicionaAresta('a7', 'M', 'T')
        self.g_p2.adicionaAresta('a8', 'T', 'Z')

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
        self.g_c1 = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c1.adicionaAresta('a1', 'J', 'C')
        self.g_c1.adicionaAresta('a2', 'J', 'E')
        self.g_c1.adicionaAresta('a3', 'J', 'P')
        self.g_c1.adicionaAresta('a4', 'E', 'C')
        self.g_c1.adicionaAresta('a5', 'P', 'C')
        self.g_c1.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        # Grafo desconexo
        self.g_d1 = MeuGrafo(['C', 'J', 'E', 'P', 'A', 'B'])
        self.g_d1.adicionaAresta('a1', 'J', 'C')
        self.g_d1.adicionaAresta('a2', 'J', 'E')
        self.g_d1.adicionaAresta('a3', 'J', 'P')
        self.g_d1.adicionaAresta('a4', 'E', 'C')
        self.g_d1.adicionaAresta('a5', 'P', 'C')
        self.g_d1.adicionaAresta('a6', 'P', 'E')
        self.g_d1.adicionaAresta('a7', 'A', 'B')
        self.g_d1.adicionaAresta('a8', 'A', 'A')

        self.g_d2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.g_d2.adicionaAresta('a1', 'A', 'B')
        self.g_d2.adicionaAresta('a2', 'C', 'A')
        self.g_d2.adicionaAresta('a3', 'C', 'B')
        self.g_d2.adicionaAresta('a4', 'B', 'A')
        self.g_d2.adicionaAresta('a5', 'E', 'F')
        self.g_d2.adicionaAresta('a6', 'F', 'G')

    def teste_ha_ciclo(self):
        self.assertEqual(self.g_p.ha_ciclo(), ['C', 'a3', 'E', 'a2', 'C'])
        self.assertEqual(self.g_p2.ha_ciclo(), ['C', 'a5', 'T', 'a7', 'M', 'a6', 'P', 'a4', 'C'])
        self.assertEqual(self.g_c1.ha_ciclo(), ['C', 'a5', 'P', 'a6', 'E', 'a4', 'C'])
        self.assertEqual(self.g_c2.ha_ciclo(), False)
        self.assertEqual(self.g_d1.ha_ciclo(), ['J', 'a3', 'P', 'a6', 'E', 'a2', 'J'])
        self.assertEqual(self.g_d2.ha_ciclo(), ['A', 'a2', 'C', 'a3', 'B', 'a1', 'A'])

    def teste_caminho(self):
        self.assertEqual(self.g_p.caminho(2), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertEqual(self.g_p.caminho(3), ['J', 'a1', 'C', 'a6', 'T', 'a8', 'M'])
        self.assertEqual(self.g_p.caminho(4), ['J', 'a1', 'C', 'a7', 'M', 'a8', 'T', 'a9', 'Z'])

        self.assertEqual(self.g_p2.caminho(2), ['J', 'a3', 'P', 'a4', 'C'])
        self.assertEqual(self.g_p2.caminho(3), ['J', 'a3', 'P', 'a4', 'C', 'a2', 'E'])
        self.assertEqual(self.g_p2.caminho(4), ['J', 'a3', 'P', 'a6', 'M', 'a7', 'T', 'a5', 'C'])

        self.assertEqual(self.g_p_sem_paralelas.caminho(2), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertEqual(self.g_p_sem_paralelas.caminho(3), ['J', 'a1', 'C', 'a4', 'T', 'a6', 'M'])
        self.assertEqual(self.g_p_sem_paralelas.caminho(4), ['J', 'a1', 'C', 'a5', 'M', 'a6', 'T', 'a7', 'Z'])

        self.assertEqual(self.g_c1.caminho(2), ['J', 'a2', 'E', 'a4', 'C'])
        self.assertEqual(self.g_c1.caminho(3), ['J', 'a2', 'E', 'a6', 'P', 'a5', 'C'])
        self.assertEqual(self.g_c1.caminho(4), False)

        self.assertEqual(self.g_c2.caminho(1), ['Nina', 'amiga', 'Maria'])
        self.assertEqual(self.g_c2.caminho(2), False)
        self.assertEqual(self.g_c2.caminho(3), False)

        self.assertEqual(self.g_d1.caminho(2), ['C', 'a4', 'E', 'a2', 'J'])
        self.assertEqual(self.g_d1.caminho(3), ['C', 'a4', 'E', 'a6', 'P', 'a3', 'J'])
        self.assertEqual(self.g_d1.caminho(4), False)

        self.assertEqual(self.g_d2.caminho(2), ['A', 'a2', 'C', 'a3', 'B'])
        self.assertEqual(self.g_d2.caminho(3), False)
        self.assertEqual(self.g_d2.caminho(4), False)

    def teste_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_p2.conexo())
        self.assertTrue(self.g_p_sem_paralelas.conexo())
        self.assertTrue(self.g_c1.conexo())
        self.assertTrue(self.g_c2.conexo())

        self.assertFalse(self.g_d1.conexo())
        self.assertFalse(self.g_d2.conexo())
