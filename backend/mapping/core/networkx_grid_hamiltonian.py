import networkx as nx

def gen_grid(height, lenght):
    return nx.grid_2d_graph(height, lenght)

def hamiltonian_path_brute_force(graph_grid):
    F = [(graph_grid,[list(graph_grid.nodes())[0]])]
    n = graph_grid.number_of_nodes()
    while F:
        graph,path = F.pop()
        confs = []
        neighbors = (node for node in graph.neighbors(path[-1]) 
                        if node != path[-1]) 
        for neighbor in neighbors:
            conf_p = path[:]
            conf_p.append(neighbor)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            if len(p)==n:
                return p
            else:
                F.append((g,p))
    return F
