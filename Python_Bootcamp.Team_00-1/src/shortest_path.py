import json
import argparse

WIKI_FILE = "wiki.json"
DEFAULT_FROM = "Wikipedia:Global actions"
DEFAULT_TO = "Wikipedia:Very short featured articles"


class DijsktraClass:

    def __init__(self):
        self.args = None
        self.graph_source = WIKI_FILE
        self.graph = None

    def solution(self):
        self.__parse_arguments()
        self.__parse_graph_source()
        if self.args.non_directed:
            self.__make_graph_non_directed()
        path = self.__alg()
        if path is None:
            print('Path not found')
        else:
            if self.args.v:
                print(" -> ".join(path))
            print(len(path))

    def __parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--from",
            dest="frm",
            type=str,
            default=DEFAULT_FROM,
            help='From')
        parser.add_argument(
            "--to",
            type=str,
            default=DEFAULT_TO,
            help='TO')

        parser.add_argument(
            "--non-directed",
            default=False,
            action="store_true",
            help='--non-directed')
        parser.add_argument(
            "-v",
            default=False,
            action="store_true",
            help='--non-directed')
        self.args = parser.parse_args()

    def __parse_graph_source(self):
        with open(self.graph_source) as graph_json:
            self.graph = json.load(graph_json)

    def __make_graph_non_directed(self):
        new_graph = self.graph.copy()
        for i in self.graph:
            for j in self.graph[i]:
                if j not in self.graph:
                    new_graph[j] = [i]
                else:
                    if i not in self.graph[j]:
                        new_graph[j].append(i)
        self.graph = new_graph

    def __alg(self):
        initial = self.args.frm
        end = self.args.to
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            try:
                destinations = self.graph[current_node]
            except:
                destinations = []
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = 1 + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return None
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        path = path[::-1]
        return path


def main():
    d = DijsktraClass()
    d.solution()


if __name__ == "__main__":
    main()
