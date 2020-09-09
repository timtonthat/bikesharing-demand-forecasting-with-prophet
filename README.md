# FORECASTING BIKE SHARE RENTALS WITH PROPHET

![screenshot](/screenshot.PNG?raw=true "screen shot")

## Description

Bike sharing has been gaining prominence over the last few decades.
Due to the ecologicial and sanitary context, shared bike are likely to definitively conquer the city centers.
To the extent, that forecasting demand has become a strategic issue.
This project illustrates how to forecast bike sharing demands using Prophet.

## Motivation

On my professional activity, I've been working around with timeseries and forecasting problems for a time now. Troughout my different projects, I've used different forecasting techniques (ARIMA, LSTM, ... ) but the one I came to enjoy using the most is Facebook Prophet.

Prophet's approach is not fundamentally disruptive from what have been around in the time series forecasting field for a while now. Yet, it enhance traditional decomposition methods to provide robust and interpretable models thanks to what its authors qualify as a "practical approach to forecasting “at scale”".

This project aims to demontrate prophet's pratical approach.

## How to 

This repositary include a python module to process raw data from [capitalbikeshare.com](https://www.capitalbikeshare.com/system-data) into the csv file used in the notebook.

1. Create a folder named `capitalbikeshare-tripdata`
2. Download files from  capitalbikeshare.com and unzip it in the created folder
3. In terminal , run : ```python process.py```

After the process is done, `capitalbikeshare-dataset-2010-2018.csv` will be found in root directory




## References

This project was inspired by the Kaggle competition: [Bike Share Demand : Forecast the city bikeshare demand](https://www.kaggle.com/c/bike-share-demand)


Original history trip data can be fout at [capitalbikeshare.com](https://www.capitalbikeshare.com/system-data)

Facebook Prophet official page : [https://facebook.github.io/prophet/](https://facebook.github.io/prophet/)
