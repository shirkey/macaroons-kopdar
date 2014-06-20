#!/usr/bin/env python
# encoding: utf-8

def create_service_token():
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

    # START 2 OMIT
    # with these three arguments, we can now create the macaroon
    servis_kopdar = macaroons.create(location, secret, public)

    # we now hold a reference to our newly instantiated macaroon object
    print servis_kopdar

    # we can print the HMAC signature of this message
    print '.signature: %s' % servis_kopdar.signature

    # and we can convert the macaroon object to a serialized form for transport
    print '.serialize(): %s' % servis_kopdar.serialize()

    # END 2 OMIT
    return servis_kopdar

if __name__ == "__main__":
    create_service_token()
