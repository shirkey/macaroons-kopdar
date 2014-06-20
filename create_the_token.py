#!/usr/bin/env python
# encoding: utf-8

# START 1 OMIT
import macaroons

# a basic macaroon consists of three elements

# 1) the secret key known only to the credential authority (a web service or software)
secret = 'kopdar_python_rocks'

# 2) some interesting metadata about this macaroon (can be anything)
public = 'kopdar_members_only'

# 3) a URI/URL, possibly referencing a targeted web service (again, can be anything)
location = 'http://www.python.or.id/'

# END 1 OMIT

def get_macaroon():

    servis_kopdar = macaroons.create(location, secret, public)
    return servis_kopdar.serialize()

def get_secret():
    return secret

if __name__ == "__main__":

    # START 2 OMIT
    # with these three arguments, we can now create the macaroon
    servis_kopdar = macaroons.create(location, secret, public)

    # we now hold a reference to our newly instantiated macaroon object
    print servis_kopdar

    # we can inspect the HMAC signature of this message
    print '.signature: %s' % servis_kopdar.signature

    # or the other public metadata, like identifier or location
    print '.identifier: %s' % servis_kopdar.identifier
    print '.location: %s' % servis_kopdar.location

    # or all the metadata + signature as one call
    print '.inspect(): '
    print servis_kopdar.inspect()

    # finally, we can convert the macaroon object to a serialized form for transport
    print '.serialize(): %s' % servis_kopdar.serialize()

    # END 2 OMIT
    get_macaroon()
