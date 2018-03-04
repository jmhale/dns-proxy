#!/usr/bin/env python3
"""
Create or update a firewall on DigitalOcean
"""

import sys
import os
import socket
import argparse
import digitalocean

try:
    DO_TOKEN = os.environ["DO_TOKEN"]
except KeyError:
    print("Please set your DigitalOcean API key in the environment variable DO_TOKEN")
    sys.exit(1)

PARSER = argparse.ArgumentParser()
PARSER.add_argument('region', type=str)

FIREWALL_NAME = "dns-proxy"

class ManageFirewall(object):
    """ Functions to manage the DigitalOceal Firewall """

    def __init__(self, region):
        self.manager = digitalocean.Manager(token=DO_TOKEN)
        self.region = region
        self.firewall = None
        self.primary_ip = socket.gethostbyname('dyn.makeithale.com')
        self.secondary_ip = socket.gethostbyname('hale-ma.ddns.net')

    def check_for_firewall(self):
        """ Checks if the firewall object already exists """
        if self.firewall:
            print("Firewall found. Proceeding with update.")
            self.update_firewall()
        else:
            print("No firewall found. Creating...")
            self.create_firewall()


    def create_firewall(self):
        """ Creates the firewall object """
        pass

    def update_firewall(self):
        """ Updates the existing firewall with new IPs """
        self.get_rules()
        pass


    def get_rules(self):
        """ Prints the inbound and outbound firewall rules """
        inbound_rules = self.firewall.inbound_rules
        print "Checking inbound rules:"
        for inbound_rule in inbound_rules:
            ports = inbound_rule.ports
            ip_addrs = inbound_rule.sources.addresses

            if self.check_for_admin_rule(inbound_rule):
                print "Admin rule in place"
                break
            else:
                print "Admin rule missing."
                # call to set admin rule
                break


    def check_for_admin_rule(self, rule):
        """ Checks the rules for allowing SSH """
        if rule.ports == "22":
            for address in rule.sources.addresses:
                if address == self.primary_ip:
                    print "SSH rule found for primary IP. Not taking action."
                    return True

        return False

    def check_for_dns_rule(self, rule):
        """ Check the rule for allowing DNS """
        if rule.ports == "53"
            for address in rule.sources.addresses:
                if address == self.primary_ip:
                    


    def get_firewall(self):
        """ Gets the Firewall object by name """
        firewalls = self.manager.get_all_firewalls()
        for firewall in firewalls:
            if firewall.name == FIREWALL_NAME:
                self.firewall = firewall
                break

        return None

    def print_id(self):
        """ Prints the firewall ID """
        print "Firewall ID is: %s" % self.firewall.id


def main(region):
    """ Entrypoint """
    manage_firewall = ManageFirewall(region)
    manage_firewall.get_firewall()
    manage_firewall.check_for_firewall()
    # check_for_firewall(manager, region)
    # create_firewall(manager, region)

if __name__ == "__main__":
    ARGS = PARSER.parse_args()
    main(ARGS.region)
