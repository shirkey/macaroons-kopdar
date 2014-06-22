macaroons-kopdar
================

Distributed Web Security with Macaroons (KopDar Python Presentation)
=======

## Overview
This is a presentation given for the [KopDar Python Meetup](http://www.meetup.com/Python-ID/events/187061422/) 
held at [IceHouse](http://www.icehousecorp.com) offices in Jakarta, Indonesia on 21-June-2014. 

The presentation is intended to provide a brief introduction to macaroons for creating distributed credentials.

The included Python source code provides the steps necessary to leverage [libmacaroons](http://github.com/rescrv/libmacaroons) to:
* create a simple macaroon
* inspecting a macaroon
* serialize a macaroon into a token
* deserializing a token into a macaroon
* validating a macaroon signature
* attentuate a macaroon by adding first-party caveats by the service
* validating the presence of caveats in a token received by the service
* attentuate a macaroon from outside of the originating service layer

This presentation only offers a basic coverage of the much more complete functionality and 
documentation offered at the libmacaroons repository. 
Further details about the concepts behind macaroons are available in the original [research paper](http://research.google.com/pubs/pub41892.html).

## Contents
* Presentation Slides (in go.tools present format)
* Installation script for libmacaroons (Debian/Ubuntu only)
* Python Source Code

## Installing / Running
To run the source code, you will need to install libmacaroons.

You will also need a recent version of Python 2.x (such as Python 2.7+) installed.

To run the presentation itself, you will need [Go version 1+](http://golang.org/) and 
[go.tools/present](http://godoc.org/code.google.com/p/go.tools/present) installed. 

If you already have Go installed, running ./start-slideshow.sh will first attempt to install 
the go.tools/present package, then launch the localhost web app used by present and finally open the default web browser to the local presentation URL.
>>>>>>> master
