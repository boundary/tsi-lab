#!/usr/bin/env python

import tspapi

# Options, can set the credentials via environment variables or passed to the constructor
# of the API class
api = tspapi.API()

source = tspapi.Source(ref='myhost')
api.event_create(title="bar", fingerprint_fields=['@title'], source=source)
