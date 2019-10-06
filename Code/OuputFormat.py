from problem1 import FriendsMeetingProblem
from RomaniaMapBuild import *
from utils import *
from test_module import *

def output_route_analytics(path, cost):
    """ Output format function for printing the cities from the path and also the total cost of this path. """

    print("The shortest route is: ")
    print(path)
    print("The necessary time to reach the destination according to chosen route is: ")
    print(cost)

def output_correctitude_check(cost_astar, start, destination):
    """ Output format function for printing if the chosen path is the minimum cost path. """

    print("Checking if the chosen route is the shortest using Dikjstra.....")
    if test_function(cost_astar, start, destination) == 1:
        print("The chosen route is the shortest route possible!")
    else:
        print("The chosen route is NOT the shortest route possible!")
        

def output_time_waited(first_to_destination, second_to_destination,  time1, time2):
    """  Output format function for printing which friend arrived first and also how much he had to waith for the other friend. """
    print("\t\t\t === Time Analysis ===")
    difference = abs(time1 - time2)

    if difference == 0:
        print("The two friends arrived simoulatenously to the destionation! Great!")
    else:
        print(first_to_destination + " waited for " + second_to_destination + " for [" + str(difference) + "] units of time.")

def run_app(start_friend1, start_friend2, meeting_point) :

    """ Function that is lauching all the processes for an appropiate functionality of the application. 
        The function creates the necessary objects, then calls the A* search, and also all the necessary
        output functions. Also, this function contains an execution time analysis of the application.  """ 

    print("The two friends have to meet in " + meeting_point.state)

    friend1 = FriendsMeetingProblem(start_friend1, meeting_point)
    path1 = astar_search(friend1).solution()

    journey_time1 = 0
    
    past = start_friend1.state

    for i in path1:
        journey_time1 += romania_map[past][i]
        past = i

    print("\t\t\t === Friend A ===")
    print("First friend is leaving from " + start_friend1.state)
    output_route_analytics(path1, journey_time1)
    output_correctitude_check(journey_time1, start_friend1, meeting_point)

  
    friend2 = FriendsMeetingProblem(start_friend2, meeting_point)
    path2 = astar_search(friend2).solution()

    journey_time2 = 0
    
    past = start_friend2.state

    for i in path2:
        journey_time2 += romania_map[past][i]
        past = i

    print("\t\t\t === Friend B ===")
    print("The second friend is leaving from " + start_friend2.state)
    output_route_analytics(path2, journey_time2)
    output_correctitude_check(journey_time2, start_friend2, meeting_point)

    if journey_time1 < journey_time2:
        first_friend = "Friend A"
        second_friend = "Friend B"
    else:
        first_friend = "Friend B"
        second_friend = "Friend A"


    output_time_waited(first_friend, second_friend, journey_time1, journey_time2)

   


    