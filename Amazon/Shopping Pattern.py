def getMinScore(products_nodes, products_from, products_to):
    len_edge = len(products_from)
    edge = {}
    sum = []
    for node in range(products_nodes):
        edge[node+1] = []
    for i in range(len_edge):
        edge[products_from[i]].append(products_to[i])
        edge[products_to[i]].append(products_from[i])
    for k,v in edge.items():
        score = 0
        if len(v) == 2:
            score = 2 + len(set(edge[v[0]])) + len(set(edge[v[1]])) - 6
            sum.append(score)
    if not sum:
        return -1 
    else:
        return min(sum)

products_from = [1,2,2,3,4,5]
products_to = [2,4,5,5,5,6]

print(getMinScore(6,products_from,products_to))

        