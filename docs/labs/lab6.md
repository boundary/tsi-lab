Lab 6 - API Integration
=======================

With all you have learned regarding the Event, Metric, and Measurements APIs it is time
put your new knowledge to some interesting examples. Hold on tight, make sure your
parachute is packed, we are climbing to 10,000, be ready to bail out.

The three exercises we have in store for are:

1. Collecting your favorite stocks pricing and volume (Commission Free!)
2. Collecting temperature from your favorite city
3. Collecting some statistics of your Twitter feed.

## Exercise 6-1 Stocks

In this example we use the `ystockquote` Python package to send measurements to send stock pricing
and volume given the stock ticker to TrueSight Intelligence.

The stock script allows multiple tickers to be passed on the command line and their corresponding
price and volume will be sent to TrueSight Intelligence.

### Adding the metric definitions

To add the metric definitions for this exercise run the following:

1. Change directory to `labs/lab-6`:

    ```
    cd ~/labs/lab-6
    ```

2. Add the metric definitions by running the following:

    ```
    metric-import -f ex6-2.stocks.json
    ```

### Sending Stock Price and Volume Measurements to TrueSight Intelligence

1. To create measurements of stock prices and volume for Google, Apple, and Twitter run
the following:

    ```
    ex6-2.stock.py goog aapl twtr
    ```

The output should be similar to the following:

```
ticker: goog, price: 759.24, volume: 896107
ticker: aapl, price: 111.83, volume: 12232507
ticker: twtr, price: 17.695, volume: 8318681
ticker: goog, price: 759.24, volume: 896151
ticker: aapl, price: 111.82, volume: 12238391
ticker: twtr, price: 17.69, volume: 8318981
```

## Exercise 6-2 Open Weather Map

> Climate is what we expect,
> weather is what we get.

Mark Twain

Let's talk about the weather. For this exercise we are heating up and will create a
script that collects data from you favorite city or cities.

We are going to the exploit the services of the [Open Weather Map API](http://openweathermap.org/api)


### Obtaining Open Weather Map API Keys

**To Be Completed**


### Adding the metric definitions

To add the metric definitions for this exercise run the following:

1. Change directory to `labs/lab-6`:

    ```
    cd ~/labs/lab-6
    ```

2. Add the metric definitions by running the following:

    ```
    metric-import -f ex6-2.weather.json
    ```

## Running the weather collection script

1. Change directory to `labs/lab-6`:

    ```
    cd ~/labs/lab-6
    ```

2. To create weather data for San Jose, CA run the following:

    ```
    ex6-2.weather.py "San Jose, CA"
    ```

## Exercise 6-3 Twitter


### Obtaining your Twitter API Keys

**To Be Completed**

### Adding the metric definitions

To add the metric definitions for this exercise run the following:

1. Change directory to `labs/lab-6`:

    ```
    cd ~/labs/lab-6
    ```

2. Add the metric definitions by running the following:

    ```
    metric-import -f ex6-3.twitter.json
    ```
