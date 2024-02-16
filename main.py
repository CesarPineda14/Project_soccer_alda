import generatorModule as gen
import pandas as pd


dataDic = [
    
]


for x in range(7):
    dataDic.append( {
                    "ID":gen.randomId(),
                    'Name': gen.randomFaker("name"),
                    'LastName':gen.randomFaker("lastName"),
                    'Country':gen.randomFaker("country"),
                    'Age':gen.randomAge()[0],
                    })


df = pd.DataFrame(dataDic)

print(df)