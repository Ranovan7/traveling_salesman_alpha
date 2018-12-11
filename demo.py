from simulated_annealing import SimulatedAnnealing
import matplotlib.pyplot as plt
import random
import time


'''
This file just exist to demo the simulated annealing function
'''
# Some Important Parameters
recurse = 10
radiusX = 1000
radiusY = 1000
city_number = 100

# Generate Random City Coordinate
cities = [(random.randrange(radiusX), random.randrange(radiusY)) for x in range(city_number)]
x0 = []
y0 = []
for data in cities:
    x0.append(data[0])
    y0.append(data[1])
plt.figure(0)
plt.scatter(x0, y0, marker='x')
plt.title("Initial Points")

'''
Using the methods and iterate it multiple times to get the best result
'''
best_result = None
for i in range(recurse):
    start = time.time()
    tour = SimulatedAnnealing(cities, temperature=2000, cooling_rate=0.3,
                              start=0)
    print(f"Simulated Annealing {i+1} Execution Time {time.time() - start} seconds")
    print(f"Simulated Annealing {i+1} distance : {tour.distance}")
    print()
    if best_result is None:
        best_result = tour
        continue
    if tour.distance < best_result.distance:
        best_result.set_attributes(tour)

print(f"Simulated Annealing Best Result distance : {best_result.distance}")

'''Drawing the Visualization'''
plt.figure(1)
plt.plot(best_result.xList, best_result.yList, 'xb-')
plt.title("Traveling Salesman Problem with Simulated Annealing")
plt.show()
