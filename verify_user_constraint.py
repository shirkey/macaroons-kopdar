#!/usr/bin/env python

from create_the_token import get_secret
from deserialize_the_token import deserialize

servis_kopdar = deserialize()
print('servis_kopdar_token: %s' % servis_kopdar.serialize())

# START 1 OMIT
import macaroons
servis_kopdar_token = 'MDAyNmxvY2F0aW9uIGh0dHA6Ly93d3cucHl0aG9uLm9yLmlkLwowMDIzaWRlbnRpZmllciBrb3BkYXJfbWVtYmVyc19vbmx5CjAwMmZzaWduYXR1cmUgPTBa1YP4kNcWeZ9bEeBLautN8R9XueRXQ5uHZ4eQFxAK' # // HL002
client_token = 'MDAyNmxvY2F0aW9uIGh0dHA6Ly93d3cucHl0aG9uLm9yLmlkLwowMDIzaWRlbnRpZmllciBrb3BkYXJfbWVtYmVyc19vbmx5CjAwMTdjaWQgdXNlcmlkPXNoaXJrZXkKMDAyZnNpZ25hdHVyZSA9JIzWgSX2dH5F1eGGsPnNPg0axz7mkh6AnRByzR5/uAo=' # // HL001

def get_access_to_user_resource_path(user_macaroon, resource_path):
    # first, we establish our Verifier as before
    v = macaroons.Verifier()
    v.satisfy_exact('userid=%s' % resource_path)
    return v.verify(user_macaroon, get_secret())

client_macaroon = macaroons.deserialize(client_token) # user macaroon // HL
requested_path = 'shirkey' # user has requested path = shirkey // HL
print('Can access user resource path at %s? %s' % (requested_path, get_access_to_user_resource_path(client_macaroon, requested_path)))
# END 1 OMIT
