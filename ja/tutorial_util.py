#!/usr/bin/env python
# coding: utf-8

from graphillion import GraphSet
from graphviz import Digraph
import networkx as nx
import json
import matplotlib.pyplot as plt
from IPython.display import Image

def zdd_size(graph_set):
    zdd = dump2zdd(graph_set.dumps().split("\n"))
    return len(zdd)


def draw_zdd(graph_set, universe=None):
    if not universe:
        universe = GraphSet.universe()
    zdd = dump2zdd(graph_set.dumps().split("\n"))

    return draw(zdd, universe)

def draw(zdd, labels):
    dot_str_lines = []
    dot_str_lines.append("digraph top {")
    dot_str_lines.append('node[ colorscheme = "rdylgn11", color = 3];')

    dot = Digraph()

    same_label_nodes = {}
    for nid in zdd:
        vals = zdd[nid]
        label = vals['label']
        lo = vals['lo']
        hi = vals['hi']
        if label not in same_label_nodes:
            same_label_nodes[label] = []
        same_label_nodes[label].append(nid)
        dot.node(nid, str(labels[int(label)-1]))
        dot.edge(nid, lo, style='dashed')
        dot.edge(nid, hi, style='solid')

    dot.node('T', '1', shape='square')
    dot.node('B', '0', shape='square')
    for labels in same_label_nodes.values():
        with dot.subgraph() as c:
            c.body.append("{rank= same;" + "; ".join(labels) + ";}")
    return dot

def dump2zdd(arr):
    nodes = {}

    for elem in arr:
        elems = elem.split()
        if len(elems) != 4: 
            continue
        nid, label, lo, hi  = elems
        nodes[nid] = {'label': label, 'lo': lo, 'hi': hi}

    return nodes

def _encode_digit(val):
    if isinstance(val, int):
        return '_int' + str(val)
    return val
    
def _decode_digit(val):
    if isinstance(val, str) and val.startswith('_int'):
        return int(val[4:])
    return val


def _graph2nx_layout(graph):
    dot = Digraph()
    for u, v in graph.edges:
        u = _encode_digit(u)
        v = _encode_digit(v)
        dot.edge(u, v)
    json_obj = json.loads(dot.pipe(format='json'))
    positions = {}
    for node in json_obj['objects']:
        name = _decode_digit(node['name'])
        pos_pair = tuple(float(x) for x in  node['pos'].split(','))
        positions[name] = pos_pair

    return positions

def draw_universe(universe=None):
    draw_subgraph(None, universe)



def draw_subgraph(subgraph=None, universe=None):
    if not universe:
        universe = GraphSet.universe()
    g = nx.Graph(sorted(universe))
    
    if not subgraph:
        subgraph = set([])
    else:
        subgraph = set(subgraph)

    pos = _graph2nx_layout(g)
    nx.draw_networkx_nodes(g, pos, node_color='#FFFFFF', edgecolors='#000000')
    edge_weights = []
    edge_colors = []
    for edge in g.edges():
        if edge in subgraph or (edge[1], edge[0]) in subgraph:
            edge_weights.append(5)
            edge_colors.append('#FF0000')
        else:
            edge_weights.append(1)
            edge_colors.append('#000000')


    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos, edge_color=edge_colors, width=edge_weights)

    plt.show()
