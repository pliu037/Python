# https://projecteuler.net/problem=107

import re
import heapq


def get_graph():
    graph = {}
    node_id = 1
    f = open('C:/Users/Peng/Desktop/data.txt', 'r')
    line = f.readline().strip()
    while line != '':
        line_parsed = re.split(',', line)
        for i, value in enumerate(line_parsed):
            if value != '-':
                if node_id not in graph:
                    graph[node_id] = []
                graph[node_id].append(tuple([i + 1, int(value)]))
        node_id += 1
        line = f.readline().strip()
    f.close()
    return graph


def get_max_savings():
    graph = get_graph()
    in_set = {1}
    frontier_edges = []
    sum_included_edge_weight = 0
    sum_not_included_edge_weight = 0
    for node_id, edge_weight in graph[1]:
        heapq.heappush(frontier_edges, tuple([edge_weight, node_id]))
    while len(in_set) < len(graph):
        edge_weight, node_id = heapq.heappop(frontier_edges)
        sum_included_edge_weight += edge_weight
        if node_id not in in_set:
            in_set.add(node_id)
            for edge_node_id, edge_edge_weight in graph[node_id]:
                if edge_node_id not in in_set:
                    heapq.heappush(frontier_edges, tuple([edge_edge_weight, edge_node_id]))
                else:
                    sum_not_included_edge_weight += edge_edge_weight
        else:
            sum_not_included_edge_weight += edge_weight
    return sum_not_included_edge_weight - sum_included_edge_weight


print get_max_savings()
