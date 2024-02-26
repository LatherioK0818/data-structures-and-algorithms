class Vertex:
    """
    A class to represent a vertex in a graph.
    """
    def __init__(self, value):
        self.value = value

class Edge:
    """
    A class to represent an edge in a graph.
    It stores the target vertex and the weight of the edge.
    """
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    """
    A Graph class to represent a graph using an adjacency list.
    """
    def __init__(self):
        self.adj_list = {}  # Key: Vertex object, Value: List of Edge objects

    def add_node(self, value):
        """
        Add a vertex to the graph.
        :param value: The value of the node.
        :return: The Vertex object for the node.
        """
        if value not in self.adj_list:
            vertex = Vertex(value)
            self.adj_list[vertex] = []
            return vertex

    def add_edge(self, start, end, weight=1, bidirectional=True):
        """
        Add an edge between two vertices.
        :param start: The start vertex object.
        :param end: The end vertex object.
        :param weight: The weight of the edge.
        :param bidirectional: If True, adds an edge back from end to start as well.
        """
        if start not in self.adj_list:
            self.add_node(start.value)
        if end not in self.adj_list:
            self.add_node(end.value)

        self.adj_list[start].append(Edge(end, weight))
        if bidirectional:
            self.adj_list[end].append(Edge(start, weight))

    def get_nodes(self):
        """
        Return all nodes in the graph.
        """
        return [vertex.value for vertex in self.adj_list]

    def get_neighbors(self, vertex):
        """
        Return all neighbors of a given vertex along with the edge weights.
        :param vertex: The vertex object.
        :return: A list of tuples (neighbor_vertex_value, weight).
        """
        return [(edge.vertex.value, edge.weight) for edge in self.adj_list[vertex]]

    def size(self):
        """
        Return the number of vertices in the graph.
        """
        return len(self.adj_list)

    def display(self):
        """
        Display the graph's adjacency list with edge weights.
        """
        for vertex, edges in self.adj_list.items():
            edge_descriptions = ', '.join([f"({edge.vertex.value}, {edge.weight})" for edge in edges])
            print(f"{vertex.value}: [{edge_descriptions}]")
