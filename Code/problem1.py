from utils import *
from RomaniaMapBuild import *

class FriendsMeetingProblem(Problem):

    """The problem of finding the shortest route from a source to a destination
        in a graph can also be interpreted as the problem of searching a graph 
        from one node to another."""

    def __init__(self, initial_position, goal_position):
        Problem.__init__(self, initial_position.state, goal_position.state)

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        possible_actions = []

        for x in romania_map[A].keys():
            possible_actions.append(x)
 
        return possible_actions

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B):
        """ The path cost is the cost so far adde to the cost required
           to reach city B from A, cost that is given by the adjaency list 
           that also contains the costs of edges. """
        return cost_so_far + (romania_map[A][B])

    def find_min_edge(self, current):
        """Find minimum value of edges."""
        m = infinity
        for d in romania_map[current].values():
            local_min = min(d.values())
            m = min(m, local_min)

        return m

    def h(self, node):
        """h function is straight-line in the plane distance from a node's state to goal.
           This distance is represented by the ceiled euclidia distance in xoy plane. 
           The coordinates in the plane xoy are given by romania_map_coordinates dictioanry. """

        return ceil( sqrt( pow( (romania_map_coordinates[node.state][0] - romania_map_coordinates[self.goal][0] ), 2 ) + pow( (romania_map_coordinates[node.state][1] - romania_map_coordinates[self.goal][1] ) , 2 ) ) )

