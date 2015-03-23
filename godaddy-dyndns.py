#!/usr/bin/env python3

import configparser
import logging
import sys

import pif
import pygodaddy


logging.basicConfig(filename='godaddy-dyndns.log',
		    format='%(asctime)s %(message)s',
		    level=logging.INFO)   
config = configparser.ConfigParser()
config.read('godaddy-dyndns.conf')

client = pygodaddy.GoDaddyClient()
is_logged_in = client.login(config.get('godaddy', 'username'),
			    config.get('godaddy', 'password'))
if not is_logged_in:
    logging.error('Login failed!')
    sys.exit(1)

for domain in client.find_domains():
    dns_records = list(client.find_dns_records(domain))
    public_ip = pif.get_public_ip()
    logging.info("Domain '{0}' DNS records: {1}".format(domain, dns_records))
    if public_ip != dns_records[0].value:
        client.update_dns_record(domain, public_ip)
        logging.info("Domain '{0}' public IP set to '{1}'".format(domain, public_ip))
