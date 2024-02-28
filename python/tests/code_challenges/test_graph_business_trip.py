import pytest
from data_structures.graph import Graph  # Adjust the import statement based on your project structure
from code_challenges.graph_business_trip import direct_flights  # Adjust the import statement based on your project structure

@pytest.fixture
def setup_graph():
    graph = Graph()
    vertices = {}

    # Create vertices and store them in a dictionary for easy reference
    for city in ["Metroville", "Pandora", "Arendelle", "New Monstropolis", "Naboo", "Narnia"]:
        vertices[city] = graph.add_node(city)

    # Add edges based on the provided test cases
    graph.add_edge(vertices["Pandora"], vertices["Arendelle"], 150)
    graph.add_edge(vertices["Pandora"], vertices["Metroville"], 82)
    graph.add_edge(vertices["Metroville"], vertices["Arendelle"], 99)
    graph.add_edge(vertices["New Monstropolis"], vertices["Arendelle"], 42)
    graph.add_edge(vertices["New Monstropolis"], vertices["Metroville"], 105)
    graph.add_edge(vertices["New Monstropolis"], vertices["Naboo"], 73)
    graph.add_edge(vertices["Metroville"], vertices["Naboo"], 26)
    graph.add_edge(vertices["Metroville"], vertices["Narnia"], 37)
    graph.add_edge(vertices["Narnia"], vertices["Naboo"], 250)

    return graph, vertices

def test_add_edge(setup_graph):
    graph, vertices = setup_graph
    # Using the vertices from the fixture to ensure correct instances are referenced
    arendelle_neighbors = graph.get_neighbors(vertices["Arendelle"])
    assert ("Pandora", 150) in arendelle_neighbors
    assert ("Metroville", 99) in arendelle_neighbors
    assert ("New Monstropolis", 42) in arendelle_neighbors

def test_get_neighbors(setup_graph):
    graph, vertices = setup_graph
    metroville_neighbors = graph.get_neighbors(vertices["Metroville"])
    # Checking a few neighbors to ensure edges are correctly added
    assert ("Pandora", 82) in metroville_neighbors
    assert ("Arendelle", 99) in metroville_neighbors
    assert ("Naboo", 26) in metroville_neighbors

def test_direct_flights_possible(setup_graph):
    graph, _ = setup_graph
    # Direct flights test cases based on your requirements
    assert direct_flights(graph, ["Metroville", "Pandora"]) == (True, 82)
    assert direct_flights(graph, ["Arendelle", "New Monstropolis", "Naboo"]) == (True, 115)

def test_direct_flights_impossible(setup_graph):
    graph, _ = setup_graph
    # Test cases where direct flights should not be possible
    assert direct_flights(graph, ["Naboo", "Pandora"]) == (False, 0)
    assert direct_flights(graph, ["Narnia", "Arendelle", "Naboo"]) == (False, 0)
