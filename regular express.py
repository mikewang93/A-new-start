import re

# Try to match a ip address
re.search(r'(([01]{0,1}\d{0,3}\d{0,3})\.){3}[01]{0,1}\d{0,3}\d{0,3}','192.168.1.1')
