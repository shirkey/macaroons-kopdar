#!/usr/bin/env bash
if (( $EUID != 0 )); then
    echo "Please run as root"
        exit
    fi

# START OMIT
#run as root/sudo
wget -O - http://ubuntu.hyperdex.org/hyperdex.gpg.key | apt-key add -
wget -O /etc/apt/sources.list.d/hyperdex.list http://ubuntu.hyperdex.org/trusty.list
apt-get update
apt-get install python-macaroons
# END OMIT
