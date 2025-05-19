//Algoritmos e Estrutura de Dados II
//Vitória Marca Santa Lucia - 23200577

#include <stdio.h>
#include <limits.h>

#define MAX_VERTICES 20
#define INF INT_MAX

int ler_num_vertices() {
    int n;
    do {
        printf("Quantidade de vértices (1 a %d): ", MAX_VERTICES);
        scanf("%d", &n);
    } while (n < 1 || n > MAX_VERTICES);
    return n;
}

void ler_matriz(int adj[][MAX_VERTICES], int n) {
    printf("\nDigite a matriz de adjacência (use -1 para ausência de aresta):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int peso;
            printf("Peso de %d para %d: ", i + 1, j + 1);
            scanf("%d", &peso);
            adj[i][j] = (peso >= 0 ? peso : INF);
        }
    }
}

int ler_vertice(const char *rotulo, int n) {
    int v;
    do {
        printf("%s (1 a %d): ", rotulo, n);
        scanf("%d", &v);
    } while (v < 1 || v > n);
    return v - 1;
}


void dijkstra(int adj[][MAX_VERTICES], int n, int origem, int dist[MAX_VERTICES],
              int prev[MAX_VERTICES]) {
    int visited[MAX_VERTICES] = {0};

    for (int i = 0; i < n; i++) {
        dist[i] = adj[origem][i];
        prev[i] = (adj[origem][i] < INF && i != origem) ? origem : -1;
        visited[i] = 0;
    }

    dist[origem] = 0;
    visited[origem] = 1;

    
    for (int count = 1; count < n; count++) {
        int u = -1, min_dist = INF;

        for (int i = 0; i < n; i++) {
            if (!visited[i] && dist[i] < min_dist) {
                min_dist = dist[i];
                u = i;
            }
        }

        if (u == -1) break;
        visited[u] = 1;

        for (int v = 0; v < n; v++) {

            if (!visited[v] && adj[u][v] < INF) {
                int alt = dist[u] + adj[u][v];

                if (alt < dist[v]) {
                    dist[v] = alt;
                    prev[v] = u;
                }
            }
        }
    }
}

void imprimir_caminho(int prev[MAX_VERTICES], int origem, int destino) {
    if (prev[destino] == -1 && destino != origem) {
        printf("Não existe caminho de %d para %d.\n", origem + 1, destino + 1);
        return;
    }

    int stack[MAX_VERTICES], topo = 0, u = destino;
    while (u != -1) {
        stack[topo++] = u;
        u = prev[u];
    }

    printf("Caminho: ");
    for (int i = topo - 1; i >= 0; i--) {
        printf("%d", stack[i] + 1);
        if (i > 0) printf(" -> ");
    }
    printf("\n");
}

int main() {
    int adj[MAX_VERTICES][MAX_VERTICES];
    int dist[MAX_VERTICES], prev[MAX_VERTICES];

    int n = ler_num_vertices();
    ler_matriz(adj, n);

    int origem  = ler_vertice("Vértice de origem", n);
    int destino = ler_vertice("Vértice de destino", n);

    dijkstra(adj, n, origem, dist, prev);

    if (dist[destino] == INF) {
        printf("\nNão existe caminho de %d para %d.\n",
               origem + 1, destino + 1);
    } else {
        printf("\nMenor distância de %d para %d: %d\n",
               origem + 1, destino + 1, dist[destino]);
        imprimir_caminho(prev, origem, destino);
    }

    return 0;
}
