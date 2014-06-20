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
    # notice that we can add constraints to a macaroon without providing the original secret!
    macaroon = servis_kopdar.add_first_party_caveat('userid=%s' % userid) # // HL
    return macaroon

# validate the user via authentication methods
if some_authentication_method(user_id,password):
    user_macaroon = get_user_macaroon(user_id)
    # user_macaroon = user_macaroon.add_first_party_caveat('groupid=kopdar-python')
    print "Our new macaroon: \n", user_macaroon.inspect() # // HL

# END 1 OMIT

