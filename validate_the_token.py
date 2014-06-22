#!/usr/bin/env python

from deserialize_the_token import deserialize

macaroon = deserialize()

def validate_verbose(submitted_macaroon=macaroon):
    # START 1 OMIT

    import macaroons

    # validation occurs using a Verifier object
    v = macaroons.Verifier() # // HL

    # we'll need the original secret we created earlier
    secret = 'kopdar_python_rocks'  # // HL
    # secret = 'kopdar_python_is_ok-lah'

    # we attempt to verify the submitted macaroon
    print "Is the secret '%s'? -- %s" % (secret, v.verify(submitted_macaroon, secret)) # // HL
    # END 1 OMIT

if __name__ == "__main__":
    validate_verbose()
