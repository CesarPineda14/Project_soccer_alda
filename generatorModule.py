import random as rn
from faker import Faker

# funcion que retorna un numero aleatorio entre 10000000-99999999
def randomId():
    return rn.randint(10000000, 99999999)

# funcion que retorna un nombre aleatorio mediante el uo de la libreria Faker
# type("name"): nombre random
# type("LastName"): apellido random
# type("country"): pais random
def randomFaker(type):
    faker = Faker()
    if type=="name":
        return faker.first_name_male()
    elif type=="lastName" :
        return faker.last_name()
    elif type=="country":
        return faker.country()
    

def randomAge():
    ages = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
    weight = [4,4,5,9,9,9,9,9,6,6,5,5,4,3,2,2,2,2,2,1,1,1,1]
    return rn.choices(ages, weights=weight)
    



