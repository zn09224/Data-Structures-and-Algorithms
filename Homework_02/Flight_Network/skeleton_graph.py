import csv

def addVertices(G: dict, vertices: list):
    for i in vertices:
        G[i] = []

def addEdges(G: dict, edges: list):
    for edge in edges:
        origin, destination, weight = edge
        G[origin].append((destination, weight))       

def create_flight_network(filename: str, option: int):
    # Read data from the given file and convert in appropriate format:
    with open(filename) as f :
        lines = f.readlines()
    input = []
    for line in lines :
        line = line.strip() 
        tokens = line.split(",") 
        input.append(tokens)
    
    vertices = []
    duration_edges = []
    distance_edges = []
    
    for i in input[1:]:
        
        if i[0] not in vertices:
            vertices.append(i[0])       # First element in each line is a node
            
        duration_edges.append((i[0], i[1], int(i[2])))
        distance_edges.append((i[0], i[1], int(i[3])))
    
    G = {}      # Initializing the graph as G
    
    addVertices(G, vertices)        # Adding nodes to the graph
    
    if option == 1:
        addEdges(G, duration_edges)     # If option is 1, adding duration edges in our graph G
    else:
        addEdges(G, distance_edges)     # If option is 2, adding distance edges in our graph G
    
    return G
        

def get_flight_connections(graph: dict, city: str, option: str) -> list:
    connections = []
    
    if city not in graph.keys():        # Check if given city is not in the network
        return connections
    
    elif option == "o":         # For outbound connections
        for i in graph[city]:
            connections.append(i[0])
    
    elif option == "i":         # For inbound connections
        for k, v in graph.items():
            for i in v:
                if i[0] == city:
                    connections.append(k)
               
    return connections
        

def get_number_of_flight_connections(graph: dict, 
                                     city: str, 
                                     option: str) -> int:
    
    connections = 0         # Variable to store number of connections
    
    if city not in graph.keys():     # Check if given city is not in the network
        return connections
    
    elif option == "o":         # For outbound connections
        for i in graph[city]:
            connections += 1
    
    elif option == "i":         # For inbound connections
        for k, v in graph.items():
            for i in v:
                if i[0] == city:
                    connections += 1
    
    return connections

def get_flight_details(graph: dict, origin: str, destination: str) -> int:
    
    if origin not in graph.keys():          # Check if the origin is in the network
        return None
    
    weight = - 1           # Initializing weight (distance or duration) as -1
    
    for i in graph[origin]:         # Iterating over the neighbours of origin
        if i[0] == destination:
            weight = i[1]
    
    return weight
    

def add_flight(graph: dict, origin: str, destination: str, weight: int):
    
    if origin not in graph.keys():     # Check if the origin is in the network
        print(f"{origin} not accessed by the flight network.")
    
    elif destination not in graph.keys():       # Check if destination is in the network 
        print(f"{destination} not accessed by the flight network.")
    
    else:
        c = 0       # Variable which works as a flag i.e it will be updated if the connection already exists
        
        # Finding a connection if it exists already
        for i in range(len(graph[origin])):     
            if graph[origin][i][0] == destination:
                graph[origin][i] = (graph[origin][i][0], weight)        # Update weight of the connection
                c = 1
        
        if c == 0:          # Check if flag variable is the same i.e no connection exists already
            graph[origin].append((destination, weight))         # Add a new connection
                

def add_airport(graph: dict, city: str, destination: str, weight: int):
    
    if city in graph.keys():        #  Check if city is already in the connection
        print("Airport already exists.")
    
    else:
        addVertices(graph, [city])
        addEdges(graph, [(city, destination, weight)])
        

def get_secondary_flights(graph: dict, city: str):
    
    if city not in graph.keys():    # Check if the city is in the connection
        return None 
    
    secondary_connections = []         # Initializing list to store secondary connections
    
    for i in graph[city]:       # Iteration over neighbours of given city
        for j in graph[i[0]]:   # Iteration over neighbours of neighbours of given city
            if j[0] not in secondary_connections:
                secondary_connections.append(j[0])
    
    return secondary_connections

def counting_common_airports(graph: dict, cityA: str, cityB: str) -> int:
    
    list_A = []     # List  to store the neighbours of cityA
    for i in graph[cityA]:
        list_A.append(i[0])
    
    common = 0      # Variable to store the number of common airports
    
    for i in graph[cityB]:
        if i[0] in list_A:      # If neighbour of B is also the neighbour of A
            common += 1
    
    return common

def remove_flight(graph: dict, origin: str, destination: str):
    
    if origin not in graph.keys():      # Check if origin is in the network
        print(f"{origin} not accessed by the flight network.")
        return
    
    if destination not in graph.keys():     # Check if destination is in the network
        print(f"{destination} not accessed by the flight network.")
        return
    
    # Remove the connection from origin to destination if any:
    for i in graph[origin]:
        if i[0] == destination:
            graph[origin].remove(i)
    
    # Remove connection from destination to orirgin if any:
    for i in graph[destination]:
        if i[0] == origin:
            graph[destination].remove(i)
    

def remove_airport(graph: dict, city: str):
    
    if city not in graph.keys():        # Check if city is in the network
        print(f"{city} not accessed by the flight network.")
    
    else:
        for k, v in graph.items():
            for i in v:
                if i[0] == city:
                    v.remove(i)     # Removing the inbound edges of city
                    
        del graph[city]         # Removing the city from keys of graph


def DFS_all_routes(graph: dict,
                    origin: str, 
                    destination: str,
                    route: list, 
                    all_routes: list):
    
    if origin == destination:
        if route not in all_routes:         # Check if this route not already exists in all_routes
            all_routes.append(route)
        
    for i in graph[origin]:         # Iterating over the neighbours of current origin
        if i[0] not in route:
            temp_route = route.copy()       # Creating a copy of the current route
            temp_route.append(i[0])
            DFS_all_routes(graph, i[0], destination, temp_route, all_routes)    # Recursive call with neighbour of current origin as the origin, and the copy of the current route
             
    return all_routes


def find_all_routes(graph: dict, origin: str, destination: str):
    
    # Check if origin and destination are in the graph network
    if origin not in graph.keys() or destination not in graph.keys():     
        return None
    
    if origin == destination:       
        return []
        
    route = [origin]        # Initializing route list with first element as origin
    all_routes = []         # Initializing the list of all routes as empty list
     
    # Return list of all routes
    return DFS_all_routes(graph, origin, destination, route, all_routes) 


def DFS_layovers(graph: dict, origin: str, destination: str, 
                 route: list, 
                 layovers_lst: list):       # Function not required
    pass
        
        
def find_number_of_layovers(graph: dict, origin: str, destination: str):
    
    # Check if origin and destination are in the graph network
    if origin not in graph.keys() or destination not in graph.keys():
        return None
    
    if origin == destination:
        return []
    
    all_routes = find_all_routes(graph, origin, destination)    # List of all possible routes
    
    layovers = []       # Initializing the list of number of layovers
    
    for i in all_routes:
        layovers.append(len(i) - 2)     # Subtracting origin and destination because they are not layovers 
    
    layovers.sort()     
    return layovers

     

