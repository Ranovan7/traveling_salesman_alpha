# traveling_salesman_alpha
Trying simulated annealing method to find shortest path in traveling salesman problem

Always fascinated by traveling salesman problem but only just now understand (one of) the method used in dealing with it.

- using 100 randomized city sample, got around 3 secs average execution time per Simulated Annealing, will be faster if the sample is smaller but the increase in execution time on bigger sample can be felt so much (i don't know how to put it, i'll update if i got the correct term)

- making this just as a fun project as i take TSP challenge in kaggle annual comp and also want to populate my github XP

- hope it can be an interesting read, if anyone is reading, if any.

Function :
1. SimulatedAnnealing
- Params :  
            a. cities : lists of cities coordinateof cities lists
            b. temperature : initial temperature, used to check if the change is acceptable
            c. cooling_step : cooling down the temperature to make it less likely to accept worse change over time
            d. start : id or index which the coordinate of the route starts
            e. end : id or index which the coordinate of the route ends
            f. log : if true will show the logging of the process of this function
- Returns : x and y coordinates of cities in order
