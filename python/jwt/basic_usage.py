#!/usr/bin/env python

import jwt

encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')

print "Basic Encoding using JSON Web Tokens"
print "Encoded:", encoded
print "Decoded:", jwt.decode(encoded, 'secret')
