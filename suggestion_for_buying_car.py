from requests import get
from bs4 import BeautifulSoup
import re
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def decision_tree(price , mile , name , year):
    data_car = pd.DataFrame(list(zip(name , price , mile , year)) , columns=['Name' , 'Price' , 'Mile' , 'Year'])
    data_test = pd.DataFrame([{'price':16500 , 'miles':10000, 'year':2017}])
    try:
        dec_tree = DecisionTreeClassifier().fit(data_car[['Price' , 'Mile' , 'Year']] , data_car[['Name']])
        print(dec_tree.predict(data_test[['price' , 'miles' , 'year']]))
    except Exception as err:
        print(err)

def edit_text(new_price , new_mile , new_name , new_year):
    edit_price = []
    edit_mile = []
    edit_year = []

    for i in new_price: #remove $ from number 
        i.split('$')
        test_para = i[1:]
        last_para = re.sub(',' , '' , test_para)
        edit_price.append(int(last_para))
    
    for j in new_mile: # remove (, miles) form number
        test_para2 = re.sub(',' , '' , j)
        last_para2= test_para2.split()
        edit_mile.append(int(last_para2[0]))

    for k in new_year: #convert to integer
        edit_year.append(int(k))
    
    decision_tree(edit_price , edit_mile , new_name , edit_year)    


def extract_text(old_price , old_mile , old_name , old_year):
    new_price = []
    new_mile = []
    new_name = []
    new_year = []
    
    for ghymat in old_price:
        new_price.append(ghymat.text)
    for mile in old_mile:
        new_mile.append(mile.text)
    for esm in old_name:
        new_name.append(esm.text)
    for years in old_year:
        new_year.append(years.text)

    edit_text( new_price , new_mile ,new_name ,  new_year)

req = get('https://www.truecar.com/used-cars-for-sale/listings/')
soup = BeautifulSoup(req.text , 'html.parser')

price = soup.find_all('div' , attrs={'data-test':'vehicleListingPriceAmount'})
mile = soup.find_all('div' , attrs={'data-test':'vehicleMileage'})
name = soup.find_all('span' , attrs={"class" : "vehicle-header-make-model text-truncate"})
year = soup.find_all('span' , attrs={"class":"vehicle-card-year font-size-1"})


extract_text(price , mile , name , year)