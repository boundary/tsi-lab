Lab 2 - Introduction REST
=========================


## Using `curl` to make REST calls.

The `curl` command line utility permits the issuing http(s) request from the command line. The following are examples of its use, which later be used to call the actual APIs.


### Example`GET` request
```
[vagrant@tsi-lab-01 ~]$ curl -X GET -s https://httpbin.org/get 
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.29.0"
  }, 
  "origin": "198.147.195.5", 
  "url": "https://httpbin.org/get"
}
```

### Example GET with parameters
```
[vagrant@tsi-lab-01 ~]$ curl -X GET -s 'https://httpbin.org/get?foo=bar&color=red'
{
  "args": {
    "color": "red", 
    "foo": "bar"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.29.0"
  }, 
  "origin": "198.147.195.5", 
  "url": "https://httpbin.org/get?foo=bar&color=red"
}
```

### Example `POST`



### Example `PUT`


### Example `DELETE`


### Example `POST` with a `JSON` payload


### Status Codes


## TrueSight Pulse APIs

- Metrics
- Measurements
- Events

### Metrics

Metrics are the _thing_ to be measured like CPU or network traffic. A metric is uniquely identified by its name.


##### APIs
- Create
- Get
- Update
- Delete

### Measurements

Measurements represent the the actual time series data point. A measurement consists of 4 pieces of information:

- metric
- value
- source
- timestamp

The timestamp is optionally.

##### APIs

- Create
- Get

### Events

- Create
- Get
- 
