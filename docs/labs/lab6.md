Lab 6 - API Integration
=======================

## Exercise 6-1 Open Weather Map


## Exercise 6-2 Stocks

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

3. To create price and volume for Google, Apple, and Twitter run
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

## Exercise 6-3 Twitter

To add the metric definitions for this exercise run the following:

1. Change directory to `labs/lab-6`:

    ```
    cd ~/labs/lab-6
    ```

2. Add the metric definitions by running the following:

    ```
    metric-import -f ex6-3.twitter.json
    ```
