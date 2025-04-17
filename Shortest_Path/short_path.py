import heapq
from typing import List

class Graph:
    def __init__(self, n: int, arestas: List[List[int]]):
        self.num_nos = n
        self.lista_adjacencia = [[] for _ in range(n)]
        for aresta in arestas:
            self.adicionarAresta(aresta)

    def adicionarAresta(self, aresta: List[int]) -> None:
        no_origem, no_destino, custo = aresta
        self.lista_adjacencia[no_origem].append((no_destino, custo))

    def caminhoMaisCurto(self, no_inicio: int, no_fim: int) -> int:
        if no_inicio == no_fim:
            return 0
        
        distancias = [float('inf')] * self.num_nos
        distancias[no_inicio] = 0
        
        fila_prioridade = []
        heapq.heappush(fila_prioridade, (0, no_inicio))
        
        while fila_prioridade:
            distancia_atual, no_atual = heapq.heappop(fila_prioridade)
            
            if no_atual == no_fim:
                return distancia_atual
            
            if distancia_atual > distancias[no_atual]:
                continue
            
            for vizinho, custo in self.lista_adjacencia[no_atual]:
                nova_distancia = distancia_atual + custo
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
        
        return -1 if distancias[no_fim] == float('inf') else distancias[no_fim]