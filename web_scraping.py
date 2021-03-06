import mysql.connector
import requests
from bs4 import BeautifulSoup

#REQUESTS TO SITE (.com)
for i in range(30):
    url1 ="https://www.truecar.com/used-cars-for-sale/listings/".format(i)
    link = requests.get(url1)
    soup = BeautifulSoup(link.text , 'html.parser')

esm = soup.find_all('span' , attrs={"class" : "vehicle-header-make-model text-truncate"})
kar = soup.find_all('div' , attrs={"data-test" : "vehicleMileage"})
sal = soup.find_all('span' , attrs={"class":"vehicle-card-year font-size-1"})
ghymat = soup.find_all('div' , attrs={"class":"heading-3 margin-y-1 font-weight-bold"})


cnx = mysql.connector.connect(user='' , password='' , host='127.0.0.1' , database='last')
cursor = cnx.cursor()

#write in database
for name in esm:
    for work in kar:
        for years in sal:
            for price in ghymat:
                cursor.execute('INSERT INTO info VALUES(\'%s\' , \'%s\' , \'%s\' , \'%s\')' %(name.text , work.text , years.text , price.text))
                cnx.commit()
                ghymat = ghymat[1:]
                break
            sal = sal[1:]
            break
        kar = kar[1:]
        break
cnx.close()
