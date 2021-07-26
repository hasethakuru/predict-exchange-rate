import pandas
import numpy

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('dataset.csv')
latest = data.loc[data['year'] == data['year'].iloc[-1]]
rate = data.iloc[latest.index[0], 1]
yr = data.iloc[latest.index[0], 0]
rates = data['exchangeRate']
lr = LinearRegression()

# USD into INR

def predictByLatest(year):
    previousYearRate = data.iloc[latest.index[0]-1, 1]
    diff = year - yr

    print(f'Exchange Rate (by Latest) of India in {year} will be ₹{str(round(rate + (rate - previousYearRate) * diff))}')

def predictByAverage(year):
    avg = numpy.std(rates)
    diff = year - yr

    print(f'Exchange Rate (by Average) of India in {year} will be ₹{str(round(rate + (avg * diff)))}')   

def predictByLast3(year):
    latestThree = numpy.array(rates[len(rates)-3:])

    avg = numpy.std(latestThree)
    diff = year - yr

    print(f'Exchange Rate (by Avg of last 3) of India in {year} will be ₹{str(round(rate + (avg * diff)))}')   

def predictByLinearRegression(year):
    X = data[['year']]
    y = data['exchangeRate']

    lr.fit(X, y)

    prediction = lr.predict([[year]])

    print(f'Exchange Rate (by Linear Regression) of India in {year} will be ₹{round(prediction[0])}')   

def predict(year):
    predictByLast3(year)
    predictByAverage(year)
    predictByLatest(year)
    predictByLinearRegression(year)

predict(2050)
print('\n')