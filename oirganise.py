from pandas import read_csv, DataFrame
from numpy import array



def split_data(df: DataFrame, split_ratio = 0.2):
    test_set     = df.sample(frac=split_ratio)
    training_set = df.drop(test_set.index)
    return training_set, test_set



def data_organise(data: DataFrame = None,split_ratio: float = 0): # type: ignore
    if not data:
        data = read_csv("./real_estate.csv")
    if split_ratio > 0 and split_ratio < 1:
        split_data(data, split_ratio)
    # 1st col to 13 (0-12) in features (rest)
    # 14 col in prediction (MEDV)
    x = array(data.iloc[:, : -1])
    y = array(data.iloc[:,   -1])
    return  x, y
