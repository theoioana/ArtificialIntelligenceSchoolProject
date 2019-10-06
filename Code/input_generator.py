from RomaniaMapBuild import city_list
import random

def input_random_generator():
    """ The input generator rondomly shuffles the list with the cities from Romania, every city having a single occurence.
    Having the cities shuffled every time the function is called, the start cities for the friend A, respectively for the friend B,
    and the meeting point of the 2 friends can be chosed aribitrarly in the following way: the city that reaches position '0' will be
    the start city for friend A, the city that reaches position '1' will be the start city for friend B, and the city that reaches 
    position '2' will represent the meeting point. This data will be returned as a tuple""" 

    city_list_copy = city_list
    random.shuffle(city_list_copy)

    start1 = city_list_copy[0]
    start2 = city_list_copy[1]
    destination = city_list_copy[2]

    return (start1, start2, destination)



   
