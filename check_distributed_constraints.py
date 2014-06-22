#!/usr/bin/env python
import macaroons
from create_the_token import get_secret
from datetime import datetime, timedelta
client_token = 'MDAyNmxvY2F0aW9uIGh0dHA6Ly93d3cucHl0aG9uLm9yLmlkLwowMDIzaWRlbnRpZmllciBrb3BkYXJfbWVtYmVyc19vbmx5CjAwMTdjaWQgdXNlcmlkPXNoaXJrZXkKMDAyZnNpZ25hdHVyZSA9JIzWgSX2dH5F1eGGsPnNPg0axz7mkh6AnRByzR5/uAo='
# user can take the original token provided by the web service,
# and apply additional constraints to it
client_macaroon = macaroons.deserialize(client_token) # // HL
timeout = datetime.now().date() # // HL

new_macaroon = client_macaroon.add_first_party_caveat('date=%s' % timeout) # // HL
print 'newly constrained macaroon:\n', new_macaroon.inspect()
# this new token can now be delegated to another user for limited against the service
delegation_token = new_macaroon.serialize()
path='shirkey'
# START 1 OMIT

# servis_kopdar obtains token from third party (not original client)
print delegation_token
asserting_macaroon = macaroons.deserialize(delegation_token)
print 'Asserting macaroon: \n', asserting_macaroon.inspect()

# the web service must support constraint checking for the specified caveat
# so let's add a check for this constraint
def get_access_to_user_resource_path(user_macaroon, resource_path):
    # first, we establish our Verifier as before
    v = macaroons.Verifier()
    v.satisfy_exact('userid=%s' % resource_path)
    v.satisfy_exact('date=%s' % datetime.now().date())  # // HL
    return v.verify(user_macaroon, get_secret())

print "Is the user authorized to this resource? %s" % \
    get_access_to_user_resource_path(asserting_macaroon, path)
# END 1 OMIT
