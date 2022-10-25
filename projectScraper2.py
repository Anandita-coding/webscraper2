from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text,'html.parser')
starTable = soup.find_all('table')
templist = []
tablerows = starTable[7].find_all('tr')
for tr in tablerows:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    templist.append(row)

starNames = []
distance = []
mass = []
radius = []

for i in range(1,len(templist)):
    starNames.append(templist[i][0])
for i in range(1,len(templist)):
   distance.append(templist[i][0])
for i in range(1,len(templist)):
    mass.append(templist[i][0])
for i in range(1,len(templist)):
    radius.append(templist[i][0])


df2 = pd.DataFrame(list(zip(starNames,distance,mass,radius)),columns = ['Star Name' , 'Distance', 'Mass' ,'Radius'])
df2.to_csv('BrownDwarf.csv')