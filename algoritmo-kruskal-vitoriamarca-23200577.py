# Algoritmos e Estrutura de Dados II
# Vitória Marca Santa Lucia - 23200755

def algoritmo_kruskal(num_vertices, arestas):
    pai = list(range(num_vertices))
    rank = [0] * num_vertices

    def encontrar_conjunto(i):
        if pai[i] == i:
            return i
        pai[i] = encontrar_conjunto(pai[i])
        return pai[i]
    
    def unir_conjuntos(i, j):
        raiz_i = encontrar_conjunto(i)
        raiz_j = encontrar_conjunto(j)

        if raiz_i != raiz_j:
            if rank[raiz_i] < rank[raiz_j]:
                pai[raiz_i] = raiz_j

            elif rank[raiz_i] > rank[raiz_j]:
                pai[raiz_j] = raiz_i

            else:
                pai[raiz_j] = raiz_i
                rank[raiz_i] += 1
            return True
        return False
    
    arestas_mst = []
    mst_custo_total = 0
    num_arestas_na_mst = 0

    arestas_ordenadas = sorted(arestas, key=lambda aresta: aresta[2])
    
    for u, v, peso in arestas_ordenadas:
        if unir_conjuntos(u, v):
            arestas_mst.append((u, v, peso))
            mst_custo_total += peso
            num_arestas_na_mst += 1
            if num_arestas_na_mst == num_vertices - 1:
                break

    if num_vertices > 0 and num_arestas_na_mst < num_vertices - 1:
        print("O grafo não é conexo. Não foi possível formar uma MST completa.")
    
    return arestas_mst, mst_custo_total
#######################################
# teste 1    
num_vertices = 9
arestas = [
    (0,1,4),(0,7,8),(1,2,8),(2,3,7),(3,4,9),(4,5,10),(5,6,2),(6,7,1),(2,7,11),
    (3,5,14),(2,5,4),(6,7,6),(2,8,2),(7,8,7)
]   

mst_resultado, custo_resultado = algoritmo_kruskal(num_vertices,arestas)

for u,v,peso_aresta in mst_resultado:
    print(f"aresta:{u} -- {v} Peso: {peso_aresta}")
print(f"Custo Total da Árvore Geradora Mínima: {custo_resultado}")

#teste 2
num_vertices_2 = 7
arestas_2 = [
    (0, 1, 7), (0, 3, 5),
    (1, 2, 8), (1, 3, 9), (1, 4, 7),
    (2, 4, 5),
    (3, 4, 15), (3, 5, 6),
    (4, 5, 8), (4, 6, 9),
    (5, 6, 11)
]    
mst_resultado_ex2, custo_total_ex2 = algoritmo_kruskal(num_vertices_2, arestas_2)
for u, v, peso_aresta in mst_resultado_ex2:
    print(f"Aresta: {u} -- {v}  Peso: {peso_aresta}")
print(f"Custo Total da Árvore Geradora Mínima: {custo_total_ex2}")