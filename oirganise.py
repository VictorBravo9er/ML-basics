import pandas as pd

def data_organise():
    data = pd.read_csv("./real_estate.csv")
    
    # 1st col to 13 (0-12) in features (rest)
    # 14 col in prediction (MEDV)

    data_feature = data[data['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']]