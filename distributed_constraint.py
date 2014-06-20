#!/usr/bin/env python
import macaroons
from datetime import datetime, timedelta
client_token = 'MDAyNmxvY2F0aW9uIGh0dHA6Ly93d3cucHl0aG9uLm9yLmlkLwowMDIzaWRlbnRpZmllciBrb3BkYXJfbWVtYmVyc19vbmx5CjAwMTdjaWQgdXNlcmlkPXNoaXJrZXkKMDAyZnNpZ25hdHVyZSA9JIzWgSX2dH5F1eGGsPnNPg0axz7mkh6AnRByzR5/uAo='
# START 1 OMIT
# user can take the original token provided by the web service,
# and apply additional constraints to it
client_macaroon = macaroons.deserialize(client_token) # // HL
timeout = datetime.now().date() # // HL

new_macaroon = client_macaroon.add_first_party_caveat('date=%s' % timeout) # // HL
print 'newly constrained macaroon:\n', new_macaroon.inspect()
# this new token can now be delegated to another user for limited against the service
delegation_token = new_macaroon.serialize()
# END 1 OMIT
