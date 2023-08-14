
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_pistols" #Change Website URL
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
titles=[]
images=[]

table = soup.find("table")

for row in table.find_all("tr"):

    tds = row.find_all("td")
    if len(tds) >= 5:

        image = tds[2]
        
        if len(image.findChildren()) > 0:
            image = image.findChildren()[0]
            image = str(image).split('src="')[1]
            image = image.split('"')[0]
            images.append(image)

            title = tds[0].get_text()
            title = title.replace("'","")
            titles.append(title)

formula = "INSERT INTO AssaultRifles (name,image) VALUES " #Change Table name

x=0
while x < len(titles):
    formula = formula + "('" + titles[x] + "','" + images[x] + "'),"
    x+=1

formula = formula + ");"

print(formula)