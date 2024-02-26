import pytest
from data_structures.graph import Graph, Vertex

def test_vertex_addition():
    graph = Graph()
    vertex = graph.add_node("A")
    assert isinstance(vertex, Vertex)
    assert vertex.value == "A"

def test_edge_addition():
    graph = Graph()
    start = graph.add_node("A")
    end = graph.add_node("B")
    graph.add_edge(start, end, 5)
    assert len(graph.get_neighbors(start)) == 1
    assert graph.get_neighbors(start)[0].vertex == end
    assert graph.get_neighbors(start)[0].weight == 5

def test_retrieving_all_vertices():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    vertices = graph.get_nodes()
    assert len(vertices) == 2
    assert set(vertex.value for vertex in vertices) == {"A", "B"}

def test_retrieving_neighbors():
    graph = Graph()
    start = graph.add_node("A")
    end = graph.add_node("B")
    graph.add_edge(start, end, 5)
    neighbors = graph.get_neighbors(start)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == end
    assert neighbors[0].weight == 5

def test_neighbors_with_weights():
    graph = Graph()
    start = graph.add_node("A")
    end = graph.add_node("B")
    graph.add_edge(start, end, 10)
    neighbors = graph.get_neighbors(start)
    assert neighbors[0].weight == 10

def test_graph_size():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    assert len(graph.get_nodes()) == 2

def test_single_vertex_edge_graph():
    graph = Graph()
    loop_vertex = graph.add_node("A")
    graph.add_edge(loop_vertex, loop_vertex, 1)
    assert len(graph.get_nodes()) == 1
    neighbors = graph.get_neighbors(loop_vertex)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == loop_vertex
    assert neighbors[0].weight == 1

# Optional: Run tests if this script is executed directly
if __name__ == "__main__":
    pytest.main()
