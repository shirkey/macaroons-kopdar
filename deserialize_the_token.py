#!/usr/bin/env python

from create_the_token import get_macaroon

submitted_token = get_macaroon()

def deserialize(token=submitted_token):
    import macaroons
    return macaroons.deserialize(token)

def deserialize_verbose(token=submitted_token):
    # START 1 OMIT
    import macaroons

    # token = "MDAyNmxvY2F0aW9uIGh0dHA6Ly93d3cucHl0aG9uLm9yLmlkLwowMDIzaWRlbnRpZmllciBrb3BkYXJfbWVtYmVyc19vbmx5CjAwMmZzaWduYXR1cmUgPTBa1YP4kNcWeZ9bEeBLautN8R9XueRXQ5uHZ4eQFxAK"

    # first, we attempt to rehydrate a valid macaroon instance from the string # // HL
    try:
        print('Token to be deserialized: %s' % token)
        submitted_macaroon = macaroons.deserialize(token)  # // HL
        # we can check its details
        print('submitted_macaroon.inspect():')
        print(submitted_macaroon.inspect())

    except macaroons.MacaroonError:
        print('The token provided is not a valid macaroon: %s' % token)
    except:
        print 'An unknown error occurred while deserializing the token'

    # END 1 OMIT

if __name__ == "__main__":
    # request the token for inspection
    #submitted_token = raw_input('Enter token to be inspected: ') or submitted_token
    deserialize(submitted_token)
