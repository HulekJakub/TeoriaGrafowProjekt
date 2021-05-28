import json
import math
from typing import List


class Edge:
    edge_index: int
    start_index: int
    end_index: int
    capacity: int
    current_flow: int
    reverse_index: int

    def __init__(self):
        self.current_flow = 0


class Node:
    node_index: int
    in_edges: List
    out_edges: List

    def __init__(self):
        self.in_edges = list()
        self.out_edges = list()


class Graph:
    nodes: List
    edges: List
    source: Node
    sink: Node
    original_edges: int

    def __init__(self):
        self.nodes = list()
        self.edges = list()
        self.source = Node()
        self.sink = Node()
        self.original_edges = 0

    def load_data(self):
        f = open('graph.json', )
        incidence_matrix = json.load(f)

        for i in range(len(incidence_matrix)):
            new_node = Node()
            self.nodes.append(new_node)
            new_node.node_index = i

        for i in range(len(incidence_matrix[0])):
            new_edge = Edge()
            self.edges.append(new_edge)
            new_edge.edge_index = i
            for j in range(len(incidence_matrix)):
                if incidence_matrix[j][i] > 0:
                    new_edge.capacity = incidence_matrix[j][i]
                    new_edge.start_index = j
                    self.nodes[j].out_edges.append(new_edge)
                if incidence_matrix[j][i] < 0:
                    new_edge.end_index = j
                    self.nodes[j].in_edges.append(new_edge)

        self.original_edges = len(self.edges)
        for i in range(self.original_edges):
            original_edge = self.edges[i]
            reverse_edge = Edge()
            reverse_edge.edge_index = original_edge.edge_index + self.original_edges
            reverse_edge.start_index = original_edge.end_index
            reverse_edge.end_index = original_edge.start_index
            reverse_edge.current_flow = original_edge.capacity
            reverse_edge.capacity = original_edge.capacity
            reverse_edge.reverse_index = original_edge.edge_index
            original_edge.reverse_index = reverse_edge.edge_index

            self.nodes[original_edge.end_index].out_edges.append(reverse_edge)
            self.nodes[original_edge.start_index].in_edges.append(reverse_edge)
            self.edges.append(reverse_edge)

        self.source = self.nodes[0]
        self.sink = self.nodes[-1]

    def bfs(self) -> List:
        path = [None] * len(self.nodes)
        queue = list()
        queue.append(self.source)

        while len(queue) > 0:
            current_node = queue.pop(0)
            for edge in current_node.out_edges:
                if path[edge.end_index] is None and edge.end_index != self.source.node_index\
                        and edge.capacity > edge.current_flow:
                    path[edge.end_index] = edge
                    queue.append(self.nodes[edge.end_index])

        return path

    def edmonds_karp(self) -> int:
        flow = 0
        path = self.bfs()
        while path[self.sink.node_index]:
            edge = path[self.sink.node_index]
            flow_increment = math.inf

            while edge is not None:
                flow_increment = min(flow_increment, edge.capacity - edge.current_flow)
                edge = path[edge.start_index]

            edge = path[self.sink.node_index]
            while edge is not None:
                edge.current_flow += flow_increment
                self.edges[edge.reverse_index].current_flow -= flow_increment
                edge = path[edge.start_index]
            flow += flow_increment
            path = self.bfs()

        return flow


graph = Graph()
graph.load_data()
print(graph.edmonds_karp())
