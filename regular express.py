import re

# Try to match a ip address
re.search(r'(([01]{0,1}\d{0,3}\d{0,3})\.){3}[01]{0,1}\d{0,3}\d{0,3}','192.168.1.1')
#try to match some charactor

re.search(r'[a-z]{4}','mike')

#.+*？

re.search(r'[01]\d\d|2[0-4]\d|25[0-5]','192')
