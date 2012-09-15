import re
import urllib
import sys

def parse_sitemap(url):
  """Returns a list of urls for each individual page on a Google Sites website.
  Input: URL of sitemap (<RootURL>/system/feeds/sitemap, probably)
  """
  print url
  ufile = urllib.urlopen(url)
  urlcontents = ufile.readlines()
  urls = ''
  for line in urlcontents:
    if '<loc>' in line:
      urls += line
  messyurls = urls.split('</loc>')
  urllist = list()
  for line in messyurls:
    match = re.search(r'<loc>(.+)', line)
    if match:
      urllist.append(match.group(1))
  return urllist
  


args = sys.argv[1:]
if len(args) != 2:
  print "Usage: urllist.py urlsitemap-url outputfile"
  print "    example:  urllist.py http://sites.google.com/site/foobar/system/feeds/sitemap urls.txt"
  sys.exit()
url = args[0]
outfile = args[1]
ofile = open(outfile, 'w')
urllist = parse_sitemap(url)
print urllist
print len(urllist)
for line in urllist:
  url = line + '\n'
  ofile.write(url)
ofile.close()
