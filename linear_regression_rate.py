from requests import get
from bs4 import BeautifulSoup
import re
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def make_linear_regression(raw_price , raw_mile):
    raw_price_series = pd.Series(raw_price)
    raw_mile_series = pd.Series(raw_mile)

    raw_price_series_value = raw_price_series.values
    raw_mile_series_value = raw_mile_series.values

    reshape_raw_price = raw_price_series_value.reshape(-1,1)
    reshape_raw_mile = raw_mile_series_value.reshape(-1,1)

    try:
        lin_reg = LinearRegression().fit(reshape_raw_price,reshape_raw_mile)
        prediction = lin_reg.predict(reshape_raw_mile)
        plt.scatter(reshape_raw_mile , reshape_raw_price , color='r')
        plt.plot(reshape_raw_mile , prediction , color='b')
        plt.show()
    except Exception as err:
        print(err)
    

def edit_text(new_price , new_mile):
    edit_price = []
    edit_mile = []
    
    for i in new_price: #remove $ from number 
        i.split('$')
        test_para = i[1:]
        last_para = re.sub(',' , '' , test_para)
        edit_price.append(int(last_para))
    
    for j in new_mile: # remove (, miles) form number
        test_para2 = re.sub(',' , '' , j)
        last_para2= test_para2.split()
        edit_mile.append(int(last_para2[0]))
    
    make_linear_regression(edit_price,edit_mile)

def extract_text(old_price , old_mile):
    new_price = []
    new_mile = []

    for ghymat in old_price:
        new_price.append(ghymat.text)
    for mile in old_mile:
        new_mile.append(mile.text)
    
    edit_text(new_price , new_mile)

req = get('https://www.truecar.com/used-cars-for-sale/listings/')
soup = BeautifulSoup(req.text , 'html.parser')

price = soup.find_all('div' , attrs={'data-test':'vehicleListingPriceAmount'})
mile = soup.find_all('div' , attrs={'data-test':'vehicleMileage'})

extract_text(price , mile)