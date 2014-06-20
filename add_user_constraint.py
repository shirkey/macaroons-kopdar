#!/usr/bin/env python

from create_the_token import get_secret
from deserialize_the_token import deserialize

servis_kopdar = deserialize()

def some_authentication_method(x,y):
    return True
# START 1 OMIT

print servis_kopdar.inspect() # the original/base macaroon for the web service // HL

user_id = 'shirkey' # // the user's id HL
password = '123456' # // the user's password

# helper function for generating user-constrained macaroon
def get_user_macaroon(userid):
    macaroon = servis_kopdar.add_first_party_caveat('userid=%s' % userid); # // HL
    return macaroon

# validate the user via authentication methods
if some_authentication_method(user_id,password):
    user_macaroon = get_user_macaroon(user_id)
    #user_macaroon.add_first_party_caveat('kopdar-python')
    print 'user_macaroon.inspect():'
    print user_macaroon.inspect() # // HL

    # macaroon can be serialized for client-side use
    print user_macaroon.serialize()

# END 1 OMIT

