import pandas as pd
from sklearn.model_selection import train_test_split , cross_val_score , RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier # highest score

def prediction(clean_data):
    x_train , x_test , y_train , y_test = train_test_split(clean_data[['ApplicantIncome','CoapplicantIncome',
                                                                   'LoanAmount','Loan_Amount_Term' ,
                                                                   'Female','Rural','Urban']] , clean_data[['Y']] ,
                                                                    test_size= 0.2)
    para ={'criterion' :['gin','entropy'],'max_features' :['auto', 'sqrt', 'log2'] }
    cls = RandomizedSearchCV(RandomForestClassifier(n_estimators = 12) ,para, cv=3 , return_train_score = False , n_iter=3)
    cls.fit(x_train , y_train.values.ravel())
    #print(cls.best_params_)

    random_forest =RandomForestClassifier(n_estimators= 12 , criterion='entropy',max_features='auto')
    random_forest.fit(x_train , y_train.values.ravel())

    print(random_forest.predict(x_test))
    print(y_test)
    #print(random_forest.score(x_test , y_test.values.ravel()))


def clean_data(raw_data):
    raw_data.dropna(subset=['Gender' , 'Married','Self_Employed'] , inplace=True)
    raw_data['LoanAmount'].fillna(raw_data['LoanAmount'].mean() , inplace=True)
    raw_data.drop(['Dependents' , 'Credit_History'] , axis='columns' , inplace=True)
    raw_data.drop(['Loan_ID'] ,axis='columns' , inplace=True)

    gender = pd.get_dummies(raw_data.Gender)
    pr_area = pd.get_dummies(raw_data.Property_Area)
    Loan_status = pd.get_dummies(raw_data.Loan_Status)

    concat_data = pd.concat([raw_data , gender , pr_area , Loan_status] , axis='columns')
    clean_data = concat_data.drop(['Gender' , 'Married' , 'Self_Employed' , 'Education'] , 
                                axis='columns')
    clean_data.drop(['Property_Area' , 'Loan_Status' , 'Male' , 'N' , 'Semiurban'] 
                    , axis='columns' , inplace=True)

    clean_data.dropna(inplace=True)

    prediction(clean_data)

if __name__ == '__main__':
    l = pd.read_csv('train_u6lujuX_CVtuZ9i.csv')
    raw_data = pd.DataFrame(l)

    #print(raw_data.isna().sum())



