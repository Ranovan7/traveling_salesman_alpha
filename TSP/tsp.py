
class City:
    '''
    City object
    1. x : x coordinate of the city
    2. y : y coordinate of the city
    3. front : connection in the front of the city
    4. back : connection in the back of the city
    '''
    front = None
    back = None

    def __init__(self, x, y):
        '''Initialize the coordinate of the city'''
        self.x = x
        self.y = y

    def add_connection(self, front, back):
        '''Add Connection to the city'''
        self.front = front
        self.back = back

    def swap_connection(self):
        '''Swap the Connection to the city'''
        self.front, self.back = self.back, self.front


class Tour:
    '''
    City object
    1. xList : list of x coordinate of the tour
    2. yList : list of y coordinate of the tour
    3. tour : list of cities in order
    4. distance : total distance traveled
    '''

    def __init__(self, xList, yList, tour, distance):
        '''Initialize the information about the tour'''
        self.xList = xList
        self.yList = yList
        self.tour = tour
        self.distance = distance

    def set_attributes(self, other):
        '''Set the object attributes to match other object attributes'''
        self.xList = other.xList
        self.yList = other.yList
        self.tour = other.tour
        self.distance = other.distance
