from utils import Node

""" This module contains the data structures containing data about the Romania map. 
    These data structures are used globally in the application as the Romania map data
    is constant. More precisely, contains the following: a list with unique occurances of
    all the cities, a dictionary that represents the adjaency list of the graph represented
    by the links between the cities from Romania with the correspondent costys, and a dictionary 
    with the coordinates of every city. Node instances of the cities are created for further 
    implementation simplicity. """

global Sibiu, Arad, Bucharest, Craiova, Drobeta, Eforie, Fagaras, Giurgiu, Hirsova, Iasi, Lugoj, Mehadia, Neamt, Oradea, Pitesti, Rimnicu, Timisoara, Urziceni, Vaslui,  Zerind

Sibiu = Node("Sibiu")
Arad = Node("Arad")
Bucharest = Node("Bucharest")
Craiova = Node("Craiova")
Drobeta = Node("Drobeta")
Eforie = Node("Eforie")
Fagaras = Node("Fagaras")
Giurgiu = Node("Giurgiu")
Hirsova = Node("Hirsova")
Iasi = Node("Iasi")
Lugoj = Node("Lugoj")
Mehadia = Node("Mehadia")
Neamt = Node("Neamt")
Oradea = Node("Oradea")
Pitesti = Node("Pitesti")
Rimnicu = Node("Rimnicu")
Timisoara = Node("Timisoara")
Urziceni = Node("Urziceni")
Vaslui = Node("Vaslui")
Zerind = Node("Zerind")

city_list = [Sibiu, Arad, Bucharest, Craiova, Drobeta, Eforie, Fagaras, Giurgiu, Hirsova, Iasi, Lugoj, Mehadia, Neamt, Oradea, Pitesti, Rimnicu, Timisoara, Urziceni, Vaslui,  Zerind]

romania_map = {
    "Arad": {"Zerind" :75, "Sibiu":140, "Timisoara":118},
    "Bucharest": {"Urziceni" :85, "Pitesti":101, "Giurgiu":90, "Fagaras":211},
    "Craiova":{"Drobeta":120, "Rimnicu":146, "Pitesti":138},
    "Drobeta" :{"Mehadia":75, "Craiova": 120},
    "Eforie": {"Hirsova":86},
    "Fagaras": {"Sibiu":99, "Bucharest": 211},
    "Hirsova": {"Urziceni":98, "Eforie" : 86},
    "Iasi": {"Vaslui":92, "Neamt":87},
    "Lugoj": {"Timisoara":111, "Mehadia":70},
    "Mehadia" : {"Drobeta":75, "Lugoj":70},
    "Neamt" : {"Iasi":87},
    "Oradea": {"Zerind":71, "Sibiu":151},
    "Pitesti": {"Rimnicu":97, "Craiova" : 138, "Bucharest" : 101 },
    "Rimnicu": {"Sibiu":80, "Craiova" : 146, "Pitesti" : 97},
    "Sibiu" : {"Arad":140, "Oradea" : 151, "Fagaras":99, "Rimnicu" : 80},
    "Timisoara" : {"Arad":118, "Lugoj":111},
    "Urziceni": {"Vaslui":142, "Bucharest" : 85, "Hirsova" : 98},
    "Vaslui" : {"Urziceni":142, "Iasi":92},
    "Zerind" : {"Arad":75, "Oradea":71},
    "Giurgiu" : {"Bucharest" : 90 }
    }

romania_map_coordinates = {
    "Arad" : (91, 492), "Bucharest" : (400, 327), "Craiova" : (253, 288),
    "Drobeta" : (165, 299), "Eforie" : (562, 293), "Fagaras" : (305, 449),
    "Giurgiu" : (375, 270), "Hirsova" : (534, 350), "Iasi" : (473, 506),
    "Lugoj" : (165, 379), "Mehadia" : (168, 339), "Neamt" : (406, 537),
    "Oradea" : (131, 571), "Pitesti" : (320, 368), "Rimnicu" : (233, 410),
    "Sibiu" : (207, 457), "Timisoara" : (94, 410), "Urziceni" : (456, 350),
    "Vaslui" : (509, 444), "Zerind" :(108, 531)}
