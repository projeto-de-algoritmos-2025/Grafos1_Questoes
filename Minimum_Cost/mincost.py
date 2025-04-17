import heapq

class Solution:
    def minCost(self, grade: List[List[int]]) -> int:
        linhas, colunas = len(grade), len(grade[0])
        direcoes = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        fila_prioridade = []
        heapq.heappush(fila_prioridade, (0, 0, 0))
        distancias = [[float('inf')] * colunas for _ in range(linhas)]
        distancias[0][0] = 0
        
        while fila_prioridade:
            custo, linha, coluna = heapq.heappop(fila_prioridade)
            if linha == linhas - 1 and coluna == colunas - 1:
                return custo
            if custo > distancias[linha][coluna]:
                continue
            for direcao in [1, 2, 3, 4]:
                delta_linha, delta_coluna = direcoes[direcao]
                nova_linha = linha + delta_linha
                nova_coluna = coluna + delta_coluna
                custo_adicional = 0 if direcao == grade[linha][coluna] else 1
                novo_custo = custo + custo_adicional
                if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas:
                    if novo_custo < distancias[nova_linha][nova_coluna]:
                        distancias[nova_linha][nova_coluna] = novo_custo
                        heapq.heappush(fila_prioridade, (novo_custo, nova_linha, nova_coluna))
        return distancias[linhas-1][colunas-1]