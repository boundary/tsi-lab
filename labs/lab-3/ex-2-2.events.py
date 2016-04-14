#!/usr/bin/env python
import tspapi

api = tspapi.API()

source = tspapi.Source(ref='myhost')
api.event_create(title="bar", fingerprint_fields=['@title'], source=source)
