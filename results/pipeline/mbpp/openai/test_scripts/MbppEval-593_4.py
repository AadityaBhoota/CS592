import re
def removezero_ip(ip):
    parts = ip.split('.')
    
    # Remove leading zeros from each part
    parts = [str(int(part)) for part in parts]
    
    # Join the parts back together using periods
    modified_ip = '.'.join(parts)
    
    return modified_ip

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)