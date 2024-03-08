import generatorModule as gen
import graphModule as gm
import pandas as pd

import webbrowser

def randomFuntion(rows):
    # Time complexity: O(1)
    # Memory complexity: O(1)
    dataDic = []

    # Time complexity: O(n) n = row
    # Memory complexity: O(1)
    for x in range(rows):
        position = gen.randomPosition()
        print("Number of Row Generated: "+str(x+1))

        # Time complexity: O(1) 
        # Memory complexity: O(n) n = row
        dataDic.append( {
                        "ID":gen.randomId(),
                        'Name': gen.randomFaker("name"),
                        'LastName':gen.randomFaker("lastName"),
                        'Country':gen.randomFaker("country"),
                        'Age':gen.randomAge()[0],
                        'Position':position[0],
                        'Sub_Position':position[1],
                        'Pie Dominante':gen.randomFoot()[0]
                        })
        # Time complexity: O(n) n = row
        # Memory complexity: O(n) n = row
        df = pd.DataFrame(dataDic)
    df.to_excel('data.xlsx', index=False)
    


def main():
    # Time complexity: O(1)
    # Memory complexity: O(1)
    rows = input("Enter the number of rows to be generated:  ")
    randomFuntion(int(rows))

if __name__ == "__main__":
    main()