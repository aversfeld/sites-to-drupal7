#!/usr/local/bin/python
"""Migrates a single page from Google Sites (as defined in config.py), and loads it as a new node
into an installation of Drupal7 (also defined in config.py)
"""

from config import config_local, config_google
from get_site_page import *



def main():
  client, auth_token = setup_client(config_google['sitename'], config_google['email_address'], config_google['password'])

if __name__ == '__main__':
  main()
