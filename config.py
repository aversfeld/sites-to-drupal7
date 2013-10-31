test = True

#This is the path to the location where Google Liberation tools dumped the tree of xhtml files:
targetPath = "site"

#Modify to suite your drupal site:
user = "admin"
password = "XXXXXXXX"
drupalURL = "http://localhost/xmlrpc.php"



baseURL = '/'.join( drupalURL.split('/')[0:3] )
