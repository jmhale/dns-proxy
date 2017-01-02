#!/usr/bin/env python3
"""
Terminate a DigitalOcean instance
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

def _get_manager():
    " Sets up the manager "
    return digitalocean.Manager(token=DO_TOKEN)

def _get_droplet(manager, droplet_id):
    " Return the Droplet object"
    return manager.get_droplet(droplet_id)

def terminate_droplet(droplet_id):
    " Terminates the droplet "

    manager = _get_manager()
    droplet = _get_droplet(manager, droplet_id)
    print("Terminating Droplet: {}".format(droplet.name))
    droplet.destroy()
    print("Droplet: {} destroyed. :(".format(droplet.name))


def main(droplet_id):
    " Destroys the droplet with the given ID. "
    terminate_droplet(droplet_id)

if __name__ == "__main__":
    ARGS = PARSER.parse_args()
    main(ARGS.droplet_id)
