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
    print("Please set your DigitalOcean API key in the environment variable DO_TOKEN")
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
    droplet.create()
    return droplet.id

def main(region):
    " Create the droplet in the given region "
    droplet_id = create_droplet(region)
    with open('.properties', 'a') as out:
        out.write('DROPLET_ID=' + str(droplet_id) + '\n')
    print(droplet_id)

if __name__ == "__main__":
    ARGS = PARSER.parse_args()
    main(ARGS.region)
