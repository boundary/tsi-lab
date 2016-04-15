Lab 3 - Event APIs
==================


## Overview

Events are notifications of a specific situation that occurs in your environment.
In the implementation there are two types of Events that are manipulated with the API:
_Raw Events_, and _Events_. Each of the event types are described in more detail
in the following sections. _NOTE:_ The scope of these exercises are limited to generation of events,
the querying and extraction of events is not discussed.


### Raw Events

Every event occurrence is persisted as a _Raw Event_ and based upon the _fingerprint_ fields a new _Event_
will be created or an existing event will be used to de-duplicate. Raw Events sent using the API
are the only means by which Events can be created.

### Events

Events are stateful in that the accumulate the field values affected by Raw Events.

### Fingerprint Fields

An array of fields of a Raw Event that are used to calculate whether to generate a new event or
use an existing event (de-duplication). When fingerprint fields are prefixed with '@', such as
@title and @message fields, this indicates that the Raw Event title and/or message fiels should
be used in the computation of what constitutes a duplicate event. Other fields not adorned with `@`
are references to properties associated with the Raw Event. Each field must have a non-null,
non-empty field value with a basic type (string, number, or boolean)

### Properties

_Properties_ key/value pairs that provide additional data to a Raw Event and are able to participate in the
de-duplication of events.

### Sources

Sources identify the origin of an event and consist of key/value pairs of the following:

- Ref
- Type
- Name
- Properties


### Status

Optional free-form text that indicates the disposition of the event. Typical values for status are
the following:

- OPEN
- CLOSED
- ACKNOWLEDGED
- OK

### Severity

_Severity_ is a free-form text that indicates the quality of the event. A typical set of severities are
the following:

- INFO
- WARN
- ERROR
- CRITICAL

### Tags

_Tags_ are additional key/value pairs that provide additional classification of an event.


## Manipulating Events using `curl`

In previous labs we introduced the curl command line utility which permits the generation of HTTP requests
and receipt of the HTTP response. We are going to use curl to generate a Raw Event and the corresponding
Event.

The minimal required fields to generate a raw event consist of:

- Title
- Source
- Fingerprint Fields

for this exercise we add two additional fields:

- Status
- Severity

The fields are used to create a JSON document that becomes the payload of the HTTP request:

```
{
  "title": "test event",
  "fingerprintFields": ["@title", "@message"],
   "status": "OPEN",
   "message": "Hello World!",
   "source": {"ref": "myhost", "type": "host"}
}
```

_NOTE_: During these labs we have made it easier to run the exercises by storing your
credentials and api endpoint information in environment variables as follows:

- `TSP_EMAIL` - TrueSight Intelligence account e-mail address
- `TSP_API_TOKEN` - TrueSight Intelligence API token
- `TSP_API_HOST` - TrueSight Intelligence API endpoint

The complete command to generate a Raw Event including your credentials and api endpoint is
as follows:

```
curl -i "https://$TSP_API_HOST/v1/events" \
-X POST \
-u "$TSP_EMAIL:$TSP_API_TOKEN" \
-H "Content-Type: application/json" \
-d '{
      "title": "test event",
      "fingerprintFields": ["@title", "@message"],
      "message": "Hello World!",
      "status": "OPEN",
      "source": {"ref": "myhost", "type": "host"}
    }'
```

Run the above command as a script located at `labs/lab-2/ex-2-1-events.sh`

## Exercise 3-1 - Creating Additional Events Using `curl`

1. Using the script located at `labs/lab-3/ex-3-1.events.sh` as template create 3 to 5, or more events on
your with the following changed content:

- 3 with status and severity of your choice
- 1 with no severity i.e a change event or an DEV Ops event from chef or puppet

2. Verify and view the events inside the INSIGHTS page in TSI


### TrueSight Pulse Python API library

The TrueSight Pulse Python API can be used to generate an event with having to knowing
the details of generating an HTTP request and handling its response. The API library hides
the details behind the Python language. API Library can be used with Python versions 2.7.10 or later.


### Installing the Python API library

The Python API can be installed via a PyPi package by running the following command:

```
$ pip install tspapi
```

Depending on the installation location of your Python you may have to prefix the above instruction with `sudo`.

_NOTE_: The Vagrant virtual machine already has this library installed so there is no need for this step.
The details are provided here so as to be able to install the libraries on other systems.

### Using the Python API library

To use the Python API in a program you must import and allocate an `API` instance with your e-mail, api-token,
and api endpoint, a snippet of which is shown here:

```
import tspapi

# Allocate an instance of API
api = tspapi.API()
```

### Creating an Event with the Python API Library

With an instance of an `API` you can now create an event by first allocating a source instance:

```
# Create a source instance to identify the orign of the event
source = Source(ref='myhost', _type='host')
```

Next call the `create_event` method on the instance `api`:

```
# Create an event instance
api.event_create(title='Hello World',source=source, fingerprint_fields=['@title])
```
Here is the Python script in its entirety:

```
#!/usr/bin/env python
import tspapi

api = tspapi.API()

source = tspapi.Source(ref='myhost')
api.event_create(title="bar", fingerprint_fields=['@title'], source=source)
```

## Exercise 3-2 - Creating Events Using Python

Run the script `labs\lab-3\ex-2-2.events.py` which contains the Python script from the previous section.

1. Change directory to your home directory:

    ```
    $ cd
    ```

2. Run the following:

    ```
    $ labs\lab-3\ex-2-2.events.py
    ```

## Exercise 3-2 - Creating Additional Events Using Python

Using `labs\lab-3\ex-2-2.events.py` as template create additional events similiary as
you did in exercize 3-1.

