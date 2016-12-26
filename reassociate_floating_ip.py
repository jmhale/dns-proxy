#!/usr/bin/env python3
"""
Re-associates floating IP with the given droplet
"""

import os
import sys
import argparse
import digitalocean

try:
    DO_TOKEN = os.environ["DO_TOKEN"]
except KeyError:
    print("Please set your DigitalOcean API key in the environment variable DO_TOKEN")
    sys.exit(1)

PARSER = argparse.ArgumentParser()
PARSER.add_argument('droplet_id', type=str)
PARSER.add_argument('ip_address', type=str)

def _get_manager():
    " Sets up the manager "
    return digitalocean.Manager(token=DO_TOKEN)

def _get_floating_ip(manager, ip_address):
    " Return the Floating IP object"
    return manager.get_floating_ip(ip_address)

def _disassociate_ip(manager, ip_address):
    " Disassociate the floating ip. "
    floating_ip = _get_floating_ip(manager, ip_address)
    try:
        floating_ip.unassign()
    except digitalocean.baseapi.DataReadError:
        print("Floating IP not associated to a droplet. Not trying to unassign.")

def _associate_ip(manager, ip_address, droplet_id):
    " Associate the floating ip with a droplet "
    floating_ip = _get_floating_ip(manager, ip_address)
    floating_ip.assign(droplet_id)

def reassociate_ip(droplet_id, ip_address):
    " Reassociate floating IP with Droplet "
    manager = _get_manager()
    _disassociate_ip(manager, ip_address)
    _associate_ip(manager, ip_address, droplet_id)

def main(droplet_id, ip_address):
    " Entrypoint for commandline execution "
    reassociate_ip(droplet_id, ip_address)

if __name__ == "__main__":
    ARGS = PARSER.parse_args()
    main(ARGS.droplet_id, ARGS.ip_address)
