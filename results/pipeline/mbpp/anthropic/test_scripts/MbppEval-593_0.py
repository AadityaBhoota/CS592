import re

def removezero_ip(ip):
    octets = ip.split('.')
    octets = [str(int(octet)) for octet in octets]
    result = '.'.join(octets)
    return result

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)