###DNS proxy

TL;DR: Creates an instance on DigitalOcean running bind9 and sniproxy to allow proxying some traffic through your instance.

This is a set of scripts that I created to help automate deploying a couple of DNS/proxy instances to DigtialOcean droplets.

I'm using them in a Jenkins pipeline, but they're pretty simple and can be adapted for anything (or nothing! Just run them.)

The scripts have some env-specific configs, so they're not meant to be a turn-key solution for anyone else. However, they're straight-forward enough that they can be easily adapted to suit your needs.
