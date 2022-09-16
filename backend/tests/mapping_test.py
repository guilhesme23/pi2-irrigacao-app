import networkx as nx
import networkx.algorithms.approximation as nx_app

from mapping.core.networkx_grid_route import gen_grid, complete_graph, irrigation_delimiter, flip_to_start_position, christofides_tsp_custom

def test_gen_grid():
    G = nx.grid_2d_graph(round(10/3), round(10/3))
    G.remove_node((0,1))
    G.remove_node((1,1))

    H = gen_grid(10, 10, [[0, 1], [1, 1], [1, 2]])

    assert G.nodes == H.nodes

def test_complete_graph():
    G = gen_grid(10, 10, [[0, 1], [1, 1], [1, 2]])
    H = G.copy()
    pos = {i: [a[0], a[1]] for i,a in enumerate(G.nodes)}

    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            dist = len(nx.shortest_path(H, tuple(pos[i]), tuple(pos[j]))) - 1
            G.add_edge((pos[i][0],pos[i][1]), (pos[j][0],pos[j][1]), weight=dist)
    
    I = complete_graph(H, H.copy())

    assert I.edges == G.edges

def test_irrigation_delimiter():
    G = gen_grid(10, 10, [[0, 1], [1, 1], [1, 2]])
    H = G.copy()
    cycle = irrigation_delimiter(H, nx_app.christofides(complete_graph(G, H), weight="weight"))

    assert cycle == [(0, 0), 'S', (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), 'S', (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]

def test_flip_to_start_position():
    cycle = [(0, 0), 'S', (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), 'S', (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]

    assert flip_to_start_position(cycle, (0,2)) == [(0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0), 'S', (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), 'S', (0, 2)]

def test_christofides_tsp_custom():
    G = gen_grid(10, 10, [[0, 1], [1, 1], [1, 2]])

    assert christofides_tsp_custom(G, (0,2)) == [(0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0), 'S', (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), 'S', (0, 2)]