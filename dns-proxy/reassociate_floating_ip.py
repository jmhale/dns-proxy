#!/usr/bin/env python3
"""
Re-associates floating IP with the given droplet
"""

import os
import sys
import argparse
import time
import digitalocean

try:
    DO_TOKEN = os.environ["DO_TOKEN"]
except KeyError:
    print("Please set your DigitalOcean API key in the environment variable DO_TOKEN")
    sys.exit(1)

PARSER = argparse.ArgumentParser()
PARSER.add_argument('droplet_id', type=str)
PARSER.add_argument('region', type=str)

IP_ADDRESSES = {
    'nyc1': '45.55.107.76',
    'nyc3': '159.203.144.22'
}

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
        old_droplet_id = floating_ip.droplet['id']
        with open('.properties', 'a') as out:
            out.write('DROPLET_ID=' + str(old_droplet_id) + '\n')
        print("Unassociating Floating IP from Droplet: {}".format(old_droplet_id))
        floating_ip.unassign()
    except digitalocean.baseapi.DataReadError:
        print("Floating IP not associated to a droplet. Not trying to unassign.")

def _associate_ip(manager, ip_address, droplet_id):
    " Associate the floating ip with a droplet "
    floating_ip = _get_floating_ip(manager, ip_address)
    while True:
        try:
            floating_ip.assign(droplet_id)
            break
        except digitalocean.baseapi.DataReadError:
            print("Floating IP yet not available for assignment. Sleeping 10 seconds...")
            time.sleep(10)

def reassociate_ip(droplet_id, ip_address):
    " Reassociate floating IP with Droplet "
    manager = _get_manager()
    _disassociate_ip(manager, ip_address)
    _associate_ip(manager, ip_address, droplet_id)

def main(droplet_id, region):
    " Entrypoint for commandline execution "
    reassociate_ip(droplet_id, IP_ADDRESSES[region])

if __name__ == "__main__":
    ARGS = PARSER.parse_args()
    main(ARGS.droplet_id, ARGS.region)
