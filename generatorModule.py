import random as rn
from faker import Faker

#variables

# Function that returns a random number between 10000000-99999999
# Time complexity: O(1)
# Memory complexity: O(1)
def randomId():
    return rn.randint(10000000, 99999999)

# Function that returns a random name using the Faker library
# type("name"): random first name
# type("lastName"): random last name
# type("country"): random country


def randomFaker(type):
    faker = Faker()
    if type == "name":
        # Time complexity: O(1)
        # Memory complexity: O(1)
        return faker.first_name_male()
    elif type == "lastName":
        # Time complexity: O(1)
        # Memory complexity: O(1)
        return faker.last_name()
    elif type == "country":
        # Time complexity: O(1)
        # Memory complexity: O(1)
        return faker.country()

# Function that returns a random number between 17 and 39 based on a defined probability of appearance

def randomAge():
    # Time complexity: O(1)
    # Memory complexity: O(1)
    ages = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
    # Time complexity: O(1) 
    # Memory complexity: O(1)   
    weight = [4,4,5,9,9,9,9,9,6,6,5,5,4,3,2,2,2,2,2,1,1,1,1]

    # Time complexity: O(n) n = number of elements in ages
    # Memory complexity: O(1)
    return rn.choices(ages, weights=weight)

# Function that returns a random position and, based on that position, returns a sub-position
def randomPosition():
    # Time complexity: O(1) 
    # Memory complexity: O(1) 
    positionDic = {
        'GOALKEEPER': ['GOALKEEPER'],
        'DEFENDER': ['CENTRAL', 'SIDE'],
        'MIDFIELDER': ['DEFENSIVE', 'CENTRAL MIDFIELDER', 'ATTACKING MIDFIELDER', 'LEFT WINGER', 'RIGHT WINGER'],
        'FORWARD': ['STRIKER', 'SECOND STRIKER', 'WINGER']
    }
    # Time complexity: O(1) 
    # Memory complexity: O(1)   
    percentPosition = [12.5, 34.4, 28.5, 24.6]
    # Time complexity: O(n) n = number of keys in positionDic
    # Memory complexity: O(1)
    chosenPosition = rn.choices(list(positionDic.keys()), weights=percentPosition)[0]
    chosenPositionValues = positionDic[chosenPosition]
    # Time complexity: O(1) 
    # Memory complexity: O(1)
    chosenSubPosition = rn.choice(chosenPositionValues)

    return [chosenPosition, chosenSubPosition]

# Function that returns a random foot preference
def randomFoot():
    # Time complexity: O(1) 
    # Memory complexity: O(1)
    foot = ['RIGHT', 'LEFT']
    # Time complexity: O(1) 
    # Memory complexity: O(1)
    return rn.choices(foot, weights=[7, 3])
