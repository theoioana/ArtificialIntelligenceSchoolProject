from RomaniaMapBuild import *

from queue import PriorityQueue

def dijsktra(initial, destination):
    """ This function calculates the shortest cost path from a source city to all the others city in romania_map. 
        The dictionary romania_map represents the adjaency list of the graph on which Dikjstra algorithm will run.
        The dictionary d represents the distances from source to all the other cities. In the end, the distance from 
        source to the destination will be returned. """
    
    distances = {}

    for i in city_list:
        distances[i.state] = 10000000000000

    distances[initial.state] = 0

    q = PriorityQueue()

    q.put( (0, initial.state) )
    
    while q.empty() == False :
        current = q.get()
        current_city = current[1]
        for neighbour in romania_map[current_city].keys():
            if distances[neighbour] > (distances[current_city] + romania_map[current_city][neighbour]):
                distances[neighbour] = distances[current_city] + romania_map[current_city][neighbour]
                q.put( (distances[neighbour], neighbour) )
   
    return distances[destination.state]

def test_function(cost_astar, start, destination):
    """ The test_function is testing if the minimum cost provided by Dikjstra (uninformed searching strategy) 
        is identical with the cost provided by the A* algorithm (informed searching strategy). Performing the two 
        searching strategies on the same graph, with the same input, and both providing the same miminimun path cost, 
        proves that the problem abordation is correct."""
    
    return cost_astar == dijsktra(start, destination)