import xmlrpclib
import config

proxy = xmlrpclib.ServerProxy(config.drupalURL, allow_none=True)

ctype = 'article'
meth = proxy.bulkpub.deletePages


checkPrompt = raw_input("About to delete ALL content of type '" + ctype + "' from " + config.baseURL + ".  Are you sure? ")
if checkPrompt == "y" or checkPrompt == "Y":
  print "Deleting..."
  count = meth('', ctype,  config.user, config.password)
  print str(count) + " articles deleted."
