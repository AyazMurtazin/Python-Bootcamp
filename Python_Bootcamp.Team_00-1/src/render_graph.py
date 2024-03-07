import networkx as nx
import json
import matplotlib.pyplot as plt

WIKI_FILE = "wiki.json"


def parse_graph_source():
    with open(WIKI_FILE) as graph_json:
        return json.load(graph_json)


graph = parse_graph_source()
G = nx.DiGraph(graph, directed=True)
node_sizes = [G.in_degree(node) * 200 for node in G.nodes()]
# nx.draw(G, with_labels=True, font_weight='bold')
nx.draw(G, with_labels=True, font_weight='bold', node_size=node_sizes)
plt.savefig("wiki_graph.png")
plt.show()
