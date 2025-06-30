# Algoritmos e Estrutura de Dados II
# Vitória Marca Santa Lucia - 23200755

def algoritmo_kruskal(num_vertices, arestas):
    #cada vértice é seu próprio pai, inicialmente
    pai = list(range(num_vertices))
    #inicializa o vetor rank apenas com zeros, para todos os vértices
    rank = [0] * num_vertices

    #encontra a raiz do conj. que i pertence
    def encontrar_conjunto(i):
        if pai[i] == i: #caso ele mesmo seja raiz, retorna 
            return i
        #se não, recursivamente encontra a raiz do conjunto
        pai[i] = encontrar_conjunto(pai[i])
        return pai[i]
    
    #função que une dois conjuntos
    def unir_conjuntos(i, j):
        raiz_i = encontrar_conjunto(i) #raiz de i
        raiz_j = encontrar_conjunto(j) #raiz de j

        if raiz_i != raiz_j: #só une caso as raízes estiverem em conjuntos diferentes
            
            #caso raiz_j seja mais profunda, então torna-se pai de raiz_i
            if rank[raiz_i] < rank[raiz_j]:
                pai[raiz_i] = raiz_j

            #se não, o contrário ocorre
            elif rank[raiz_i] > rank[raiz_j]:
                pai[raiz_j] = raiz_i
            
            #caso a profundidade seja a mesma, incrementa o rank
            else:
                pai[raiz_j] = raiz_i
                rank[raiz_i] += 1
            return True #teve união
        return False #caso não passe no if, já estavam no mesmo conjunto
    
    #lista que armazenará as arestas da mst
    arestas_mst = []
    #custo da mst
    mst_custo_total = 0
    #contador para verificar e controlar se temos n-1 arestas
    num_arestas_na_mst = 0

    #ordena cada aresta em ordem crescente por peso
    arestas_ordenadas = sorted(arestas, key=lambda aresta: aresta[2])
    
    #cada aresta é processada em ordem
    for u, v, peso in arestas_ordenadas:
        #se a aresta conecta dois conjuntos distintos
        if unir_conjuntos(u, v): #caso não tenha ciclos
            arestas_mst.append((u, v, peso)) #adiciona a aresta à mst
            mst_custo_total += peso #atualiza o custo total 
            num_arestas_na_mst += 1 #incrementa o contador de arestas
            if num_arestas_na_mst == num_vertices - 1: #caso todas tenham sido testadas
                break

    #se não foi possível conectar todos, o grafo não é conexo
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