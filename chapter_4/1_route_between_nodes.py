import unittest

from data_structures.trees_and_graphs.directed_graph import Graph
from data_structures.stacks_and_queues.queue import Queue


def is_route_between_nodes(graph, id_a, id_b):
    """Check to see if there is a route between nodes with id a and id b, in a
    directed graph

    Uses 2 simultaneous breadth first searches from id a and id b

    Parameters
    ----------
    graph : Graph
        Directed graph to search
    id_a : any
        Id of node at one end of route we are trying to find. Must be hashable,
        so can be used as key in a dictionary.
    id_b : any
        Id of node at other end of route we are trying to find. Must be
        hashable, so can be used as key in a dictionary.
    """
    # Set up dict of nodes visited by search from node with id a, and b
    visited_by_a = {k: False for k in graph.nodes.keys()}
    visited_by_b = {k: False for k in graph.nodes.keys()}

    # Use Queue to store tuple: (id of node to visit, bool that is True if node
    # is part of node a's search, False if part of node b's search
    nodes_to_visit = Queue()

    # Mark starting nodes as visited, and add to queue
    visited_by_a[id_a] = True
    nodes_to_visit.add((id_a, True))
    visited_by_b[id_b] = True
    nodes_to_visit.add((id_b, False))

    # Keep visiting nodes until none left to visit (Queue empty)
    while not nodes_to_visit.is_empty():

        # Extract node at front of Queue
        current_node_id, is_on_search_a = nodes_to_visit.remove()
        current_node = graph.nodes[current_node_id]

        # Check through current_node's neighbours
        for node_id in current_node.neighbour_ids:

            # Ensure node not already visited by relevant search
            if is_on_search_a and not visited_by_a[node_id]:
                # Check if node has b's id
                if node_id == id_b:
                    return True
                # Mark node as visited and add to Queue
                visited_by_a[node_id] = True
                nodes_to_visit.add((node_id, is_on_search_a))
            else:
                # Check if node has a's id
                if current_node_id == id_a:
                    return True
                # Mark node as visited and add to Queue
                visited_by_b[node_id] = True
                nodes_to_visit.add((node_id, is_on_search_a))

    # If no match found after search completes, return False
    return False


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs

    def test_is_route_between_nodes(self):
        """Test operations of SetOfStacks class
        """

        # Initialise graph
        g = Graph()
        # Insert nodes
        node_ids = list('ABCDEFGHIJK')
        [g.insert(j, i) for i, j in enumerate(node_ids)]
        # Make connections
        connection_sources = [
            'A', 'A', 'A', 'B', 'C',
            'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'I'
        ]
        connection_destinations = [
            'B', 'C', 'H', 'E', 'B',
            'D', 'I', 'F', 'G', 'A',
            'E', 'J', 'K'
        ]
        [g.connect(x, y) for x, y in zip(
            connection_sources, connection_destinations
        )]

        # Test paths
        self.assertTrue(is_route_between_nodes(g, 'A', 'B'))
        self.assertTrue(is_route_between_nodes(g, 'A', 'F'))
        self.assertTrue(is_route_between_nodes(g, 'B', 'C'))
        self.assertFalse(is_route_between_nodes(g, 'J', 'K'))


if __name__ == '__main__':

    unittest.main()
