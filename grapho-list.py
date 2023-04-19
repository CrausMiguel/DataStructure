# Lista Adjacencia

lista_adj = {}
direcional = True


def main():
    linhas = open("grapho.txt", "r")
    count_linha = 0
    for linha in linhas:
        if count_linha == 0:
            vertices = linha.strip().split(",")
            numero_vertices = len(vertices)
            for i in range(0, numero_vertices):
                vertice = vertices[i]
                lista_adj[vertice] = []

        else:
            vertices = linha.strip().split("-")

            origem = vertices[0]
            destino = vertices[1]
            peso = vertices[2]

            aresta = {'destino': destino, 'peso': peso}
            lista_adj[origem].append(aresta)

        count_linha += 1
    print(lista_adj)


if __name__ == '__main__':
    main()
