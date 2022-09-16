import networkx as nx
import networkx.algorithms.approximation as nx_app
import math

def gen_grid(widht, lenght, nodes_to_remove):
    square_side_meters = 3
    vertical_nodes = widht/square_side_meters
    horizontal_nodes = lenght/square_side_meters

    G = nx.grid_2d_graph(round(vertical_nodes), round(horizontal_nodes))
    H = G.copy()
    H = H.to_undirected()
    for node in nodes_to_remove:
        if H.has_node(tuple(node)):
            H.remove_node(tuple(node))
        sub_graphs = [H.subgraph(c).copy() for c in nx.connected_components(H)]
        if len(sub_graphs) > 1 or len(H.nodes) < 1:
            H = G.copy()
            H = H.to_undirected()
            continue
        if G.has_node(tuple(node)):
            G.remove_node(tuple(node))

    return G

def complete_graph(G, H):
    pos = {i: [a[0], a[1]] for i,a in enumerate(G.nodes)}

    #complete graph with weight as shortest path len
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            dist = len(nx.shortest_path(H, tuple(pos[i]), tuple(pos[j]))) - 1
            G.add_edge((pos[i][0],pos[i][1]), (pos[j][0],pos[j][1]), weight=dist)
    
    return G

def irrigation_delimiter(H, cycle):
    i=0
    while True:
        if i == len(cycle) - 1:
            break
        if math.dist(list(cycle[i]), list(cycle[i+1])) != 1:
            path = nx.shortest_path(H, cycle[i], cycle[i+1])[1:-1]
            cycle.insert(i+1, "S")
            i += 1
            for node in path:
                cycle.insert(i+1, node)
                i += 1
            cycle.insert(i+1, "S")
            i += 1
        i += 1
    return cycle

def flip_to_start_position(cycle, node_to_start):
    check = True
    node_to_start = tuple(node_to_start)
    for i, node in enumerate(cycle):
        if node == 'S':
            check = not check    
        if check == True and node == node_to_start:
            cycle = cycle[:-1]
            cycle_start = cycle[:i]
            cycle_end = cycle[i:]
            cycle_end.extend(cycle_start)
            cycle_end.append(node_to_start)
            break
    return cycle_end

def christofides_tsp_custom(G, node_to_start):
    H = G.copy()
    
    G = complete_graph(G, H)
    
    cycle = nx_app.christofides(G, weight="weight")

    cycle = irrigation_delimiter(H, cycle) 
    
    if tuple(node_to_start) == (0,0):
        return cycle
        
    cycle = flip_to_start_position(cycle, node_to_start)

    return cycle
    
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
