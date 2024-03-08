import plotly.express as px
import webbrowser
import pandas as pd



def pieGraph(datadic, grapName,columnName):
    grap = px.pie(datadic, values='count', names=columnName, title=grapName)
    grap.write_html(columnName + ".html")
    




def dicFormater(dataList, name, columnName):
    AgeCount = {}
    for x in dataList:
        if x in AgeCount:
            AgeCount[x] +=1
        else:
            AgeCount[x] = 1

    data = pd.DataFrame(list(AgeCount.items()), columns=[columnName, 'count'])
    pieGraph(data, name, columnName)
        
def openBrowser():
    webbrowser.open("index.html", new=2)