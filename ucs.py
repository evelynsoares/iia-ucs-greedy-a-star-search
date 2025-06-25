import heapq

def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
    linhas, colunas = len(grid), len(grid[0])
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Cima, Baixo, Esquerda, Direita

    visitados = set()
    fila = [(0, pos_inicial, [pos_inicial])]  # (custo acumulado, posição atual, caminho)

    while fila:
        custo, atual, caminho = heapq.heappop(fila)
        if atual in visitados:
            continue
        visitados.add(atual)

        # Se chegou ao tesouro
        if atual == pos_tesouro:
            return caminho

        x, y = atual
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and grid[nx][ny] != '#':  # Verifica limites e obstáculos
                novo_custo = custo + (5 if grid[nx][ny] == 'L' else 1)
                heapq.heappush(fila, (novo_custo, (nx, ny), caminho + [(nx, ny)]))

    return []  # Retorna vazio se não houver caminho
