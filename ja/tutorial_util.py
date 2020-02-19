#!/usr/bin/env python
# coding: utf-8

from graphillion import GraphSet, tutorial
import pygraphviz as pgv
import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import Image

def zdd_size(graph_set):
    zdd = dump2zdd(graph_set.dumps().split("\n"))
    return len(zdd)

def draw_zdd(graph_set, universe=GraphSet.universe()):
    zdd = dump2zdd(graph_set.dumps().split("\n"))

    return draw(zdd, universe)

def draw(zdd, labels):
    dot_str_lines = []
    dot_str_lines.append("digraph top {")
    dot_str_lines.append('node[ colorscheme = "rdylgn11", color = 3];')

    same_label_nodes = {}
    for nid in zdd:
        vals = zdd[nid]
        label = vals['label']
        lo = vals['lo']
        hi = vals['hi']
        if label not in same_label_nodes:
            same_label_nodes[label] = []
        same_label_nodes[label].append(nid)

        dot_str_lines.append(f'"{nid}" [label="{labels[int(label)-1]}"];')
        dot_str_lines.append(f'"{nid}" -> "{lo}" [style=dashed];')
        dot_str_lines.append(f'"{nid}" -> "{hi}" [style=solid];')

    for labels in same_label_nodes.values():
        dot_str_lines.append("{rank= same;" + "; ".join(labels) + ";}")
    dot_str_lines.append('"T" [shape=square, label="1"];')
    dot_str_lines.append('"B" [shape=square, label="0"];')

    dot_str_lines.append("{rank=same; T; B;}")
    dot_str_lines.append("}")
    dot_str = "\n".join(dot_str_lines)
    A = pgv.AGraph(dot_str)
    return Image(A.draw(format='png', prog='dot'))

def dump2zdd(arr):
    nodes = {}

    for elem in arr:
        elems = elem.split()
        if len(elems) != 4: 
            continue
        nid, label, lo, hi  = elems
        nodes[nid] = {'label': label, 'lo': lo, 'hi': hi}

    return nodes


def draw_subgraph(universe, subgraph=None):
    g = nx.Graph(sorted(universe))
    
    if not subgraph:
        subgraph = set([])
    else:
        subgraph = set(subgraph)

    pos = nx.nx_agraph.pygraphviz_layout(g, 'dot')
    nx.draw_networkx_nodes(g, pos, node_color='#FFFFFF', edgecolors='#000000')
    edge_weights = []
    edge_colors = []
    for edge in g.edges():
        if edge in subgraph:
            edge_weights.append(5)
            edge_colors.append('#FF0000')
        else:
            edge_weights.append(1)
            edge_colors.append('#000000')


    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos, edge_color=edge_colors, width=edge_weights)

    plt.show()
