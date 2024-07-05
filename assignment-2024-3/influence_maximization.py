import sys
import random
import networkx as nx
import numpy as np

def load_graph(filename):
    G = nx.DiGraph()
    with open(filename, 'r') as file:
        for line in file:
            u, v = line.strip().split()
            G.add_edge(int(u), int(v))
    return G

def greedy_algorithm(G, k, probability, mc):
    S = set()  # Seed nodes
    for _ in range(k):
        best_node = None
        best_spread = -1
        for node in G.nodes():
            if node in S:
                continue
            spread = average_spread(G, S | {node}, probability, mc)
            if spread > best_spread:
                best_spread = spread
                best_node = node
        S.add(best_node)
    return S
