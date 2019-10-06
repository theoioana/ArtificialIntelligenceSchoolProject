from input_generator import *
from OuputFormat import *
import time

#testcase

"""The problem input is formed by the start city of friend A, start city of friend B, and the meeting point of the 2 friends.
This input data is returned by the function 'input_random_generator'."""

input = input_random_generator()

city_friendA = input[0]
city_friendB = input[1]
meeting_point = input[2]

""" 'run_app' is the function that starts all the processes required for a correct solution based on the Input data given in the parameteres."""

t1 = time.time()
print("Running app start time: " + str(t1))
run_app(city_friendA, city_friendB, meeting_point)
t2 = time.time()
print("Running app end time: " + str(t2))
print("Time requiered to solve the problem: " + str(t2 - t1))


 
