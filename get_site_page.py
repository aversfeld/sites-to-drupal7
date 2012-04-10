#!/usr/local/bin/python

###Retrieves a single page from a Google Sites webpage
####


import sys
import re
import atom.data
import gdata.sites.client
import gdata.sites.data
import gdata.gauth

def setup_client(site_name, email_address, password):
  application_name = 'UAServices-migrate-v1'
  client = gdata.sites.client.SitesClient(source=application_name, site=site_name)

  client.ClientLogin(email_address, password, client.source);
  token = client.auth_token

  return client, token


def get_page(client, path):
  """Returns a tuple containing attributes of the target Google Sites page of format:
  Page_Title, Page_Path, Page_Node, _age_Date, Page_Author, Page_Body
  Input parameters:  Client (google session), path(relative path of the page)
  """

  uri = '%s?path=%s' % (client.MakeContentFeedUri(), path)
  feed = client.GetContentFeed(uri=uri, auth=auth_token)
  entry = feed.entry[0]
  page_title = entry.title.text
  page_node = entry.GetNodeId()
  page_date = entry.updated.text
  page_body = str(entry.content.html)
  page_path = entry.GetAlternateLink().href
  page_author = 'unknown'
  return page_title, page_path, page_node, page_date, page_author, page_body

args = sys.argv[1:]
#print args
password, email, site_name = args.pop(), args.pop(), args.pop()
client, auth_token = setup_client(site_name, email, password)
path = '/Urban-Astronomer-Updates/publiclecture-newworldsinsearchofotherearths'
output = get_page(client, path) 
print output
