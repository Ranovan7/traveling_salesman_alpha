import random
import math
from tsp import City, Tour


def Euclidean_dist(a, b):
    '''
    Calculate euclidean distance of 2 given points
    1. a : first point, a city object
    2. b : second point, a city object
    --> returns eauclidean distance
    '''
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5


def TwoDtoOneD(n):
    '''
    Turn N x N array into 1D array
    1. n : dimension of the array
    --> returns list/array
    '''
    result = []
    for i in range(n):
        for k in range(n):
            if i == k or (k - 2 == i):
                continue
            result.append((k * n) + i)
    return result


def GenerateCity(cities):
    '''
    Make dictionary of City objects
    1. cities : coordinate data of cities
    --> returns dictionary of City objects
    '''
    result = {}
    for i, data in enumerate(cities):
        result[i] = City(data[0], data[1])
    return result


def SimulatedAnnealing(cities, temperature=1000, cooling_rate=1, start=None, end=None, log=False):
    '''
    Function to calculate TSP shortest routes using 2-opt method which check all possible edges swap before stopping calculation
    --> Parameters :
    1. cities : lists of cities coordinateof cities lists
    2. temperature : initial temperature, used to check if the change is acceptable
    3. cooling_step : cooling down the temperature to make it less likely to accept worse change over time
    4. start : id or index which the coordinate of the route starts
    5. end : id or index which the coordinate of the route ends
    --> Returns : x and y coordinates of cities in order
    - note :-more temperature means the worse alternative solution will be accepted
            -the higher the cooling rate the faster the temperature to go down, the more worse alternative will be rejected
    '''
    # Checking Errors on inputs/parameters
    if start == end:
        print("Error : start point must not be the same as end point!")
        print("Returning None, might make errors when result is used immediatly")
        return None
    city_number = len(cities)
    init_temp = round(temperature)
    temperature = round(temperature, 4)
    if start is None:
        start_point = random.randrange(city_number)
    else:
        start_point = start

    # Make JSON format of the cities
    city_data = GenerateCity(cities)

    # Generate Random Initial Tour
    if end is None:
        tail = 1
        tour = random.sample(range(city_number), city_number)
    else:
        tail = 0
        tour = [start]
        temp = random.sample(range(city_number), city_number)
        temp.remove(start)
        temp.remove(end)
        tour.extend(temp)
        tour.append(end)

    # Updating cities data to include connection to each city
    for i, num in enumerate(tour):
        city_data[num].add_connection(tour[(i - 1) % len(tour)], tour[(i + 1) % len(tour)])

    # Applying 2-Opt to get better routes
    counter = 0
    success = 0
    edges_set = TwoDtoOneD(city_number)
    checked = []

    if log is True:
        # Logging
        print("Traveling Salesman Route using Simulated Annealing")
        print("Number of Cities/Points :", city_number)
        print("Doing 2-Opt Operation...")

    while True:
        if len(edges_set) == 0:
            break
        # picking 2 edges randomly
        edge_pair = random.choice(edges_set)
        i = edge_pair % city_number
        k = edge_pair // city_number
        # pick the point that will be swapped
        i2 = city_data[i].back
        k2 = city_data[k].front

        # if start and end have value, ignore the possible start-end edge swaps
        if end is not None:
            if (k == start and k2 == end) or (k == end and k2 == start) or (i == start and i2 == end) or (i == end and i2 == start):
                edges_set.remove(edge_pair)
                checked.append(edge_pair)
                continue

        # check if 2 edges only have 3 point or not (the edges are not separate)
        if k2 == i or i2 == k:
            edges_set.remove(edge_pair)
            checked.append(edge_pair)
            continue

        # Calculate Old and New tour distance difference
        original = Euclidean_dist(city_data[i], city_data[i2])
        original += Euclidean_dist(city_data[k], city_data[k2])
        new_swap = Euclidean_dist(city_data[i], city_data[k2])
        new_swap += Euclidean_dist(city_data[k], city_data[i2])

        # Calculate Acceptance Probability
        acc_prob = 0
        rand0_1 = 1
        if temperature > 0:
            error = round(original-new_swap)
            accept = min(error/temperature, 700)
            try:
                acc_prob = math.exp(accept)
            except OverflowError:
                print("Overflow Exception : math range error")
                print(f"-->accept = {accept}")
            rand0_1 = random.randrange(0, init_temp)/init_temp

        if new_swap < original or (temperature > 0 and acc_prob > rand0_1):
            # Changing Connection from the Original
            city_data[i].back = k2
            city_data[k].front = i2
            city_data[i2].front = k
            city_data[k2].back = i
            # Reverse the Loop/Flow of the i2 - k2 connection
            curr = k2
            while True:
                city_data[curr].swap_connection()
                if curr == i2:
                    break
                else:
                    curr = city_data[curr].back
            # reset num_fail or restore edges_set and clear checked
            success += 1
            edges_set.extend(checked)
            checked.clear()
            if temperature > 0:
                temperature -= cooling_rate
                temperature = round(temperature, 4)
            # if success % 100 == 0:
            #     print("-->log:'{} Successful Edges Swapped'".format(success))
        else:
            edges_set.remove(edge_pair)
            checked.append(edge_pair)
        # Logging for information during execution
        counter += 1
        if log is True and counter % 100000 == 0:
            print("At {} 2-Opt Operation...".format(counter))

    if log is True:
        print("Number of 2-Opt Operation : ", counter)
        print("Number of Successful 2-Opt Operation : ", success)

    # Setting up the data to be visualized a.k.a making tourout of city data
    x = [city_data[start_point].x]
    y = [city_data[start_point].y]
    final_tour = [start_point]
    current = start_point
    while len(final_tour) < city_number + tail:
        new_point = city_data[current].back
        x.append(city_data[new_point].x)
        y.append(city_data[new_point].y)
        final_tour.append(new_point)
        current = new_point

    # Preparing to return the results
    route_distance = 0
    curr = start_point
    for city in final_tour[1:len(final_tour)]:
        route_distance += Euclidean_dist(city_data[city], city_data[curr])
        curr = city

    if log is True:
        print(f"Finished Temperature = {round(temperature, 4)}")
        print(f"Distance Result = {route_distance}")
        print()
    return Tour(x, y, final_tour, route_distance)
