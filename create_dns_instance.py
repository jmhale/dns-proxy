#!/usr/bin/env python3
"""
Create a DNS proxy instance on DigitalOcean
"""

from datetime import datetime
import os
import sys
import argparse
import digitalocean
from userdata import USER_DATA

try:
    DO_TOKEN = os.environ["DO_TOKEN"]
except KeyError:
    print("Please set the environment variable DO_TOKEN")
    sys.exit(1)

PARSER = argparse.ArgumentParser()
PARSER.add_argument('region', type=str)

def create_droplet(region):
    " Creates the droplet "
    droplet_name = "dns-proxy-{}-{}".format(region, datetime.now().strftime('%Y%m%d%H%M%S'))
    print("Creating Droplet: {}".format(droplet_name))
    manager = digitalocean.Manager(token=DO_TOKEN)
    keys = manager.get_all_sshkeys()

    droplet = digitalocean.Droplet(token=DO_TOKEN,
                                   name=droplet_name,
                                   region=region,
                                   image='ubuntu-14-04-x64',
                                   size_slug='512mb',
                                   ssh_keys=keys,
                                   backups=False,
                                   user_data=USER_DATA)
    print(droplet.create())

def main(region):
    " Create the droplet in the given region "
    create_droplet(region)

if __name__ == "__main__":
    ARGS = PARSER.parse_args()
    main(ARGS.region)
