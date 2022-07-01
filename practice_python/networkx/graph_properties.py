import networkx as nx
import numpy as np
def basic_properties_graph(G):
    print(nx.info(G))
    print(f"Diameter of the graph {nx.diameter(G)}")
    print(f"Average shortest path length {nx.average_shortest_path_length(G)}")
    # lets find the average degree
    degree_values = [v for k, v in G.degree()]
    print(f"average degree of the graph {np.mean(degree_values)}")
    # No of connected components
    print(f"No of connected components {nx.number_connected_components(G)}")
    # Largest component size
    print(f"Largest component size {len(max(nx.connected_components(G), key=len))}")
    # average clustering coefficient
    print(f"average clustering coefficient {nx.average_clustering(G,)}")
    # Calculating the sum of all unique triangles
    print(f"sum of all unique triangles {sum(list(nx.triangles(G).values()))/3}")
    #deviding with 3 because each triangle is counted once for each node
    # Average number of triangles a node belongs to
    print(f"Average number of triangles a node belongs to {np.mean(list(nx.triangles(G).values()))}") 
    # for identifying isolate (degree zero) nodes
    print(f"No of isolates {nx.number_of_isolates(G)}")