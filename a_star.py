import heapq

def heuristica_manhattan(pos_atual, pos_tesouro):
    return abs(pos_atual[0] - pos_tesouro[0]) + abs(pos_atual[1] - pos_tesouro[1])
    
def busca_a_estrela(grid, pos_inicial, pos_tesouro):
    linhas, colunas = len(grid), len(grid[0])
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visitados = set()
    fila = [(0 + heuristica_manhattan(pos_inicial, pos_tesouro), 0, pos_inicial, [pos_inicial])]

    while fila:
        _, custo, atual, caminho = heapq.heappop(fila)
        if atual in visitados:
            continue
        visitados.add(atual)

        if atual == pos_tesouro:
            return caminho

        x, y = atual
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and grid[nx][ny] != '#':
                novo_custo = custo + (5 if grid[nx][ny] == 'L' else 1)
                heapq.heappush(fila, (novo_custo + heuristica_manhattan((nx, ny), pos_tesouro), novo_custo, (nx, ny), caminho + [(nx, ny)]))

    return []
