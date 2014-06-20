# START 1 OMIT
# user can take the original token provided by the web service,
# and apply additional constraints to it
import macaroons

client_token = 'MDAyNmxvY2F0aW9uIGh0dHA6Ly93d3cucHl0aG9uLm9yLmlkLwowMDIzaWRlbnRpZmllciBrb3BkYXJfbWVtYmVyc19vbmx5CjAwMTdjaWQgdXNlcmlkPXNoaXJrZXkKMDAyZnNpZ25hdHVyZSA9JIzWgSX2dH5F1eGGsPnNPg0axz7mkh6AnRByzR5/uAo='
client_macaroon = macaroons.deserialize(client_token)
new_macaroon = client_macaroon.add_first_party_constraint('time=%') # // HL

# this new token can now be delegated to another user for limited against the service
delegation_token = new_macaroon.serialize()
# END 1 OMIT
